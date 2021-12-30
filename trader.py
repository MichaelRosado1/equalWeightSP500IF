from secrets import API_KEY, SECRET_KEY
import alpaca_trade_api as tradeapi

class Trader:
    def __init__(self):
        self.__key_id = API_KEY
        self.__secret_key = SECRET_KEY
        self.__base_url = 'https://paper-api.alpaca.markets'



