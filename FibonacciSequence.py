#こんな代入の方法がある
a=b=1
while a < 2**10:
    print (a)
    a, b = b, a+b