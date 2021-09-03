from random import *
'''#1-masala
oilam={
        'onam':{
                'name':'Shoxsanam',
                'born':1968,
                'born_adress':'Toshkent'
                },
        'otam':{
                'name':'Xusanboy',
                'born':1958,
                'born_adress':'Boyovut'
                },
        'ukam':{
                'name':'Jo`rabek',
                'born':1999,
                'born_adress':'Boyovut'
                }
        }
for kim,param in oilam.items():
        print(f"\n{kim.title()} {param['name'].title()}, tug'ilgan yili {param['born']}, tug'ilgan manzili {param['born_adress'].title()}")
#2-masala
opcham={
        'kim':'Umida',
        'taom':'Honim'
        }
ukam={
        'kim':'Jo`rabek',
        'taom':'Chuchvara'
        }
men={
        'kim':'To`rabek',
        'taom':'Osh'
        }
sevimli=[opcham,ukam,men]
for i in sevimli:
        print(f"\n{i['kim']}ning sevimli taomi bu {i['taom']}")
#3-masala
dostlar={
        'Sardor':{
                'tel':'Motorola',
                'model':'S5'
                },
        'Doston':{
                'tel':'Samsung',
                'model':'G5'
                },
        'Tohir':{
                'tel':'Sony',
                'model':'Xperia'
                },
        'Muxrish':{
                'tel':'Nokia',
                'model':'1202'
                },
        'Islom':{
                'tel':'PoCo',
                'model':'2012'
                },
        }
#4-masala
countrys={
    'country':['O`zbekiston','Tojikiston','Qirg`iziston','Rossiya','AQSH','Buyuk Britaniya']
    }
capitals={
    'capital':['Toshkent','Dushanbe','O`sh','Moskva','Vashington','London']
    }
m=sorted(countrys['country'])
n=sorted(capitals['capital'])
print(m)
print(n)
'''#5-masala
foods={
    'osh':{
        'price':9000
        },
    'manti':{
        'price':8000
        },
    'xonim':{
        'price':8500
        },
    'lag`mon':{
        'price':8000
        },
    'chuchvara':{
        'price':11000
        },
    'shashlik':{
        'price':12000
        },
    'somsa':{
        'price':6000
        },
    'jarkop':{
        'price':10000
        },
    'jazz':{
        'price':13000
        },
    'lavash':{
        'price':15000
        },
    }
res=0
summ=0
for i,j in foods.items():
    print()
    n=input('Nima yeyishni xoxlaysiz? ')
    if n==i.title():
        res+=1
        summ+=j['price']
        print(f"{i} - {j['price']} so'm")
    elif res==3:
        print(f"Siz 3ta maxsulot zakaz qildingiz. Sizdan {summ} so'm bo'ldi")
        break
    else:
        print(f"Siz so'ragan {n} bizning menuda yo'q. Uzur")
        if res!=0:
            print(f"Siz {res}ta maxsulot zakaz qildingiz. Sizdan {summ} so'm bo'ldi")
        else:
            break


