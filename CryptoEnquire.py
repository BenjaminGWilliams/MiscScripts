import requests
import json

url = 'https://min-api.cryptocompare.com/data/pricemulti'
params = dict(fsyms='BTC,ETH,DASH,GVT',tsyms='BTC,USD,NZD')    
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

for coin,price in sorted(data.iteritems()):
    string = ""
    for currency,value in price.iteritems():
        string += "{}\t{:10.4f}\t".format(currency,value)
    print "Coin:{}\tPrice: {}".format(coin,string)
