def displayword():
     file=open("demo.txt","r")
     line=file.read()
     word=line.split()
     for w in word:
          if len(w)<4:
               print(w)
     file.close

displayword()