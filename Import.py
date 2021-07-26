import re

file = open('medicine.txt')
sum = 0

for line in file:
    line = line.rstrip()
    line = re.findall('([0-9]+)', line)
    for i in line:
        i = int(i)
        sum += i

print(sum)
