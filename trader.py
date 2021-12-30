from secrets import API_KEY, SECRET_KEY
import alpaca_trade_api as tradeapi

class Trader:
    def __init__(self):
        #api credentials
        self.__key_id = API_KEY
        self.__secret_key = SECRET_KEY

        #base trading url
        self.__base_url = 'https://paper-api.alpaca.markets'

        #api connection
        self.__api = tradeapi.REST(
            self.__key_id,
            self.__secret_key,
            self.__base_url
        )

    def get_last_quote(self, symbol):
        last_quote = self.__api.get_last_quote(symbol)
        print(last_quote)




