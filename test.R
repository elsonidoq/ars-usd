library(forecast)
df=read.csv('all_data.csv',header=T,sep=',')
a=auto.arima(log(df[df$id==4,]$val))
fo= forecast(a)
fo$x= ts(fo$x[2650:length(fo$x)], frequency=1)
fo$mean=ts(fo$mean[1:length(fo$mean)],frequency=1, start=length(fo$x))
plot(fo)

dates= df[df$id==4,]$date
today= as.Date(dates[length(dates)])

for(i in 1:length(fo$mean)) {
    min_val= exp(fo$lower[i])
    max_val= exp(fo$upper[i])
    the_day= as.Date(today)+i
    mean= exp(fo$mean[i])
    print(the_day)
    cat('\t', ' el dolar va a estar entre ', min_val,  ' y ', max_val, '(',mean,')\n')
}



