from pwn import *
context.log_level = 'debug'

# nc 103.162.14.116 14003
r = remote('103.162.14.116', 14003)

def process(ex):
    check = 0
    ok = True # ktra mo ngoac chua
    ex = str(ex).strip()
    if(ex[0] == ')'): return False
    for i in ex:
        if(check <0): 
            return False
        if(i == "("):
            check += 1
        elif(i == ")"):
            check -= 1
            
    if(check == 0):
        return True
    else:
        return False
    

print ("nhan duoc 1=> ", r.recv())
while(1):
    debai =  (r.recvline()).decode().split(": ")[1][:-1]

    print("debai = ", debai)
    res = process(debai)

    if(res):
        r.send(b"yes")
    else:
        r.send(b"no")

    print ("nhan duoc 1=> ", r.recvline())


# KCSC{Smile_Emoji____:)___}
