#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
from pprint import pprint

# ------------------------------------------------------------------
# 1. Financial Statements (Annual)
# ------------------------------------------------------------------
def get_financial_statements(symbol: str) -> Dict[str, Dict[str, float]]:
    """
    Retrieve the latest and previous period data from the
    annual balance sheet, income statement, and cash flow using yfinance.

    Returns:
        A dictionary with two keys:
            {
                "latest_item": {...},
                "previous_item": {...}
            }
        Each item is a dict containing fields like:
            - net_income
            - operating_revenue
            - operating_profit
            - working_capital
            - depreciation_and_amortization
            - capital_expenditure
            - free_cash_flow
    """
    try:
        print(f"\nFetching financial statements for {symbol} via yfinance...")

        ticker = yf.Ticker(symbol)
        balance_sheet = ticker.balance_sheet      # annual balance sheet
        income_statement = ticker.financials      # annual income statement
        cash_flow = ticker.cashflow              # annual cash flow

        # If any of these DataFrames are None or empty, we can't proceed
        if (balance_sheet is None or balance_sheet.empty or
            income_statement is None or income_statement.empty or
            cash_flow is None or cash_flow.empty):
            print("WARNING: One or more financial statements are missing/empty.")
            return {"latest_item": {}, "previous_item": {}}

        # yfinance returns wide DataFrames where columns are dates, rows are items.
        # For example, income_statement might have:
        #   columns = [2022-09-24, 2021-09-25], rows = ["Net Income", "Total Revenue", ...]
        # We transpose so each row becomes one period, each column becomes an item.
        bs_t = balance_sheet.transpose()
        is_t = income_statement.transpose()
        cf_t = cash_flow.transpose()

        # We assume the last row is the “latest” and the second-last is the “previous”.
        if len(bs_t) < 2 or len(is_t) < 2 or len(cf_t) < 2:
            print("WARNING: Not enough historical periods to form latest & previous.")
            return {"latest_item": {}, "previous_item": {}}

        # Identify the row index for latest & previous
        latest_bs_idx = bs_t.index[-1]
        prev_bs_idx = bs_t.index[-2]

        latest_is_idx = is_t.index[-1]
        prev_is_idx = is_t.index[-2]

        latest_cf_idx = cf_t.index[-1]
        prev_cf_idx = cf_t.index[-2]

        # Extract Series for each statement
        latest_balance = bs_t.loc[latest_bs_idx]
        previous_balance = bs_t.loc[prev_bs_idx]

        latest_income = is_t.loc[latest_is_idx]
        previous_income = is_t.loc[prev_is_idx]

        latest_cash_flow = cf_t.loc[latest_cf_idx]
        previous_cash_flow = cf_t.loc[prev_cf_idx]

        def safe_get(series: pd.Series, item: str) -> float:
            """Safely get a float value from the Series by 'item' key."""
            if item in series:
                return float(series[item])
            return 0.0

        # Build the “latest_item”
        latest_item = {
            "net_income": safe_get(latest_income, "Net Income"),
            "operating_revenue": safe_get(latest_income, "Total Revenue"),
            "operating_profit": safe_get(latest_income, "Operating Income"),
            "working_capital": (
                safe_get(latest_balance, "Total Current Assets")
                - safe_get(latest_balance, "Total Current Liabilities")
            ),
            "depreciation_and_amortization": safe_get(latest_cash_flow, "Depreciation"),
            "capital_expenditure": abs(safe_get(latest_cash_flow, "Capital Expenditures")),
            "free_cash_flow": (
                safe_get(latest_cash_flow, "Total Cash From Operating Activities")
                + safe_get(latest_cash_flow, "Capital Expenditures")  # typically negative
            )
        }

        # Build the “previous_item”
        previous_item = {
            "net_income": safe_get(previous_income, "Net Income"),
            "operating_revenue": safe_get(previous_income, "Total Revenue"),
            "operating_profit": safe_get(previous_income, "Operating Income"),
            "working_capital": (
                safe_get(previous_balance, "Total Current Assets")
                - safe_get(previous_balance, "Total Current Liabilities")
            ),
            "depreciation_and_amortization": safe_get(previous_cash_flow, "Depreciation"),
            "capital_expenditure": abs(safe_get(previous_cash_flow, "Capital Expenditures")),
            "free_cash_flow": (
                safe_get(previous_cash_flow, "Total Cash From Operating Activities")
                + safe_get(previous_cash_flow, "Capital Expenditures")
            )
        }

        print("Successfully processed latest & previous period data.")
        return {
            "latest_item": latest_item,
            "previous_item": previous_item
        }

    except Exception as e:
        print(f"Error retrieving financial statements for {symbol}: {e}")
        return {"latest_item": {}, "previous_item": {}}


# ------------------------------------------------------------------
# 2. Market Data
# ------------------------------------------------------------------
def get_market_data(symbol: str) -> Dict[str, Any]:
    """
    Retrieve basic market data for a given stock symbol using yfinance.
    Returns fields like market cap, volume, average volume, 52-week high/low, etc.
    """
    try:
        print(f"\nFetching market data for {symbol} via yfinance...")
        ticker = yf.Ticker(symbol)
        info = ticker.info

        market_cap = info.get("marketCap", 0)
        volume = info.get("volume", 0)
        avg_volume = info.get("averageVolume", 0)
        fifty_two_week_high = info.get("fiftyTwoWeekHigh", 0)
        fifty_two_week_low = info.get("fiftyTwoWeekLow", 0)

        data = {
            "market_cap": market_cap,
            "volume": volume,
            "average_volume": avg_volume,
            "fifty_two_week_high": fifty_two_week_high,
            "fifty_two_week_low": fifty_two_week_low
        }
        print("Successfully retrieved market data.")
        return data

    except Exception as e:
        print(f"Error retrieving market data for {symbol}: {e}")
        return {}


# ------------------------------------------------------------------
# 3. Financial Metrics (like P/E, ROE, margins)
# ------------------------------------------------------------------
def get_financial_metrics(symbol: str) -> Dict[str, Any]:
    """
    Retrieve approximate financial metrics using yfinance's 'info' dictionary.
    Returns a dictionary with P/E, P/B, ROE, margins, etc.
    """
    try:
        print(f"\nFetching financial metrics for {symbol} using yfinance...")
        ticker = yf.Ticker(symbol)
        info = ticker.info

        market_cap = info.get("marketCap", 0)
        trailing_pe = info.get("trailingPE", None)
        forward_pe = info.get("forwardPE", None)
        price_to_book = info.get("priceToBook", None)
        peg_ratio = info.get("pegRatio", None)
        return_on_equity = info.get("returnOnEquity", None)
        profit_margin = info.get("profitMargins", None)
        book_value = info.get("bookValue", None)
        # You may also retrieve: "revenue", "netIncomeToCommon", etc.

        metrics = {
            "market_cap": float(market_cap),
            "trailing_pe": trailing_pe,
            "forward_pe": forward_pe,
            "price_to_book": price_to_book,
            "peg_ratio": peg_ratio,
            "return_on_equity": return_on_equity,  # often 0.25 => 25%
            "profit_margin": profit_margin,        # e.g. 0.15 => 15%
            "book_value": book_value
        }

        print("Successfully retrieved financial metrics.")
        return metrics

    except Exception as e:
        print(f"Error retrieving financial metrics for {symbol}: {e}")
        return {}


# ------------------------------------------------------------------
# 4. Raw Financial Statements (Full DataFrames)
# ------------------------------------------------------------------
def get_financial_statements_raw(symbol: str) -> Dict[str, Any]:
    """
    Fetch the raw annual balance sheet, financials (income statement),
    and cash flow DataFrames from yfinance, as dictionaries.

    Returns:
        {
            "balance_sheet": { ... },
            "income_statement": { ... },
            "cash_flow": { ... }
        }
    """
    try:
        print(f"\nFetching raw financial statements for {symbol} via yfinance...")
        ticker = yf.Ticker(symbol)

        balance_sheet = ticker.balance_sheet
        income_statement = ticker.financials
        cash_flow = ticker.cashflow

        bs_dict = balance_sheet.to_dict("index") if isinstance(balance_sheet, pd.DataFrame) else {}
        is_dict = income_statement.to_dict("index") if isinstance(income_statement, pd.DataFrame) else {}
        cf_dict = cash_flow.to_dict("index") if isinstance(cash_flow, pd.DataFrame) else {}

        statements = {
            "balance_sheet": bs_dict,
            "income_statement": is_dict,
            "cash_flow": cf_dict
        }

        print("Successfully retrieved raw statements.")
        return statements

    except Exception as e:
        print(f"Error retrieving raw statements for {symbol}: {e}")
        return {}


# ------------------------------------------------------------------
# 5. Historical Price Data with Technical Indicators
# ------------------------------------------------------------------
def get_price_history(
    symbol: str,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
) -> pd.DataFrame:
    """
    Download historical price data for a given stock symbol using yfinance, then compute
    a variety of technical indicators (momentum, volatility, MACD, RSI, Bollinger, etc.).

    Returns a DataFrame with columns such as:
      - date, open, high, low, close, volume
      - momentum_1m, momentum_3m, momentum_6m
      - volume_momentum
      - historical_volatility, volatility_regime, volatility_z_score
      - atr_ratio
      - hurst_exponent, skewness, kurtosis
      - macd, macd_signal, macd_hist
      - rsi
      - bb_middle, bb_upper, bb_lower
    """
    try:
        # 1) Handle date defaults
        today = datetime.now().date()
        if not end_date:
            end_date = today.isoformat()
        if not start_date:
            end_dt = datetime.strptime(end_date, "%Y-%m-%d")
            start_dt = end_dt - timedelta(days=365)
            start_date = start_dt.strftime("%Y-%m-%d")

        print(f"\nFetching historical data for {symbol} via yfinance...")
        print(f"Start date: {start_date}, End date: {end_date}")

        # 2) Download data
        df = yf.download(symbol, start=start_date, end=end_date, progress=False)
        if df.empty:
            print(f"WARNING: No data retrieved for {symbol}.")
            return pd.DataFrame()

        df.rename(columns={
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Adj Close": "adj_close",
            "Volume": "volume"
        }, inplace=True)

        # Move date index into a column
        df.reset_index(inplace=True)
        df.rename(columns={"Date": "date"}, inplace=True)

        # Sort ascending
        df.sort_values("date", inplace=True)
        df.reset_index(drop=True, inplace=True)

        # If fewer than 120 rows, some long-term indicators won't be accurate
        if len(df) < 120:
            print(f"WARNING: Only {len(df)} rows. Some indicators (6m momentum, etc.) may be incomplete.")

        # 3) Compute Indicators

        # daily returns
        df["daily_returns"] = df["close"].pct_change()

        # Momentum
        df["momentum_1m"] = df["close"].pct_change(20)
        df["momentum_3m"] = df["close"].pct_change(60)
        df["momentum_6m"] = df["close"].pct_change(120)

        # Volume Momentum
        df["volume_ma20"] = df["volume"].rolling(20).mean()
        df["volume_momentum"] = df["volume"].squeeze() / df["volume_ma20"]

        # Historical Volatility
        df["historical_volatility"] = df["daily_returns"].rolling(20).std() * np.sqrt(252)

        # Volatility regime & z-score (120d)
        vol_120 = df["daily_returns"].rolling(120).std() * np.sqrt(252)
        vol_min = vol_120.rolling(120).min()
        vol_max = vol_120.rolling(120).max()
        vol_range = vol_max - vol_min
        df["volatility_regime"] = np.where(
            vol_range > 0,
            (df["historical_volatility"] - vol_min) / vol_range,
            0
        )
        vol_mean = df["historical_volatility"].rolling(120).mean()
        vol_std = df["historical_volatility"].rolling(120).std()
        df["volatility_z_score"] = (df["historical_volatility"] - vol_mean) / vol_std

        # ATR ratio (14-day)
        tr_df = pd.DataFrame()
        tr_df["h_l"] = df["high"] - df["low"]
        tr_df["h_pc"] = (df["high"] - df["close"].shift(1)).abs()
        tr_df["l_pc"] = (df["low"] - df["close"].shift(1)).abs()
        tr_df["tr"] = tr_df[["h_l", "h_pc", "l_pc"]].max(axis=1)
        df["atr"] = tr_df["tr"].rolling(14).mean()
        df["atr_ratio"] = df["atr"] / df["close"].squeeze() 

        # Hurst exponent, skewness, kurtosis
        def calculate_hurst(series: pd.Series) -> float:
            try:
                series = series.dropna()
                if len(series) < 30:
                    return np.nan
                log_rets = np.log(series / series.shift(1)).dropna()
                if len(log_rets) < 30:
                    return np.nan

                lags = range(2, min(11, len(log_rets)//4))
                tau = []
                for lag in lags:
                    std_vals = log_rets.rolling(lag).std().dropna()
                    if len(std_vals) > 0:
                        tau.append(std_vals.mean())
                if len(tau) < 3:
                    return np.nan

                lags_log = np.log(list(lags))
                tau_log = np.log(tau)
                reg = np.polyfit(lags_log, tau_log, 1)
                hurst_val = reg[0] / 2.0
                if np.isnan(hurst_val) or np.isinf(hurst_val):
                    return np.nan
                return hurst_val
            except:
                return np.nan

        log_price = np.log(df["close"] / df["close"].shift(1))
        df["hurst_exponent"] = log_price.rolling(120, min_periods=60).apply(calculate_hurst)
        df["skewness"] = df["daily_returns"].rolling(20).skew()
        df["kurtosis"] = df["daily_returns"].rolling(20).kurt()

        # MACD
        def ema(series: pd.Series, span: int) -> pd.Series:
            return series.ewm(span=span, adjust=False).mean()

        df["ema_12"] = ema(df["close"], 12)
        df["ema_26"] = ema(df["close"], 26)
        df["macd"] = df["ema_12"] - df["ema_26"]
        df["macd_signal"] = ema(df["macd"], 9)
        df["macd_hist"] = df["macd"] - df["macd_signal"]

        # RSI (14-day)
        df["change"] = df["close"].diff()
        df["gain"] = df["change"].mask(df["change"] < 0, 0)
        df["loss"] = -df["change"].mask(df["change"] > 0, 0)
        roll_gain = df["gain"].rolling(14, min_periods=14).mean()
        roll_loss = df["loss"].rolling(14, min_periods=14).mean()
        rs = roll_gain / roll_loss
        df["rsi"] = 100 - (100 / (1 + rs))

        # Bollinger Bands (20d ± 2std)
        period_bb = 20
        df["bb_middle"] = df["close"].rolling(period_bb).mean()
        rolling_std = df["close"].rolling(period_bb).std()
        df["bb_upper"] = df["bb_middle"] + 2.0 * rolling_std.squeeze() 
        df["bb_lower"] = df["bb_middle"] - 2.0 * rolling_std.squeeze() 

        print(f"Successfully retrieved {len(df)} rows for {symbol}.")
        nan_counts = df.isna().sum()
        if nan_counts.any():
            print("\nWARNING: The following columns have NaN values:")
            for col, cnt in nan_counts[nan_counts > 0].items():
                print(f"- {col}: {cnt}")

        return df

    except Exception as e:
        print(f"Error fetching historical price data for {symbol}: {e}")
        return pd.DataFrame()


# ------------------------------------------------------------------
# 6. Demo / Test
# ------------------------------------------------------------------
if __name__ == "__main__":
    test_symbol = "AAPL"  # Example: Apple Inc.

    # 1) Financial Statements
    statements = get_financial_statements(test_symbol)
    print("\n=== Latest Period ===")
    pprint(statements["latest_item"])
    print("\n=== Previous Period ===")
    pprint(statements["previous_item"])

    # 2) Market Data
    market_info = get_market_data(test_symbol)
    print("\n=== Market Data ===")
    pprint(market_info)

    # 3) Financial Metrics
    fin_metrics = get_financial_metrics(test_symbol)
    print("\n=== Financial Metrics ===")
    pprint(fin_metrics)

    # 4) Raw Statement Dictionaries
    raw_stmts = get_financial_statements_raw(test_symbol)
    print("\n=== Raw Financial Statements (short preview) ===")
    # for clarity, let's only preview keys
    print("Balance Sheet Keys:", list(raw_stmts["balance_sheet"].keys()))
    print("Income Statement Keys:", list(raw_stmts["income_statement"].keys()))
    print("Cash Flow Keys:", list(raw_stmts["cash_flow"].keys()))

    # 5) Historical Price Data + Indicators
    df_prices = get_price_history(test_symbol, "2023-01-01", "2023-07-01")
    print("\n=== Price History + Indicators (head) ===")
    print(df_prices.head(5))
    print("\n=== Price History + Indicators (tail) ===")
    print(df_prices.tail(5))
