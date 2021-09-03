from time import *
from math import *
from random import *
#1-masala
sleep(.4)
print('1-masala')
sleep(.4)
a=0
for i in range(20):
    sleep(.1)
    a=1
    print(f'{a} Salom dunyo.')
#2-masala
sleep(.4)
print('2-masala')
sleep(.4)
for i in range(1,50):
    sleep(.1)
    print(i)
#3-masala
sleep(.4)
print('3-masala')
print('1 va 2 sonlar orasidagi nechta juft son borligini ko`rsatadi.')
sleep(.4)
n=int(input('1 - Sonni kiririting: '))
sleep(.4)
m=int(input('2 - Sonni kiririting: '))
sleep(.4)
a=0
for i in range(n,m):
    if i%2==0:
        a+=1
    else:
        continue
print(f'{a}ta - juft son mavjud.')
#4-masala
sleep(.4)
print('4-masala')
print('1 va 2 sonlar orasidagi nechta toq son borligini ko`rsatadi.')
sleep(.4)
n=int(input('1 - Sonni kiririting: '))
sleep(.4)
m=int(input('2 - Sonni kiririting: '))
sleep(.4)
a=0
for i in range(n,m):
    if i%2!=0:
        a+=1
    else:
        continue
print(f'{a}ta - toq son mavjud.')
#5-masala
sleep(.4)
print('5-masala')
sleep(.4)
a=int(input('Sonni kiririting: '))
sleep(.4)
if a>=0:
    for i in range(1,a):
        print(f'{i} musbat son')
else:
    for i in range(a,0):
        print(f'{i}ta manfiy son')
#6-masala
sleep(.4)
print('6-masala')
print('1 va 2 sonlar orasidagi 3 ga qoldiqsiz bo`linadigan son borligini ko`rsatadi.')
sleep(.4)
n=int(input('1 - Sonni kiririting: '))
sleep(.4)
m=int(input('2 - Sonni kiririting: '))
sleep(.4)
a=0
for i in range(n,m):
    if i==0:
        continue
    elif i%3==0:
        a+=1         
    else:
        continue
if a==0:
    print('3 ga qoldiqsiz bo`linuvchi son mavjud emas.')
else:
    print(f'{a}ta - 3ga qoldiqsiz bo`linuvchi son mavjud.')
#7-masala
sleep(.4)
print('7-masala')
print('1 va 2 sonlar orasidagi 4 ga qoldiqsiz bo`linadigan son borligini ko`rsatadi.')
sleep(.4)
n=int(input('1 - Sonni kiririting: '))
sleep(.4)
m=int(input('2 - Sonni kiririting: '))
sleep(.4)
a=0
for i in range(n,m):
    if i==0:
        continue
    elif i%4==0:
        a+=1         
    else:
        continue
if a==0:
    print('4 ga qoldiqsiz bo`linuvchi son mavjud emas.')
else:
    print(f'{a}ta - 4ga qoldiqsiz bo`linuvchi son mavjud.')
#8-masala
sleep(.4)
print('8-masala')
print('1 dan 100 gacha bo`lgan sonlar yig`indisini ko`rsatadi.')
sleep(.4)
c=0
for i in range(1,101):
    c+=i
sleep(.4)
print(f'1 dan 100 gacha bo`lgan sonlar yig`indisi {c}ga teng')
#9-masala
sleep(.4)
print('9-masala')
print('1 dan N gacha sonlar orasida M ga qoldiqsiz bo`linadigan nechta son borligini ko`rsatadi.')
sleep(.4)
n=int(input('N - Sonni kiririting: '))
sleep(.4)
m=int(input('M - Sonni kiririting: '))
sleep(.4)
a=0
for i in range(1,n):
    if i%m==0:
        a+=1
    else:
        continue
print(f'1 dan {n} gacha bo`lgan sonlar orasida {m} ga qoldiqsiz bo`linadigan {a}ta son bor.')
#10-masala
sleep(.4)
print('10-masala')
print('1 dan N gacha bo`lgan juft sonlar o`rta arifmetigini hisoblaydigan dastur.')
sleep(.4)
n=int(input('N - Sonni kiririting: '))
sleep(.4)
a=0
c=0
for i in range(1,n):
    if i%2==0:
        a+=1
        c+=i
    else:
        continue
res=round(c/a)
print(f'1 dan {n} gacha bo`lgan juft sonlar o`rta arifmetigi {res} ga teng')
#11-masala
sleep(.4)
print('11-masala')
print('1 dan N gacha bo`lgan toq sonlar o`rta arifmetigini hisoblaydigan dastur.')
sleep(.4)
n=int(input('N - Sonni kiririting: '))
sleep(.4)
juft=0
qiymat=0
for i in range(1,n):
    if i%2!=0:
        juft+=1
        qiymat+=i
    else:
        continue
res=round(qiymat/juft)
print(f'1 dan {n} gacha bo`lgan toq sonlar o`rta arifmetigi {res} ga teng')
#12-masala
sleep(.4)
print('12-masala')
print('1 dan N gacha bo`lgan sonlarni toq va juftga hisoblaydigan dastur.')
sleep(.4)
n=int(input('N - Sonni kiririting: '))
sleep(.4)
for i in range(1,n):
    if i%2==0:
        print(f'{i} - Salom juft son.')
    else:
        print(f'{i} - Salom toq son.')
#13-masala
sleep(.4)
print('13-masala')
print('1 dan N gacha bo`lgan sonlarni ichi yurib chiqadi va M sonini qoldirib o`tadi.')
sleep(.4)
n=int(input('N - Sonni kiririting: '))
sleep(.4)
m=int(input('M - Sonni kiririting: '))
sleep(.4)
if m>=1 and m<n:
    for i in range(1,n):
        if m==i:
            continue
        else:
            print(f' {i} ')
else:
    print('Dasturda xatolik!')
    print(f'{m} soni - 1 va {n} oralig`ida emas.')
#14-masala
sleep(.4)
print('14-masala')
print('1 dan N gacha bo`lgan sonlarni ichi yurib chiqadi va M sonigacha bo`lgan sonlarni ko`rsatadi.')
sleep(.4)
n=int(input('N - Sonni kiririting: '))
sleep(.4)
m=int(input('M - Sonni kiririting: '))
sleep(.4)
if m>=1 and m<n:
    for i in range(1,n):
        if m==i:
            break
        else:
            print(f' {i} ')
else:
    print('Dasturda xatolik!')
    print(f'{m} soni - 1 va {n} oralig`ida emas.')
#15-masala
sleep(.4)
print('15-masala')
print('1 dan N gacha bo`lgan sonlarni kamayish tartibida ko`rsatadi.')
sleep(.4)
n=int(input('N - Sonni kiririting: '))
sleep(.4)
for i in range(n,0,-1):
    print(i)
sleep(10)
