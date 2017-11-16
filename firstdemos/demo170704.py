g = [x * x for x in range(1,10)]
g = (x * x for x in range(1,10))
for n in g:
    print(n,end=' ')
