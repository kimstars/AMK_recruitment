from Crypto.Util.number import getPrime

flag = b'KCSC{fake_flag}'

def verify(g, p, y, x, k, h):
    return (y*x*pow(g, k, p)) % p == pow(g, h, p)

p = getPrime(256)
g = getPrime(128)
y = 65537

lst_x = []
lst_h = []

print(f"p = {p}")
print(f"g = {g}")
print(f"y = {y}")

try:
    for i in range(20):
        x = 0
        h = 0
        x = int(input("x = "))
        h = int(input("h = "))
        if x in lst_x or h in lst_h:
            print('get out !!!')
            exit(-1)
        rs = verify(g, p, y, x, i, h)
        if rs:
            lst_x.append(x)
            lst_h.append(h)
        else:
            print('get out !!!')
            exit(-1)
            
    flag = open('flag.txt', 'rb').read()
    print(flag)
except:
    print("something went wrong")
