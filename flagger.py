from subprocess import *
from yahoo_finance import *
from datetime import *

stocksToFollow = ["goog"]
while True:
    def timeStamp():
        today = datetime.today()
        timeStamp = []
        for attr in ["hour","minute","second","microsecond"] :
            timeStamp.append(getattr(today, attr))
        return timeStamp

    for stock in stocksToFollow:
        priceAtThisMoment = stock.get_historical()
        print timeStamp()
        print priceAtThisMoment 

        if priceAtThisMoment > 100:
            stockUpdate = "python gmailText.py -u hllbck7@gmail.com -p l0ll02012 -t 8642436724@att.net -s 'stock update' -m '" + stockName + ": " + priceAtThisMoment + "'"
            subprocess.call(stockUpdate, shell=True)
