
def determination_prime(num):
    MAX = 1000
    LIST = range(2, MAX + 1)
    for i in range(2, int(MAX ** 0.5)):
        LIST = [x for x in LIST if (x == i or x % i != 0)]
    
    return num in LIST

    
num = input("素数判定をおこなう数字を入力してください >>> ")

if determination_prime(int(num)):
    print("{} は、素数です".format(num))
else:
    print("{} は、素数ではありません".format(num))
