# nc 103.162.14.116 14005

from pwn import *
context.log_level = 'debug'

# nc 103.162.14.116 14002
adict = {0:1}


def process(n):
    for i in range(n):
        if(adict.get(i) is None):
            if(i % 2 == 0):
                adict[i] = i * adict[i-1]
            else:
                adict[i] = i + adict[i-1]
                

r = remote('103.162.14.116', 14005)


print ("nhan duoc 1=> ", r.recv())

while(1):
    an  = (r.recv()).decode().split("\n>> a[")
    print("an= ", an)
    n = int(an[0].split("=")[1])
    a = int(an[1].split("]")[0])

    if(adict.get(a) is None):
        process(n+1)
        
    print(adict)
    res = (adict[a])

    r.send(str(res).encode())

    print ("nhan duoc 1=> ", r.recv())



# KCSC{KOREGA_REQUIEM_DA!!!_WWHaaaaaa___}
