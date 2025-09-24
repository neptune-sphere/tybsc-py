import matplotlib.pyplot as plt

ForestCover=[66964,28105,17346,17146,18186,12489,7726]
State=['Arunachal Pradesh','Assam','Manipur','Meghalaya','Mizoram','Nagaland','Tripura']
myexplode=[0,0,0,0,0.2,0,0]
plt.pie(ForestCover,labels=State,wedgeprops={"edgecolor":"black"},explode=myexplode,autopct='%1.1f%%')
plt.title("Forest Cover of north eastern states")
plt.legend(State,title="States",loc="upper left",bbox_to_anchor=(1,0,0,1))
plt.show()