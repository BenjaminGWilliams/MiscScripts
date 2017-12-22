import requests
import json

url = 'https://min-api.cryptocompare.com/data/pricemultifull'
params = dict(fsyms='BTC,ETH,DASH,GVT',tsyms='BTC,USD,NZD')
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

for coin,price in sorted(data['RAW'].items()):
    string = ""
    for currency,value in price.items():
        string += "{}\t{:10.4f}\t".format(currency,value['PRICE'])
    print("Coin:{}\tPrice: {}".format(coin,string))
