from pwn import *
context.log_level = 'debug'

# nc 103.162.14.116 14003
r = remote('103.162.14.116', 14004)

def find_ith_digit(i):
    # Bước 1: Khởi tạo các biến
    start = 1  # Giá trị bắt đầu của khoảng số
    digits = 1  # Số lượng chữ số
    while True:
        # Bước 2: Xác định độ dài của các khoảng số có số lượng chữ số tăng dần
        count = 9 * start * digits
        if i <= count:
            # Bước 3: Xác định số cụ thể trong khoảng số
            number = start + (i - 1) // digits
            # Bước 4: Xác định chữ số tại vị trí i trong số đó
            return str(number)[(i - 1) % digits]
        i -= count
        start *= 10
        digits += 1
        
    
print ("nhan duoc 1=> ", r.recv())

while(1):
    n =  int((r.recvline()).decode().split("= ")[1][:-1])

    print(n)

    r.send(find_ith_digit(n).encode())

    print ("nhan duoc 1=> ", r.recv())
    print ("nhan duoc 1=> ", r.recv())


# KCSC{dO_yOu_knOw_prOgrAmmIng_Is_vErY_ImpOrtAnt?}