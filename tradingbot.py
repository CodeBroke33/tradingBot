from lumibot.brokers import Alpaca
from lumibot.backtesting import YahoodataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime

API_KEY = "PK58SMNRXQUVZWVYVGB2"
API_SECRET = "TbB2nHS8bAaoNm1ZKH3fjhz1n4HcnA2rzTFk0QqL"
BASE_URL = "https://paper-api.alpaca.markets"

ALPACA_CREDS = {
    "API_KEY":API_KEY,
    "API_SECRET": API_SECRET,  
    "PAPER": True 
}

class MLTrader(Strategy):
    def initialize(self, ):
        pass
    def on_trading_iteration(self)
            pass

start_date = datetime(2024,2,15)
end_date = datetime(2024,3,31)
broker = Alpaca(ALPACA_CREDS)
Strategy = MLTrader(name='mlstrat', broker=broker, 
                   parameters={})
    
    strategy.backtesting(
         YahoodataBacktesting,
         start_date,
         end_date,
         parameters={} 
    )