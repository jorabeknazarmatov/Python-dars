import re
'''#1-masala
n='osmon'
res = re.findall('^o...n$',n)
if res:
    print(res)
else:
    print('Xato')
#2-masala
n='osmon olomon omon'
res = re.findall('^o',n) and re.findall('n$',n) 
c = n.split()
for i in c:
    if len(i)>4:
        if res:
            print(i)
        else:
            print('Xato')
    else:
        continue
#3-masala
n=list(map(str,input('Text kiriting: ').split()))
txt=[]
for i in n:
    res = re.findall('B',i) and re.findall('r',i)
    if res:
        txt.append(i)
    else:
        continue
print(txt)
#4-masala
l_names=list(map(str,input('Familyalar kiritin men ajratib beraman: ').split()))
girls=[]
boys=[]
no=[]
for i in l_names:
    girl=re.findall('va$',i)
    boy=re.findall('v$',i)
    if girl:
        girls.append(i)
    elif boy:
        boys.append(i)
    else:
        no.append(i)
print('Qizlar: ',girls)
print('O`g`il bolalar: ',boys)
print('O`zbek emas shekilli: ',no)
#5-masala
n=list(map(str,input('Text kiriting: ').split()))
txt=[]
for i in n:
    res=re.findall('^Ana',i)
    if res:
        txt.append(i)
    else:
        continue
print(txt)
#6-masala
n='Abror1998, natija: Abror'
res=re.findall('\D',n)
print(res)
#7-masala
n='Abror1998, natija: Abror'
res=re.findall('\d',n)
print(res)
#8-masala
n='Salom aka qaley'
print(re.split(' ',n))
'''
#dastur 20-dars
i=0
while True:
    n=list(map(str,input("Matn nechta so’zdan iborat ekanligini topuvchi dastur: ").split()))
    print(f'Matn ichida {len(n)} ta text bor.')
    i+=1
    if i==3:
        break






















