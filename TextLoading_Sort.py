a = open('text.txt').read().split()
a.sort()
for i in a[::-1]:
    print (i)

#別解
#print (sorted(open('text.txt').read().split(), key = int, reverse = True))
