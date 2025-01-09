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

```
stockseek/
├── src/                         # Source code directory
│   ├── agents/                  # Agent definitions and workflows
│   │   ├── fundamentals.py      # Fundamentals Agent
│   │   ├── market_data.py       # Market Data Agent
│   │   ├── portfolio_manager.py # Portfolio Manager
│   │   ├── risk_manager.py      # Risk Manager
│   │   ├── sentiment.py         # Sentiment Agent
│   │   ├── state.py             # Agent State Management
│   │   ├── technicals.py        # Technical Analyst
│   │   └── valuation.py         # Valuation Agent
│   ├── data/                    # Data storage directory
│   │   ├── sentiment_cache.json # Sentiment analysis cache
│   │   └── stock_news/          # Stock news data
│   ├── tools/                   # Tools and utility modules
│   │   ├── api.py               # API interfaces and data fetching
│   │   ├── data_analyzer.py     # Data analysis tools
│   │   ├── news_crawler.py      # News crawling tools
│   │   ├── openrouter_config.py # OpenRouter configuration
│   │   └── test_*.py            # Test files
│   ├── utils/                   # General utility functions
│   ├── backtester.py            # Backtesting system
│   └── main.py                  # Main program entry
├── .env                         # Environment variable configuration
├── .env.example                 # Environment variable example
├── poetry.lock                  # Poetry dependency lock file
├── pyproject.toml               # Poetry project configuration
└── README.md                    # Project documentation
```

## Acknowledgments
This project is adapted from [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund.git). We sincerely thank the original authors for their excellent work and inspiration. The original project provided a solid foundation for our adaptations and improvements tailored to the A-share market.


### Data Flow Process
Data Collection Phase

- Market Data Agent fetches real-time market data through the akshare API:
    - Real-time stock quotes (stock_zh_a_spot_em)
    - Historical market data (stock_zh_a_hist)
    - Financial metrics data (stock_financial_analysis_indicator)
    - Financial statement data (stock_financial_report_sina)
- News data is fetched through the Sina Finance API
- All data undergoes standardization and formatting
Analysis Phase

#### Technical Analyst:

    Calculates technical indicators (momentum, trends, volatility, etc.)
    Analyzes price patterns and trading signals
    Generates technical analysis scores and recommendations
    Fundamentals Analyst:

    Analyzes financial statement data
    Evaluates the company's fundamental status
    Generates fundamental analysis scores
    Sentiment Analyst:

    Analyzes the latest market news
    Uses AI models to assess news sentiment
    Generates market sentiment scores
    Valuation Analyst:

    Calculates valuation metrics
    Conducts Discounted Cash Flow (DCF) valuation analysis
    Assess the intrinsic value of stocks
    Risk Assessment Phase

#### Risk Manager considers multiple dimensions:

    Market risk assessment (volatility, Beta, etc.)
    Position size limit calculations
    Setting stop-loss and take-profit levels
    Portfolio risk control
    Decision Phase

#### Portfolio Manager makes decisions based on:

    Signal strength and confidence from each agent
    Current market conditions and risk levels
    Portfolio status and cash levels
    Consideration of trading costs and liquidity
    Data Storage and Caching

    Sentiment analysis results are cached in data/sentiment_cache.json
    News data is stored in the data/stock_news/ directory
    Log files are stored by type in the logs/ directory
    API call records are written to logs in real-time
    Monitoring and Feedback


    All agents share the same state object (AgentState)
    Communication is done through a message-passing mechanism
    Each agent can access necessary historical data
    Decision Weights

    Portfolio Manager considers different signal weights when making decisions:

    Valuation Analysis: 35%
    Fundamental Analysis: 30%
    Technical Analysis: 25%
    Sentiment Analysis: 10%
    Risk Control

    Mandatory risk limits
    Maximum position limits
    Trading size restrictions
    Stop-loss and take-profit settings
    System Features
    Modular Design

    Each agent is an independent module
    Easy to maintain and upgrade
    Can be individually tested and optimized
    Scalability

    Easily add new analysts
    Support adding new data sources
    Expand decision-making strategies
#### Risk Management

    Multi-layered risk control
    Real-time risk assessment
    Automatic stop-loss mechanisms
    Intelligent Decision-Making

    Based on multi-dimensional analysis
    Considers multiple market factors
    Dynamically adjusts strategies
    Future Prospects
    Data Source Expansion

    Add more A-share data sources
    Integrate more financial data platforms
    Include social media sentiment data
    Expand to Hong Kong and US stock markets
    Function Enhancements

    Add more technical indicators
    Implement automated backtesting
    Support multi-stock portfolio management
    Performance Optimization

    Improve data processing efficiency
    Optimize decision algorithms
    Increase parallel processing capabilities
    Sentiment Analysis Feature
    The Sentiment Analysis Agent is one of the key components of the system, responsible for analyzing the potential impact of market news and public opinion on stocks.

#### Automatically crawls the latest stock-related news
    Supports multiple news sources
    Real-time news data updates
    Sentiment Analysis Processing

    Uses advanced AI models to analyze news sentiment
    Sentiment score range: -1 (extremely negative) to 1 (extremely positive)
    Considers the importance and timeliness of news
    Trading Signal Generation

    Generates trading signals based on sentiment analysis results
    - Includes signal type (bullish/bearish)
    - Provides confidence level assessment
    - Accompanied by detailed analysis reasoning

#### Sentiment Score Description
    - 1.0: Extremely Positive (Significant favorable news, unexpected performance, industry policy support)
    - 0.5 to 0.9: Positive (Revenue growth, new projects launched, received orders)
    - 0.1 to 0.4: Slightly Positive (Small contracts signed, normal daily operations)
    - 0.0: Neutral (Daily announcements, personnel changes, news with no significant impact)
    - -0.1 to -0.4: Slightly Negative (Minor lawsuits, losses in non-core business)
    - -0.5 to -0.9: Negative (Performance decline, loss of key customers, tightening industry policies)
    - =1.0: Extremely Negative (Major violations, severe losses in core business, regulatory penalties)