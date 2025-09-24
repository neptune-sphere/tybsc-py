import matplotlib.pyplot as plt

import pandas as pd

df=pd.read_csv("E:\TYBCS\Python\College\Practice assignment 8\insurance.csv")
x=df['bmi']
y=df['charges']

plt.scatter(x,y)
plt.xlabel("BMI")
plt.ylabel("Charges")
plt.title("BMI vs Charges Scatter plot")
plt.show()

print(df['region'].value_counts())

x=[364,325,325,324]

lb=['southeast','northwest','southwest','northeast']
plt.pie(x,labels=lb,shadow=True,autopct='%1.1f%%')
plt.legend(loc="upper left",bbox_to_anchor=(1,0,0,1))
plt.show()

x=df['bmi']
plt.hist(x,width=1.5,color='red')
plt.title('BMI')
plt.xlabel('BMI')
plt.show()

x=df['children']
plt.hist(x,width=0.4,color='blue')
plt.title('Children')
plt.xlabel('Children')
plt.show()

x=df['age']
plt.hist(x,width=1.5,color='green')
plt.title('Age')
plt.xlabel('Age')
plt.show()

x=df['charges']
plt.hist(x,width=5000,color='orange')
plt.title('Charges')
plt.xlabel('Charges')
plt.show()


