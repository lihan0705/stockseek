# market_data_agent.py

from smolagents import (
    LiteLLMModel,
    tool
)
from smolagents.agents import ToolCallingAgent
from src.tools.api import (
    get_financial_metrics,
    get_financial_statements,
    get_market_data,
    get_price_history
)

@tool
def fetch_financial_metrics(ticker: str) -> dict:
    """
    Retrieve financial metrics for a given ticker.

    Args:
        ticker: The stock ticker symbol (e.g., "AAPL").

    """
    return get_financial_metrics(ticker)


@tool
def fetch_financial_statements(ticker: str) -> dict:
    """
    Fetch financial metrics for the given stock ticker.

    Args:
        ticker: The stock ticker symbol (e.g., "AAPL").
    """
    return get_financial_statements(ticker)


@tool
def fetch_market_data(ticker: str) -> dict:
    """
    Retrieve market data (market cap, volume, etc.) for the given ticker.
    Args:
        ticker: The stock ticker symbol (e.g., "AAPL").
    """
    return get_market_data(ticker)


@tool
def fetch_price_history(ticker: str, start_date: str, end_date: str) -> list:
    """
    Retrieve price history for [ticker] from [start_date] to [end_date]. 
    Returns a list of dict (like df.to_dict('records')).
    Args:
        ticker: The stock ticker symbol (e.g., "AAPL").
        start_date: research start time.
        end_date: research end time
    """
    df = get_price_history(ticker, start_date, end_date)
    if df is None or df.empty:
        return []
    return df.to_dict("records")

def create_market_data_agent(model_id: str = "ollama/llama3.1:8b") -> ToolCallingAgent:
    """
    Create a ToolCallingAgent that has multiple tools for fetching market data
    (prices, financial metrics, statements, etc.).
    """
    # 1) Instantiate the model
    model = LiteLLMModel(model_id=model_id)

    # 2) Initialize a ToolCallingAgent with these tools
    agent = ToolCallingAgent(
        tools=[
            fetch_financial_metrics,
            fetch_financial_statements,
            fetch_price_history,
            fetch_market_data,
        ],
        model=model,
        max_steps=2,
        # optionally you can add more config like system_prompt, user_prompt, etc.
    )

    return agent
