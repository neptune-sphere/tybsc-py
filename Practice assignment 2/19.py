file = open("lorem.txt", "r")

nline = 0
nwords = 0
nchar = 0

for line in file:
  line = line.strip("\n")
  words = line.split(' ')
  nline += 1
  nwords += len(words)
  nchar += len(line)
file.close()

print('Characters',nchar)
print('words',nwords)
print('lines',nline)