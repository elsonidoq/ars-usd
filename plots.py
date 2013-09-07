from pylab import *

def plot_data(data):
    figure()
    for k, v in data.iteritems():
        x,y= zip(*sorted(v.items()))
        plot(x,y,label=k,alpha=0.8)
    grid()
    legend(loc='best')
        

