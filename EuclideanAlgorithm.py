a = input("１つ目の数字を入力してください >>> ")
b = input("２つ目の数字を入力してください >>> ")

int_a = int(a)
int_b = int(b)

#再帰関数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print ("２つの数字の最大公約数は {} です".format(gcd(int_a,int_b)))