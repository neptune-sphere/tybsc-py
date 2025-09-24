
import matplotlib.pyplot as plt

x=['17/10','18/10','19/10','20/10','21/10','22/10','23/10','24/10','25/10']
y=[25,26,25.5,24,23.7,26.8,28,30.2,31]

plt.figure(figsize=(9,7))
plt.grid()
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.plot(x,y,linewidth=0.5,linestyle='dotted')
plt.title("Date vs Temperature")
plt.show()