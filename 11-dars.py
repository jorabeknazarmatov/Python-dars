from math import *
from random import *
from time import *
coint=int(input('Sizda qancha pul bor: '))
royxat={
    'olma': 10000,
    'behi': 20000,
    'nok': 15000,
    'orik': 30000,
    'gilos': 8000,
    'banan': 40000,
        }
print()
for i,j in royxat.items():
    print(f"{i} - {j} so'm")
for i,j in royxat.items():
    a=input("Qaysi meva kerak ? (x - hech qaysi): ")
    if a==i:
        b=int(input("Necha kg? "))
        res=b*j
        if res<=coint:
            coint-=res
            print(f'Siz {res}so`m harajat qildingiz. Pulingiz {coint}so`m qoldi')
        else:
            pas=res-coint
            print(f'Sizning harajatingiz {res}so`m. Pulingiz {pas}so`m yetmayapti')
    else:
        print("So'm:",b*j)
        break
