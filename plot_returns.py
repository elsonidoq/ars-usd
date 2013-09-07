#!/usr/bin/env python
import load_data, plots
import pandas as pd
from matplotlib import pyplot as plt


data= load_data.load_data()


df = pd.DataFrame(data)

serie = df['usd-bna/buy']


for i in [5, 30, 360]:
    f, (ax1, ax2) = plt.subplots(2)
    ax1.hist((serie/serie.shift(i)).dropna(), bins=50)
    ax1.set_title('cada %d dias' % i)
    ax2.plot((serie/serie.shift(i)).dropna())
    ax2.set_title('cada %d dias' % i)
    #f.savefig('plot-%d.pdf' % i, format = 'pdf')