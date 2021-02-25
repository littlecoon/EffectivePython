def ddd(a,b):
    b.append(a)
    print(id(b)) #查看内存地址
    return b

print(ddd(1,[1,2,3]))
print(ddd(2,['a','b','c']))
print(ddd(3,[1,2,3]))