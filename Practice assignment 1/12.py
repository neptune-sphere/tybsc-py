print("---Enter marks---")
a,b,c,d,e=float(input()),float(input()),float(input()),float(input()),float(input())
avg=(a+b+c+d+e)/5
print("Average:",avg)
if(avg>=90.0):
    print("Grade A")
elif(avg>=80 and avg<90):
    print("Grade B")
elif(avg>=70 and avg<80):
    print("Grade C")
elif(avg>=60 and avg<70):
    print("Grade D")
elif(avg>=50 and avg<60):
    print("Grade E")
else:
    print("Grade F")