import pickle

n=int(input("Enter number of students: "))

def createRec():
   
    for i in range(n):
        f=open("student.dat","ab")
        adm_no=int(input("Enter admission number: "))
        name=input("Enter name: ")
        perc=float(input("Enter percentage: "))
        mylist=[adm_no,name,perc]
        pickle.dump(mylist,f)

def countRec():
    f=open("student.dat","rb")
    cnt=0
    for i in range(n):
        record=pickle.load(f)
        if record[2]>75.0:
            print(record[0],record[1],record[2])
            cnt+=1
    print("Number of students scoring above 75% : ",cnt)

createRec()
print("---------Details--------")
countRec()