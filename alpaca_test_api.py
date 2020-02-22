import alpaca_trade_api as alpaca
import threading
import time
import datetime

from secrets import API_KEY
from secrets import API_SECRET

APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

tradeapi = alpaca.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, api_version='v2') # or use ENV Vars shown below
account = tradeapi.get_account()
tradeapi.list_positions()

is_open = "is" if tradeapi.get_clock().is_open else "is not" 

print("Market", is_open,"open")
