from  collections import  Iterable
L = []
n = 0
while n <= 99:
    L.append(n)
    n = n + 1
print(L)
#切片
print(L[0:3])
print(L[0:10])
print(L[-4:])
print(L[-4:-2])
print(L[:10:2])


d = {'a': 1, 'b': 2, 'c': 3}
for k,v in d.items():
    print("key=%s value=%s" % (k,v) )
print(isinstance(d, Iterable))
print(isinstance("abc", Iterable))

for keyvalue in d:
    print(keyvalue)

llcreate= [x * x for x in range(1, 11)]
print(llcreate)

L1 = ['Hello', 'World', 18, 'Apple', None]
print(L1)
L2 = [ll.lower() for ll in L1 if isinstance(ll,str)]
print(L2)

