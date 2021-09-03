from random import *
#son top o'yini
a=randint(1,10)
n=int(input('Son kiriting: '))
def top(x,y):
    res=[]
    while y==x:
        print(f'Tabriklaymiz siz biz o`ylagan sonni {len(res)} urunishda topdingiz')
        top()
    if y>x:
        print(f'{n} biz o`ylagan sondan katta.')
        res.append(y)
        n=int(input('Son kiriting: '))
        top(x,n)
    else:
        print(f'{n} biz o`ylagan sondan kichik.')
        res.append(y)
        n=int(input('Son kiriting: '))
        top(x,n)
top(a,n)
'''
1.randint()
2.n=son kiriting
3.n a ga tekshiruv
4.


'''
