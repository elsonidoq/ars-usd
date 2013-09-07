import os
import json
from collections import defaultdict
from dateutil import parser

def load_data(dir):
    """
    devuelve la data en un diccionario con este formato

    d[currency/(buy|sell)] -> time series
    donde time series es un diccionario de fecha en valor

    """
    curr_mappings= {'Dolar U.S.A':'usd', 'Euro':'euro'}

    d= defaultdict(dict)
    for fname in os.listdir(dir):

        fname= os.path.join(dir, fname)
        data= json.load(open(fname))

        for currency, currency_data in data.iteritems():
            date= parser.parse(currency_data['date']) # deberia estar arriba
            for action in 'buy sell'.split():
                k='%s/%s' % (curr_mappings[currency],action) 
                d[k][date]= currency_data[action]
    
    # le saco el defaultdict para evitar errores
    return dict(d)
