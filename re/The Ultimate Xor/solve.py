

rbp0x10= []
xoral = []

status = True
with open('asm1.asm', 'r') as f:
    for line in f.readlines():
        if("[rbp - 0x10]," in line):
            if(status):
                print(line)
                xoral.append(0)
            rbp0x10.append(int(line.split(",")[1],16))
            status = True
        elif("xor" in line):
            status = False
            xoral.append(int(line.split(",")[1],16))



print(len(rbp0x10))
print(len(xoral))

flag = ""
for i in range(len(rbp0x10)):
    flag += chr(rbp0x10[i]^xoral[i+1] )
    
print(flag)