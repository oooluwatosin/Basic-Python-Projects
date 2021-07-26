name= input('Enter a file name: ')
fhand= open(name)
counts=dict()
for line in fhand:
    line=line.rstrip()
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        words=line.split()
        some=words[5]
        plan=some.split(':')
        smile=plan[0]
        counts[smile]=counts.get(smile, 0)+1
t=sorted(counts.items())
for k,v in sorted(counts.items()):
    print (k,v)
