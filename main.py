import numpy as np
import pandas as pd
import requests 
import xlsxwriter
import math
from trader import Trader
stocks = pd.read_csv('sp_500_stocks.csv')
symbol = 'AAPL'

def main():
    t = Trader()

    t.get_bar(symbol)





if __name__ == '__main__':
    main()

