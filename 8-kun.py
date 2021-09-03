from math import *
from time import *
from random import *
#1-malasa
n='Toshkent axborot texnologiyalari universiteti'
print(n)
z=0
for i in n:
    if i=='o':
        z+=1
    else:
        continue
print(f'"o" harfi satrda {z} ta joyda qatnashgan')
#2-masala
n=input()
z=0
for i in n:
    if i==i.upper():
        z+=1
print(f'katta harflar satrda {z} ta')
#3-masala
n=input()
z=0
c=0
res=
for i in n:
    if i==i.upper():
        z+=1
print(f'Satrda {res} foiz katta harf bor.')
