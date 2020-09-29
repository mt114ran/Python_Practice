from functools import reduce

#パターン１
s = 0
for x in range(1,101):
    s += x
print (s)

#パターン２
print (sum(range(1,101)))

#パターン３
print (sum(x for x in range(1,101)))

#パターン４
print (reduce(lambda x,y: x+y, range(1,101)))

#パターン５
print (100*101/2)
