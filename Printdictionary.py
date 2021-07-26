name= input('Enter a file name: ')
fhand= open(name)
counts=dict()
for line in fhand:
    line=line.rstrip()
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        words=line.split()
        some=words[1]
    #for some in words:
        counts[some]=counts.get(some, 0)+1
largest=None
bigword=None
for word,count in counts.items():
    if largest is None or count>largest:
        largest=count
        bigword=word
print(bigword, largest)
