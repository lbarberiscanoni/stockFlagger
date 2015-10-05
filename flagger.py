import subprocess
from googlefinance import *
from datetime import *

stocksToFollow = {"FNMA": 2.31, "FB": 92, "AAPL": 110}
while True:
    timestamp = str(datetime.today()).split()[1]
    print timestamp
    for stock in stocksToFollow:
        priceTarget = stocksToFollow[stock]
        priceAtThisMoment = getQuotes(stock)[0]["LastTradePrice"]
        print stock + ": " + priceAtThisMoment 

        if priceAtThisMoment == priceTarget:
            stockUpdate = "python gmailText.py -u hllbck7@gmail.com -p l0ll02012 -t 8642436724@text.att.net -b '" + stock + " is at " + priceAtThisMoment + "'"
            subprocess.call(stockUpdate, shell=True)
    print "-------------------------------"
