it = (len(x) for x in open(r'article07.py'))
print(it)

print(next(it))
print(next(it))

roots =((x,x **0.5) for x in it)
print(next(roots))


flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s'%(i+1, flavor))

for i ,flavor in enumerate(flavor_list):
    print('%d: %s'%(i+1, flavor))