import matplotlib.pyplot as plt

week1=[7500,5500,6100,4500,5700,4000,6500]
week2=[6800,4700,5700,4800,5400,2700,5900]
week3=[7100,4500,4000,3700,4000,2200,6100]
weekday=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
weeks=[week1,week2,week3]


plt.figure(figsize=(10,20))
plt.bar(weekday,week1,color="red",edgecolor="black")  
plt.bar(weekday,week2,color="blue",edgecolor="black")
plt.bar(weekday,week3,color="brown",edgecolor="black")

plt.title("Mela sales report")
plt.xlabel("Days")
plt.ylabel("Sales in Rs")

plt.show()
