
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
    
    
print(process("()()(())(())))()(((()(()())(()()()))(())))()((()"))
            