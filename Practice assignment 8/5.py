import matplotlib.pyplot as plt

import pandas as pd

df=pd.read_csv("E:\TYBCS\Python\College\Practice assignment 8\Min_Max_Seasonal_IMD_2017.csv")

# print(df)

x=df['ANNUAL - MAX']
y=df['JAN-FEB - MIN']
z=df['JAN-FEB - MAX']

plt.hist(x,edgecolor='black',width=0.3,color="purple",label="Annual-MAX")
plt.hist(y,edgecolor='black',width=0.3,color="orange",label="JAN-FEB - MIN")
plt.hist(z,edgecolor='black',width=0.3,color="blue",label="JAN-FEB - MAX")
plt.xlabel("Temperature")
plt.ylabel("No of Days")
plt.legend()
plt.title("No of days vs Temperature")
plt.show()