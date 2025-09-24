import matplotlib.pyplot as plt


dc = [10, 20, 30, 40, 50]
sales = [55000, 65000, 75000, 85000, 125000]
mycolors=['blue','hotpink','orange','green','red']
plt.scatter(dc,sales,marker="*",color=mycolors)
plt.title("Sales vs Discount")
plt.xlabel("Discount in percentage")
plt.ylabel("Sales in Rs.")
plt.show()