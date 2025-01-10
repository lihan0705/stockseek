from transformers import tool
import yfinance as yf
import pandas as pd
import json
from smolagents import CodeAgent, LiteLLMModel, ManagedAgent, ToolCallingAgent
from src.simple_agents.api import get_price_history

@tool
def get_historical_prices(symbol: str, start_date: str, end_date: str) -> str:
    """
    Fetches historical prices for a given stock symbol and returns them as a JSON string.

    Args:
       symbol: The symbol of the stock.
       start_date: The start date of the historical prices, formatted as 'YYYY-MM-DD'.
       end_date: The end date of the historical prices, formatted as 'YYYY-MM-DD'.
       kwargs: any
    Returns:
        str: Historical stock prices as a JSON string.
    """
    # Fetch historical data using yfinance
    data = get_price_history(symbol, start_date=start_date, end_date=end_date)
    # Drop the second level of MultiIndex if it exists
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1)

    data.reset_index(inplace=True)
    data["date"] = data["date"].astype(str)  # Convert Timestamp to string

    # Convert DataFrame to a dictionary and then to JSON string
    result = data.to_dict(orient="records")
    return json.dumps(result)

# start_date = "2024-01-01"
# end_date = "2024-12-31"
# nvidia_prices_json = get_historical_prices(symbol="NVDA", start_date=start_date, end_date=end_date)
# nvidia_prices = json.loads(nvidia_prices_json)
# print(nvidia_prices)
# exit()

model = LiteLLMModel("ollama/qwen2.5")


data_agent = CodeAgent(tools=[get_historical_prices], 
                  model=model, 
                  add_base_tools=True,
                  additional_authorized_imports=['numpy','yfinance','pandas','json'],
                  max_steps=4)

inversting_manager_agent = ManagedAgent(
    agent=data_agent,
    name="inversting manager",
    description="base on data from data agent, analyze stock, make a reporter the company infomation"
)

output = inversting_manager_agent(request="Fetch the NVIDIA historical stock prices for 2024-6-1 to 2024-12-31? what is trend of the stock?")
print(output)
