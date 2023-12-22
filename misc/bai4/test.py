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
            return int(str(number)[(i - 1) % digits])
        i -= count
        start *= 10
        digits += 1
        
# Ví dụ sử dụng:
i = 2660284
result = find_ith_digit(i)
print(f"Ký tự thứ {i} là: {result}")


# khó quá nhờ chatgpt