def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-44444))

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))
print(power(5,2))
print(power(5,3))

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)