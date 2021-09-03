from time import *
#Tosh aqychi qog'oz
print('Tosh qaychi qog`oz. O`yiniga hush kelibsiz.')
user1=input('Birinchi ishtirokchi ismingizni kiriting: ')
user2=input('Ikkinchi ishtirokchi ismingizni kiriting: ')
print(f'Ishtirokchilarimiz {user1} va {user2} tosh, qaychi yoki qog`ozni tanlang')
print()
print('tosh ni tanlash uchun 1 ni bosing')
print('qaychi ni tanlash uchun 2 ni bosing')
print('qogo`z ni tanlash uchun 3 ni bosing')
print()
n=int(input(f'{user1}: '))
z=int(input(f'{user2}: '))
if (z and n)>0 and (z and n)<4:
    if (n==1 and z==3) or (n==2 and z==1) or (n==3 and z==2):
        print(f'{user2} g`olib bo`ldi.')
    elif n==z:
        print('Durrang')
    else:
        print(f'{user1} g`olib bo`ldi.')
else:
    print('Noto`g`ri ma`lumot kiritdingiz.')
sleep(5)

