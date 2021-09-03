from math import *
from time import *
from random import *
'''#1-malasa
n=[6,2,62,52,32,4,52]
for i in n:
    print(i**3)
#2-masala
n=[6,2,62,52,32,4,52]
m=[]
for i in n:
    res=i**2
    m.append(res)
print(m)
#3-masala
n=[6,2,62,52,32,4,52]
j=0
k=0
for i in n:
    if i%2==0:
        j+=1
    else:
        k+=1
print(f'Juft son: {j}ta, Toq son: {k}ta.')
#4-masala
n=[6,2,62,52,32,4,52]
j=0
k=0
for i in n:
    if i>=0:
        j+=1
    else:
        k+=1
print(f'Musbat son: {j}ta, Manfiy son: {k}ta.')
#5-masala
n=[6,2,62,52,32,4,52]
res=max(n)/2
for i in n:
    if i>res:
        print(i)
    else:
        continue
'''
#1-misol
n=list(range(randint(1,100)))
print(n)
