

adict = {0:1}


def process(n):
    for i in range(n):
        if(adict.get(i) is None):
            if(i % 2 == 0):
                adict[i] = i * adict[i-1]
            else:
                adict[i] = i + adict[i-1]
                

process(15)

print(adict)

