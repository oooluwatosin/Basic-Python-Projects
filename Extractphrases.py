name= input('Enter a file name: ')
fhand= open(name)
count=0
total=0
for line in fhand:
    line=line.rstrip()
    if line.startswith('X-DSPAM-Confidence: '):
        atpos=line[19:]
        atoos=float(atpos)
        count=count+1
        total=total+atoos
        lint=total/count
print('Average spam confidence: ', lint)
