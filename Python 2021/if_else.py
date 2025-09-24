#x=int(input("Enter a number"))
#nested if
    # if x%5 == 0 :  
    #     if x%7 == 0:
    #         print(x ,"is divisible by 5 and 7")
    #     else :
    #         print(x, "is divisible by 5 only")
    # else :
    #     print(x, "is not divisible by 5 and 7 ")
 #normal if
    # if x%5 == 0 and x%7 == 0:
    #     print(x,"is divisible ny noth 5 and 7")
    # else :
    #     print(x, "is not divisible by 5 and 7")

#elif (else if ladder)

ch=input("enter a character")
if ch.isaplha():
    print(ch," is an alphabet")
elif ch.isdigit():
    print(ch,"is a digit")
