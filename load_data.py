import csv
from datetime import datetime
import os
import json
from collections import defaultdict
from dateutil import parser

def load_data_bna(dir):
    """
    devuelve la data en un diccionario con este formato

    d[currency/(buy|sell)] -> time series
    donde time series es un diccionario de fecha en valor

    """
    curr_mappings= {'Dolar U.S.A':'usd-bna', 'Euro':'euro-bna'}

    d= defaultdict(dict)
    for fname in os.listdir(dir):

        fname= os.path.join(dir, fname)
        data= json.load(open(fname))

        for currency, currency_data in data.iteritems():
            date= datetime.strptime(currency_data['date'], '%d/%m/%Y') # deberia estar arriba
            if date >= datetime.now(): import ipdb;ipdb.set_trace()
            for action in 'buy sell'.split():
                # ignoro euros por ahora
                if curr_mappings[currency] == 'euro-bna': continue
                k='%s/%s' % (curr_mappings[currency],action) 
                d[k][date]= currency_data[action]
    
    # le saco el defaultdict para evitar errores
    return dict(d)

def load_data_lanacion(fname):
    mapping= {'Informal (Blue)':'usd-blue-lanacion',
              'Oficial':'usd-oficial-lanacion'}
    reader= csv.reader(open(fname))
    reader.next() # header
    res= defaultdict(dict)
    for line in reader:
        date, ammount, type= line
        ammount= float(ammount.replace(',','.'))
        date= datetime.strptime(date.split()[0], '%d/%m/%Y')
        res[mapping[type]][date]= ammount
    return dict(res)

def load_data_valordolarblue(fname):
    mapping= {'oficial_venta':'usd-oficial-valordolarblue',
              'blue_venta':'usd-blue-valordolarblue'}
    res= defaultdict(dict)
    for doc in json.load(open(fname)):
        date= doc['fecha']
        date= datetime.strptime(date, '%Y-%m-%d')
        for k, v in mapping.iteritems():
            res[v][date]= doc[k]
    return dict(res)

    

def load_data():
    d= load_data_bna('data')
    d.update(load_data_lanacion('data_lanacion.csv'))
    d.update(load_data_valordolarblue('data_valordolarblue.com.ar.json'))
    return d




