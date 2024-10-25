from string import *
from array import *
tters = [ascii_letters]
auto = [digits]
au = [f for x in auto for f in x]
le = [m for x in tters for m in x]
le.extend(au)
del le[-1],au,tters,auto




l = dict.fromkeys(le,0)
l['9'] = -1

le = array('u',le)
print(l)

k = input("Enter some words   ")

m = ''

for i in k:
    print(i, end = ' ')
    print(l[i])
    print(le[l[i] + 1])
    r = le.index(i)
    m += le[l[i] + 1]
    l[i] += 1
    print(l[i])
print(m)
print(l)
'''k = int(input("Enter "))
print(len(le))
print(au, le)
'''#words = dict(dic)
