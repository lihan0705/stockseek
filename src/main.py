# main.py
from src.agents.market_data_agent import create_market_data_agent
from smolagents import LiteLLMModel
def main():
    # 1) 创建我们的 agent
    # model_id = "meta-llama/Llama-2-7b-chat-hf"  # 仅作示例
    market_data_agent = create_market_data_agent()

    # 2) 提问: 让 agent 说明 AAPL 的市场数据
    question = "Please retrieve price history for AAPL from 2023-01-01 to 2023-07-01, then also get me its financial metrics and market data."

    # 3) 让 agent 来回答
    answer = market_data_agent.run(question)

    print("\n=== FINAL ANSWER ===")
    print(answer)

if __name__ == "__main__":
    main()
