from pwn import *
context.log_level = 'debug'

# nc 103.162.14.116 14003
r = remote('103.162.14.116', 14004)


stringnum = ""

for i in range(0,99999):
    stringnum += str(i) 
    
print ("nhan duoc 1=> ", r.recv())

while(1):
    n =  int((r.recvline()).decode().split("= ")[1][:-1])

    print(n)

    r.send(stringnum[n].encode())

    print ("nhan duoc 1=> ", r.recv())
    print ("nhan duoc 1=> ", r.recv())
