#a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
#odds = a[::2]
#evens = a[1::2]
#print(odds)
#print(evens)

x='我是中国人'
y = x.encode('utf-8')
z= y[::-1]
print(y)
print(z)
print(z.decode('utf-8'))

a= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'g']
a[::2]   #  ['a','e','c','a']
a[::-2]   # ['h', 'f', 'd', 'b']