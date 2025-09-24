import pickle

n=int(input("Enter number of records : "))

def createFile():
    for i in range(n):
        file=open("book.dat","ab")
        book_no = int(input("Enter book number: "))
        name = input("Enter book Name: ")
        book_auth=input("Enter author: ")
        price = int(input("Enter price: "))
        mylist=[book_no,name,book_auth,price]
        pickle.dump(mylist,file)

def  countRec(book_auth):
    file=open("book.dat","rb")
    cnt=0
    for i in range(n):
        record=pickle.load(file)
        if record[2]==book_auth:
            cnt+=1
    print("Total records : ",cnt)


createFile()
mystr=input("Enter author name: ")
countRec(mystr)