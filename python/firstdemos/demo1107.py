# -*- coding: utf-8 -*-
height=1.75
weight=80.5
bmi=80.5/(1.75*1.75)
print("bmi=%f"%bmi)
#判断
if bmi<18.5:
    print("过轻")
elif bmi<25:
    print("正常")
elif bmi<28:
    print("过重")
elif bmi<32:
    print("肥胖")
else:
    print("严重肥胖")
#list列表
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print("Hello %s!"%name)
#dict词典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
print( 'Tracy'in d)
d.pop('Bob')
print(d)
d['yangli']=99
d['aaaa']=99
print(d)
ssset=set([1,2,3])
ssset.add(4)
ssset.remove(1)
ssset.add(4)
print(ssset)





