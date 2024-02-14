fname = input("Enter file name: ")
if len(fname) < 1:
    fname = 'shakespeare.txt'
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for i in range(len(words)):
        if words[i] not in lst:
            lst.append(words[i])
            
            
lst.sort()
print(lst)