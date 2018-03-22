
import json
import urllib2

class btcVeriAl():
    
    def __init__(self):
       print 'veriler aliniyor'
        
    def DegerDondur(self):
        req  = urllib2.Request('https://blockchain.info/charts/market-price?timespan=30days&format=json')
        opener = urllib2.build_opener()
        f = opener.open(req)
        jsonCikti = json.loads(f.read())
        degerler = []
        btc_value = []
        for item in  jsonCikti['values']:
            degerler.append(item)

        for a in degerler:
          btc_value.append(a['y'])


        return btc_value      