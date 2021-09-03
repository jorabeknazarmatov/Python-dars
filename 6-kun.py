from math import *
from time import *
from random import *
'''#1-masala
sleep(.4)
print('1 dan N gacha bo’lgan natural sonlarni kvadratlarini yig’indisini hisoblovchi dastur')
sleep(.4)
n=int(input('N = '))
sleep(.4)
c=0
for i in range(1,n):
    c+=i**2
print('Natija {c} ga teng.')
#2-masala
sleep(.4)
print('N natural soni berilgan. 1 + 1/2 + 1/3 + ... + 1/N yig’indisini hisoblovchi dastur')
sleep(.4)
n=int(input('N = '))
sleep(.4)
c=0
res=0
for i in range(1,n):
    c+=1
    res+=1/c
print('Natija {res} ga teng.')
#3-masala
sleep(.4)
print('Klaviatura orqali N ta ixtiyoriy son yig’indisini hisoblovchi dastur')
sleep(.4)
n=int(input('N = '))
sleep(.4)
c=0
for i in range(1,n):
    c+=random()
print('Natija {c} ga teng.')
#4-masala
sleep(.4)
print('M dan N gacha bo’lgan toq sonlar ko’paytmasini hisoblovchi dastur')
sleep(.4)
m=int(input('M = '))
sleep(.4)
n=int(input('N = '))
sleep(.4)
c=1
if m<n:
    for i in range(m,n):
        if i%2!=0:
            c*=i
        else:
            continue
    print(f'Natija {c} ga teng.')
else:
    print(f'N < M Dasturda xatolik.')
#5-masala
sleep(.4)
print('M dan N gacha bo’lgan juft sonlar ko’paytmasini hisoblovchi dastur')
sleep(.4)
m=int(input('M = '))
sleep(.4)
n=int(input('N = '))
sleep(.4)
c=1
if m<n:
    for i in range(m,n):
        if i%2==0:
            c*=i
        else:
            continue
    print(f'Natija {c} ga teng.')
else:
    print(f'N < M Dasturda xatolik.')
#6-masala
sleep(.4)
print('Kiritilgan n natural soni uchun karra jadvalini hosil qiluvchi dastur')
sleep(.4)
n=int(input('N = '))
sleep(.4)
for i in range(1,11):
    print(f'{n} * {i} =',n*i)
'''#7-masala
sleep(.4)
print('Kiritilgan satrni teskari tartibda yozuvchi dastur')
sleep(.4)
n=input('4 xarfdan iborat Text kiriting = ')
z=0
a=''
b=''
c=''
d=''
sleep(.4)
for i in n:
    z+=1
    if z==1:
        a=i
    elif z==2:
        b=i
    elif z==3:
        c=i
    elif z==4:
        d=i
    else:
        continue
print(d,c,b,a)
