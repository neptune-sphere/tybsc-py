mystr=input('Enter a string:')
mydic={ch:mystr.count(ch) for ch in mystr}
print(mydic)