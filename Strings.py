tree= 'X-DSPAM-Confidence:0.8475 '
three= tree.find(':')
print(three)
tress=tree.find(' ',three)
print(tress)
spot=tree[three+1:tress]
print(spot)
float(spot)
