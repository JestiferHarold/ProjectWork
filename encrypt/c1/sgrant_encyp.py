# from test import *
from platform import system
from string import *    

name = system()
tters = [ascii_letters, digits, punctuation]
print(tters)
auto = [digits]
anoter = [punctuation]
au = [f for x in auto for f in x]
le = [m for x in tters for m in x]
an = [d for x in anoter for d in x]
le.extend(au)
le.extend(an)
print(le)
m = le[-1]
del le[-1],au,tters,auto

l = dict.fromkeys(le,1)
l['~'] = -1

le.append(m)

k = input("Enter some words   ")
m = ''

for i in k:
    if i.isspace(): 
        m += ' '
        continue
    if l[i] +1 == 94:
        l[i] = 0    
    if l[i] + le.index(i) + 1 == 94 or i == "~":
        d = 0
        m = m + le[l[i] + 1]
        l[i] += 1
    else:
        l[i] = 0 if l[i]-1 > len(le) else l[i]
        r = le.index(i)
        m = m + le[l[i] + r]
        l[i] += 1

file = f"\\encrypt\\c1\\encrypted\\{m}.txt" if name in "Windows" else f"encrypt/c1/sencrypted/{m}.txt"

# create_encrypted_file(file, m)