from math import *
from random import *
from time import *
#1-masala
print('1-masala')
sleep(.4)
a=int(input('Haqiqiy son kiriting: A = '))
sleep(.4)
b=int(input('Haqiqiy son kiriting: B = '))
sleep(.4)
if a>b:
    c=int(input('Haqiqiy son kiriting: C = '))
    print('Natija',a+b+c,'ga teng')
elif a<b:
    c=int(input('Haqiqiy son kiriting: C = '))
    print('Natija',a*b*c,'ga teng')
else:
    print("A va B sonlari teng va ular qiymati",a+b,"ga teng. Dastur tugadi.")
#2-masala
sleep(.4)
print("2-masala")
sleep(.4)
a=int(input('Haqiqiy son kiriting: A = '))
sleep(.4)
b=int(input('Haqiqiy son kiriting: B = '))
sleep(.4)
if a>b:
    c=int(input('Haqiqiy son kiriting: C = '))
    z=sqrt(a**2+b**2+c**2)
    if z<0:
        print('Dasturda xatolik!!!')
    else:
        print('Natija',z,'ga teng.')
if a<b:
    c=int(input('Haqiqiy son kiriting: C = '))
    z=sqrt(a**2-b**2+c**2)
    sleep(.4)
    if z<0:
        print('Dasturda xatolik!!!')
    else:
        print('Natija',z,'ga teng.')
else:
    print("Dastur tugatildi.")
#3-masala
a=int(input('1 - Xaqiqiy son yoki butun son kiriting = '))
b=int(input('2 - Xaqiqiy son yoki butun son kiriting = '))
if a>=0 and b>=0:
    print('Ikkala son ham musbat')
elif (a>=0 and b<0)or(b>=0 and a<0):
    print('Sonlarning biri manfiy')
else:
    print('Ikkala son ham manfiy')
#4-masala
sleep(0.3)
print('4-masala')
sleep(0.3)
a=int(input("Haqiqiy son kiriting: A = "))
sleep(0.3)
b=int(input("Haqiqiy son kiriting: b = "))
sleep(0.3)
if a>b and b>5:
    sleep(0.3)
    print("Bahor")
elif a==b:
    z=(a+b)/(a**2+b**2+1)
    sleep(0.3)
    print('Natija',z,'ga teng.')
else:
    c=randint(0,10)
    z=sqrt(c)*sin(c**2+a**2+b)-1/7
    sleep(0.3)
    print('Natija',z,'ga teng.')
#5-masala
sleep(.4)
print('5-masala')
sleep(.4)
a=int(input('Haqiqiy son kiriting: A = '))
sleep(.4)
b=int(input('Haqiqiy son kiriting: B = '))
if a<b:
    sleep(.4)
    c=int(input('Musbat son kiriting: C = '))
    z=2*a**2*b**3*c-1/3*sqrt(c)
    sleep(.4)
    print('Natija',z,'ga teng.')
else:
    sleep(.4)
    print('Dastur tugadi.')
#6-masala
sleep(.4)
print('6-masala')
sleep(.4)
a=int(input('Haqiqiy son kiriting: A = '))
sleep(.4)
b=int(input('Haqiqiy son kiriting: B = '))
sleep(.4)
if a==abs(b):
    z=sin(a**2+b**2)**2
    print(z)
elif a<b:
    print('boshqa son kiriting ')
elif a<0 and b<0:
    c=int(input('Haqiqiy son kiriting: c = '))
    z=log(a**2+b**2)+exp(c)
    sleep(.4)
    print('Natija',z,'ga teng.')
else:
    print('Dastur tugadi')
#7-masala (Qo'shimch qo'shilgan)
sleep(.4)
print('7-masala')
sleep(.4)
a=int(input('Son kiriting: A = '))
sleep(.4)
b=int(input('Son kiriting: B = '))
z=a+b
sleep(.4)
if (a%2==0) and (b%2==0):
    print('Kiritilgan sonlar juft.','Ularning qiymati: ',z,' ga teng.')
elif (a%2!=0) and (b%2!=0):
    print('Kiritilgan sonlar toq.','Ularning qiymati: ',z,' ga teng.')
else:
    print('Kiritilgan sonlarning biri toq.')
    if a%2!=0 and b%2==0:
        print('A - toq son','Ularning qiymati: ',z,' ga teng.')
    else:
        print('B - toq son','Ularning qiymati: ',z,' ga teng.')
#8-masala
sleep(.4)
print('8-masala')
sleep(.4)
a=int(input('Haqiqiy son kiriting: A = '))
sleep(.4)
b=int(input('Haqiqiy son kiriting: B = '))
sleep(.4)
if a>b:
    c=int(input('Haqiqiy son kiriting: C = '))
    sleep(.4)
    d=int(input('Haqiqiy son kiriting: D = '))
    if c>d:
        z=c**2+a**2-d**2-b**2
        print('Natija',z,'ga teng.')
    else:
        print('Dastur tugatildi')
elif a<b:
    c=int(input('Haqiqiy son kiriting: C = '))
    if c<8:
        z=log(a**2+b**2)+exp(c)
        sleep(.4)
        print('Natija',z,'ga teng.')
else:
    print('Dastur tugatildi')
#9-masala
sleep(.4)
print('9-masala')
sleep(.4)
a=int(input('Haqiqiy son kiriting: A = '))
sleep(.4)
b=int(input('Haqiqiy son kiriting: B = '))
sleep(.4)
if a>0 and a%2==0:
    c=int(input('Haqiqiy son kiriting: C = '))
    if c%2==0:
        sleep(.4)
        z=a**2+b**2+c**2
        print('Natija ',z,' ga teng.')
    else:
        print('Dastur tugadi.')
else:
    print('Dastur tugadi.')
#10-masala 
sleep(.4)
print('10-masala')
sleep(.4)
a=int(input('Haqiqiy son kiriting: A = '))
sleep(.4)
b=int(input('Haqiqiy son kiriting: B = '))
sleep(.4)
if a>=b:
    c=int(input('Haqiqiy son kiriting: C = '))
    a+=1
    b+=1
    c-=1
    z=a**7+(a*b/19)+c**5
    print('A = ',a,', B = ',b,', C = ',c,' ga o`zgardi.')
    print('Natija ',z,' ga teng')
else:
    print('Dastur tugadi.')
#12-masala
sleep(.4)
print('12-masala')
sleep(.4)
a=int(input('Haqiqiy son kiriting: A = '))
sleep(.4)
b=int(input('Haqiqiy son kiriting: B = '))
sleep(.4)
c=int(input('Haqiqiy son kiriting: C = '))
sleep(.4)
if (a-b)>c:
    print('A-B katta C dan.')
else:
    print('Dastur tugadi')
#13-masala
sleep(.4)
print('13-masala')
sleep(.4)
a=int(input('Haqiqiy son kiriting: A = '))
sleep(.4)
b=int(input('Haqiqiy son kiriting: B = '))
sleep(.4)
c=int(input('Haqiqiy son kiriting: C = '))
sleep(.4)
if a==b and c>0:
    print('Mening sevimli futbol jamoam ',input(),'!')
elif a>b and c>0:
    z=a**2+(b/a**2+1)+sqrt(c)
    print('Natija ',z,' ga teng.')
else:
    print('Dastur tugadi')
#14-masala
sleep(.4)
print('14-masala')
sleep(.4)
a=int(input('Kompyuter narxini kiriting = '))
sleep(.4)
b=int(input('Pulingizni miqdorini kiriting = '))
sleep(.4)
if b>=a:
    print('Siz ushbu maxsulotni sotib olishingiz mumkin.')
else:
    z=a-b
    print('Sizga',z,'so`m mablag` yetmayapti.')
#15-masala
sleep(.4)
print('15-masala')
sleep(.4)
a=int(input('Samsung S3 narxi = '))
sleep(.4)
b=int(input('Pulingizni miqdorini kiriting = '))
sleep(.4)
if b>=a:
    print('Siz ushbu Samsung-S3 telefonini sotib olishingiz mumkin.')
    print('Sotib olish uchun 1 ni bosing')
    c=int(input())
    if c==1:
        sleep(.4)
        print('Telefon sotib olindi!!!')
        print('Xozida balansingizda ',b-a,'so`m pulingiz qoldi.')
    else:
        sleep(.4)
        print('Sotib olish uchun 1 ni bosing')
else:
    z=a-b
    print('Sizga',z,'so`m mablag` yetmayapti.')

