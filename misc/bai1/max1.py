from pwn import *
context.log_level = 'debug'

# nc 103.162.14.116 14002

def solve(recv1):
    recv = recv1.decode()

    recv = recv.split("= ")[1]
    recv = (recv[1:-2]).split(",")
    print(recv)
    
    recv = [int(i) for i in recv]

    res = (max(recv))
    return res

r = remote('103.162.14.116', 14002)

print ("nhan duoc 1=> ", r.recv())
while(1):
    rec1 =  r.recvline()
    print ("nhan duoc 1=> ", r.recv())

    res = solve(rec1)

    r.send(str(res).encode())

    print ("nhan duoc 1=> ", r.recv())

# KCSC{Ezzz_Programmingggg}
