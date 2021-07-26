name= input('Enter a file name: ')
fhand= open(name)
new=[]
for line in fhand:
    line=line.rstrip()
    #words=line.split()
    for word in line.split():
        if not word in new:
            new.append(word)

new.sort()
print(new)
