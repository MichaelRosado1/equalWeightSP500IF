import numpy as np
import pandas as pd
import requests 
import xlsxwriter
import math
import os
from dotenv import load_dotenv
load_dotenv()

from secrets import IEX_CLOUD_API_TOKEN

stocks = pd.read_csv('sp_500_stocks.csv')
symbol = 'AAPL'


class Trader:
    def __init__(self, symbol):
