# AI StockSeek
This is a proof-of-concept project for an AI-based investment system. The project's goal is to explore how AI can assist in investment decision-making. This project is for **educational purposes only** and is not suitable for actual trading or investment.
### TODO
```bash
1. local ollama llm based agent
2. adapter to US stock market
3. different agent frame result comparsion
    a. simple version langgraph(original [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund.git))
    b. phidata
    c. llama-index
    d. autogen
    e. smolagents
```
simple result from smolagents(qwen2.5)

```bash
[Step 1: Duration 111.80 seconds| Input tokens: 2,052 | Output tokens: 997]
Reached max steps.
Final answer: Certainly! Here’s how we can propose and apply a simple trend-following strategy to NVIDIA stock prices using historical data.

### Trend-Following Strategy

1. **Moving Average Calculation**: We will calculate the moving average of the closing price over a specified window.
2. **Signal Generation**: If the current closing price is above the moving average, we generate a buy signal; if it’s below, we generate a sell signal.

### Example Implementation in Python

First, let's define the necessary functions and then apply them to sample data or real historical stock prices for NVIDIA (NVDA).

```python
import pandas as pd

# Sample dummy data for demonstration purposes
data = {
    'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'Close': [45.2, 46.0, 47.1, 48.2, 49.3, 50.0, 51.1, 52.2, 53.3, 54.4,
              55.5, 56.6, 57.7, 58.8, 60.0, 61.2, 62.4, 63.6, 64.8, 66.0,
              67.2, 68.4, 69.6, 70.8, 72.0, 73.2, 74.4, 75.6, 76.8]
}

nvidia_prices = pd.DataFrame(data)
nvidia_prices.set_index('Date', inplace=True)

def moving_average(data, window):
    return data['Close'].rolling(window=window).mean()

def calculate_trend_following_strategy(prices, ma_window=20):
    """
    Calculate a simple trend-following strategy based on a moving average.
    
    :param prices: DataFrame with 'Date' and 'Close' columns
    :param ma_window: Window for the moving average calculation
    :return: A DataFrame with buy/sell signals ('Strategy')
    """
    # Calculate the moving average
    ma = moving_average(prices, ma_window)
    
    # Create a strategy column to indicate when to buy or sell
    prices['Strategy'] = 0
    
    # Generate buy signal
    prices.loc[prices['Close'] > ma, 'Strategy'] = 1
    
    # Generate sell signal
    prices.loc[prices['Close'] < ma, 'Strategy'] = -1
    
    return prices

# Apply the strategy to the sample data
nvidia_prices_with_strategy = calculate_trend_following_strategy(nvidia_prices)
print(nvidia_prices_with_strategy[['Close', 'Strategy']])

Explanation:

- **Data Preparation**: We created a DataFrame with dummy closing price data for NVIDIA. In practice, you would replace this with actual historical stock prices.
- **Moving Average Calculation**: The `moving_average` function calculates the moving average of the closing prices over a specified window (`ma_window`).
- **Signal Generation**: The `calculate_trend_following_strategy` function generates buy or sell signals based on whether the current closing price is above or below the moving average.

### Output:

The output DataFrame will include columns for the closing prices and strategy signals. A value of 1 in the 'Strategy' column indicates a buy signal, while -1 indicates a sell signal.

If you have access to real historical stock data, simply replace the dummy data with your dataset and run the above code. This will give you practical buy/sell signals based on the moving average 
strategy for NVIDIA (NVDA) or any other stock of interest. 

Would you like to proceed with this example using a more detailed dataset? If so, please provide the historical stock prices, and I can help you further! 🚀🚀🚀
[Step 2: Duration 0.00 seconds| Input tokens: 4,071 | Output tokens: 1,823]
Certainly! Here’s how we can propose and apply a simple trend-following strategy to NVIDIA stock prices using historical data.

### Trend-Following Strategy

1. **Moving Average Calculation**: We will calculate the moving average of the closing price over a specified window.
2. **Signal Generation**: If the current closing price is above the moving average, we generate a buy signal; if it’s below, we generate a sell signal.

### Example Implementation in Python

First, let's define the necessary functions and then apply them to sample data or real historical stock prices for NVIDIA (NVDA).

import pandas as pd

# Sample dummy data for demonstration purposes
data = {
    'Date': pd.date_range(start='2023-01-01', periods=30, freq='D'),
    'Close': [45.2, 46.0, 47.1, 48.2, 49.3, 50.0, 51.1, 52.2, 53.3, 54.4,
              55.5, 56.6, 57.7, 58.8, 60.0, 61.2, 62.4, 63.6, 64.8, 66.0,
              67.2, 68.4, 69.6, 70.8, 72.0, 73.2, 74.4, 75.6, 76.8]
}

nvidia_prices = pd.DataFrame(data)
nvidia_prices.set_index('Date', inplace=True)

def moving_average(data, window):
    return data['Close'].rolling(window=window).mean()

def calculate_trend_following_strategy(prices, ma_window=20):
    """
    Calculate a simple trend-following strategy based on a moving average.
    
    :param prices: DataFrame with 'Date' and 'Close' columns
    :param ma_window: Window for the moving average calculation
    :return: A DataFrame with buy/sell signals ('Strategy')
    """
    # Calculate the moving average
    ma = moving_average(prices, ma_window)
    
    # Create a strategy column to indicate when to buy or sell
    prices['Strategy'] = 0
    
    # Generate buy signal
    prices.loc[prices['Close'] > ma, 'Strategy'] = 1
    
    # Generate sell signal
    prices.loc[prices['Close'] < ma, 'Strategy'] = -1
    
    return prices

# Apply the strategy to the sample data
nvidia_prices_with_strategy = calculate_trend_following_strategy(nvidia_prices)
print(nvidia_prices_with_strategy[['Close', 'Strategy']])

### Explanation:

- **Data Preparation**: We created a DataFrame with dummy closing price data for NVIDIA. In practice, you would replace this with actual historical stock prices.
- **Moving Average Calculation**: The `moving_average` function calculates the moving average of the closing prices over a specified window (`ma_window`).
- **Signal Generation**: The `calculate_trend_following_strategy` function generates buy or sell signals based on whether the current closing price is above or below the moving average.

### Output:

The output DataFrame will include columns for the closing prices and strategy signals. A value of 1 in the 'Strategy' column indicates a buy signal, while -1 indicates a sell signal.

If you have access to real historical stock data, simply replace the dummy data with your dataset and run the above code. This will give you practical buy/sell signals based on the moving average strategy for NVIDIA (NVDA) or any other stock of interest. 

Would you like to proceed with this example using a more detailed dataset? If so, please provide the historical stock prices, and I can help you further! 🚀🚀🚀
```

The system consists of the following collaborative agents:

1. **Market Data Analyst** - Responsible for collecting and preprocessing market data
2. **Valuation Agent** - Calculates the intrinsic value of stocks and generates trading signals
3. **Sentiment Agent** - Analyzes market sentiment and generates trading signals
4. **Fundamentals Agent** - Analyzes fundamental data and generates trading signals
5. **Technical Analyst** - Analyzes technical indicators and generates trading signals
6. **Risk Manager** - Calculates risk indicators and sets position limits
7. **Portfolio Manager** - Makes final trading decisions and generates orders


![Screenshot 2024-12-27 at 5 49 56 PM](https://github.com/user-attachments/assets/c281b8c3-d8e6-431e-a05e-d309d306e967)

**Note:** The system only simulates trading decisions and does not execute actual trades.

## Disclaimer

This project is for **educational and research purposes only**.

- Not suitable for actual trading or investment
- No guarantees provided
- Past performance does not indicate future results
- Creators are not liable for any financial losses
- Consult a professional financial advisor for investment decisions

By using this software, you agree to use it solely for learning purposes.


## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
  - [Running the model](#running-the-model)
  - [Running the Backtester](#running-the-backtester)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Setup

Clone the repository:

```bash
git clone https://github.com/24mlight/A_Share_investent_Agent.git
cd A_Share_investent_Agent
```

1. Install Poetry (if not already installed):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
if use zsh
```bash
export PATH="$HOME/.local/bin:$PATH"
```

2. Install dependencies:

```bash
poetry install
```

3. Set up your environment variables:

```bash
# Create .env file for your API keys
cp .env.example .env

# Get your Gemini API key from https://aistudio.google.com/
GEMINI_API_KEY='your-gemini-api-key-here'
GEMINI_MODEL='gemini-1.5-flash'
```

## Usage

### Running

The system supports multiple ways to run and allows combining different parameters as needed:

1. **Basic Run**

```bash
poetry run python src/main.py --ticker 301155
```

This will run the system with default parameters, including:

- Analyze 5 news articles by default (num_of_news=5)
- Do not display detailed analysis process (show_reasoning=False)
- Use default initial capital (initial_capital=100,000)

2. **Display Analysis Reasoning Process**

```bash
poetry run python src/main.py --ticker 301155 --show-reasoning
```

This will display the analysis process and reasoning results of each agent (Market Data Agent, Technical Analyst, Fundamentals Agent, Sentiment Agent, Risk Manager, Portfolio Manager).

Set Initial Capital：

- initial_capital: Initial cash amount (optional, default is 100,000)

4. **Customize Number of News Articles and Specific Date Investment Advice**

```bash
poetry run python src/main.py --ticker 301157 --show-reasoning --end-date 2024-12-11 --num-of-news 20
```

This will:

- Analyze the latest 20 news articles within the specified date range for sentiment analysis
- start-date and end-date format: YYYY-MM-DD

5. **Backtesting Functionality**

```bash
poetry run python src/backtester.py --ticker 301157 --start-date 2024-12-11 --end-date 2025-01-07 --num-of-news 20
```

The backtesting functionality supports the following parameters:

- ticker: Stock code
- start-date: Backtest start date (YYYY-MM-DD)
- end-date: Backtest end date (YYYY-MM-DD)
- initial-capital: Initial capital (optional, default is 100,000)
- num-of-news: Number of news articles used for sentiment analysis (optional, default is 5, maximum is 100)

### Parameter Description

- --ticker: Stock code (required)
- --show-reasoning: Display analysis reasoning process (optional, default is false)
- --initial-capital: Initial cash amount (optional, default is 100,000)
- --num-of-news: Number of news articles used for sentiment analysis (optional, default is 5, maximum is 100)
- --start-date: Start date, format YYYY-MM-DD (optional)
- --end-date: End date, format YYYY-MM-DD (optional)

Output Description
The system will output the following information:

1. Fundamental analysis results
2. Valuation analysis results
3. Technical analysis results
4. Sentiment analysis results
5. Risk management assessment
6. Final trading decision

**Example Output:**

```
Final Result:
{
  "action": "buy",
  "quantity": 12500,
  "confidence": 0.42,
  "agent_signals": [
    {
      "agent": "Technical Analysis",
      "signal": "bullish",
      "confidence": 0.6
    },
    {
      "agent": "Fundamental Analysis",
      "signal": "neutral",
      "confidence": 0.5
    },
    {
      "agent": "Sentiment Analysis",
      "signal": "neutral",
      "confidence": 0.8
    },
    {
      "agent": "Valuation Analysis",
      "signal": "bearish",
      "confidence": 0.99
    },
    {
      "agent": "Risk Management",
      "signal": "buy",
      "confidence": 1.0
    }
  ],
  "reasoning": "Risk Management allows a buy action with a maximum quantity of 12500..."
}
```

## Project Structure



## Acknowledgments
This project is adapted from [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund.git). We sincerely thank the original authors for their excellent work and inspiration. The original project provided a solid foundation for our adaptations and improvements tailored to the A-share market.
please refer to [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund.git) to check the strategy and agent function.