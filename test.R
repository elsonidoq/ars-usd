library(forecast)
df=read.csv('all_data.csv',header=T,sep=',')
a=auto.arima(log(df[df$id==4,]$val))
fo= forecast(a)
fo$x= ts(fo$x[2650:length(fo$x)], frequency=1)
fo$mean=ts(fo$mean[1:length(fo$mean)],frequency=1, start=length(fo$x))
plot(fo)



