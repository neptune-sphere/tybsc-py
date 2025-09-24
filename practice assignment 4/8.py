f=open("cities.txt","r")
data=f.read()
data=data.replace('a','x')
f.close()

f=open("cities.txt","w")
f.writelines(data)
f.close()