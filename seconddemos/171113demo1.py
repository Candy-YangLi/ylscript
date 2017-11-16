#key parameters
def functest(a,b=10,c=30):
    '''在函数的第一个逻辑行的字符串是这个函数的 文档字符串
    print the key parameters
    print print print'''
    print("a=%d,b=%d,c=%d"%(a,b,c))
functest(10,30,20)
functest(10,c=30,b=20)
functest(10,c=30,b=20)
functest(b=10,a=30,c=20)
print(functest.__doc__)