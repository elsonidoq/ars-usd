from time import sleep
from datetime import timedelta
import json
import os
from datetime import datetime
import urllib, httplib, urllib
from dateutil import parser
from lxml.html import document_fromstring

def get_data(date):
    params='hidSubmit=S&hidFecha=%s&hidFeriados=&hidMonedas=&cmbMonedas=0&butBuscar=Submit'
    date= urllib.quote_plus(date)
    params%= date

    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain",
            'Host': 'www.bna.com.ar',
            'Connection': 'keep-alive',
            'Content-Length': '88',
            'Cache-Control': 'max-age=0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Origin': 'http://www.bna.com.ar',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.65 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'http://www.bna.com.ar/bp/bp_cotizaciones_historico.asp',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Cookie': 'ASPSESSIONIDQQSTDSRT=MNDCMEFAHEGMKGMFFKLBNDND; __utma=46687092.468978546.1377789204.1377789204.1378399458.2; __utmc=46687092; __utmz=46687092.1377789204.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=http://www.bna.com.ar/'
                   
               }
    conn = httplib.HTTPConnection("www.bna.com.ar")
    conn.request("POST", "/bp/bp_cotizaciones_historico.asp", params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()

    
    return data


def parse(data):
    dom= document_fromstring(data)

    l= dom.cssselect('.renglones')
    res= {}
    for e in l:
        curr, sell, buy, date= [e.text_content() for e in e.cssselect('div div')]
        res[curr]= dict(sell=float(sell), buy=float(buy), date=date)#parser.parse(date).date())
    return res

def download_data():
    d= datetime.now().date()

    while True:
        str_d= d.strftime('%d/%m/%Y')    
        print str_d
        fname= 'data/' + d.strftime('%d_%m_%Y.json')    
        if os.path.exists(fname): 
            d= d - timedelta(days=1)
            continue
        for i in xrange(3):
            try:
                pd= parse(get_data(str_d))
                break
            except Exception, e:
                print "ERROR"
                print e
                sleep(1)
        else:
            continue
            
        with open(fname,'w') as f: 
            json.dump(pd,f)

        d= d - timedelta(days=1)

if __name__ == '__main__': download_data()
