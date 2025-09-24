mystr=input('Enter a string: ')

freq={ch:mystr.count(ch) for ch in mystr}
print(freq)


# max=0
# val=freq.values()
# for i in val:
#     if i > max:
#         max=i

# print(max)

val = max(freq,key=freq.get)
print(val)


# for ch in mystr:
#     if ch not in freq:
#         freq[ch]=1
#     else:
#         freq[ch]+=1


    

