#This code takes in the world record for the 100m sprint and predicts
#what the record will be in the future


import matplotlib.pyplot as plt
import numpy as np

#got these times from the internet
#could be much more comprehensive using a complete csv file
years = [1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984,]
times = [221280994, 159978870, 106260000,181379640, 212222025, 359197037,252583617,234760478]

#gets a plot

#works out the trendline
z = np.polyfit(years, times, 1)
f = np.poly1d(z)

slope = z[0]
y_intercept = z[1]

#uses the model to predict the future time + speed
year_predict = int(input("What year would you like to predict: "))
time_predict = slope*year_predict + y_intercept #y = mx+ C
speed_predict = round(100/time_predict,3)

#gives info to the user
print("In year",year_predict,"expected gross of top film",str(round(time_predict,3))+"s")
print("This represents an increase", str(speed_predict)+"m/s")

#plots the trendline and shows the graph
plt.plot(years,times, "gs-")
plt.plot(years,f(years),"r--")
plt.show()

