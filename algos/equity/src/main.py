
import os
import pyotp
import time

import robin_stocks as r

from prometheus_client import start_http_server, Gauge

robinhood = r.robinhood

class Equity:

    def __init__(self, _ticker, _delay = 30):
        self.ticker = _ticker
        self.delay = _delay
        self.access_token = "null"
        self.CurrentPrice = Gauge('equity_price_current', 'Current Price of the Equity',labelnames=['symbol'])

    def isLoggedIn(self):
        if self.access_token == "null":
            self.access_token = robinhood.login(os.environ['ROBINHOOD_USERNAME'],os.environ['ROBINHOOD_PASSWORD'], mfa_code=pyotp.TOTP(os.environ['ROBINHOOD_OTP']).now())['access_token']

            if self.access_token == "":
                print("Loggin Failed")
                return False
            else:
                return True
        else:
            return True
        
    def current_price(self):
        if self.isLoggedIn():
           return robinhood.stocks.get_latest_price(self.ticker)[0]
        
    def run(self):
        while True:
            self.CurrentPrice.labels(symbol=self.ticker).set(self.current_price())
            time.sleep(self.delay)

start_http_server(9200)
Equity(os.environ['TICKER']).run()