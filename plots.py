from pylab import *

def plot_data(data):
    figure()
    for k, v in data.iteritems():
        x,y= zip(*sorted(v.items()))
        plot(x,y,'-o',label=k,alpha=0.8,markersize=3)
    grid()
    legend(loc='best')
        

