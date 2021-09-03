import re
while True:
    n=list(map(str,input('Text kiritin biz uni tekshiramiz.').split(',')))
    test='^T......k$'
    res=[]
    for i in n:
        a=re.match(test,i)
        if a:
            res.append(i)
        else:
            continue
    if res==[]:
        continue
    else:
        print(res)
        break

#[n] n - qayerda qatnashgan bo'lsa qaytaradi. So'z o'rtasidagini ham.
pattern = '[To]'
ism = list(map(str,input('Text kiriting: ').split()))
print(ism)
for i in ism:
    res = re.findall(pattern,i)
    if res:
        print(i)
    else:
        continue
#^ matn boshini tekshirish
pattern = '^To'
ism = list(map(str,input('Text kiriting: ').split()))
for i in ism:
    res = re.findall(pattern,i)
    if res:
        print(i)
    else:
        continue
#$ matn boshini tekshirish
pattern = 'bek$'
ism = list(map(str,input('Text kiriting: ').split()))
for i in ism:
    res = re.findall(pattern,i)
    if res:
        print(i)
    else:
        continue
# . matnda ishlatilgan harflar sonini tekshirish
pattern = '...'
ism = list(map(str,input('Text kiriting: ').split()))
for i in ism:
    res = re.findall(pattern,i)
    if res:
        print(i)
    else:
        continue
#\A SATR boshini tekshirish
pattern = '\AMen'
ism = 'To`rabek Meni ismim'
res = re.findall(pattern,ism)
print(res)
if res:
    print("Moslik bor.")
else:
    print('Moslik yo`q')
#\d matnda sonlar ishtirokini tekshirish
pattern = '\d'
ism = 'To`rabek Meni ismim. Yoshim 25da men 2 kursman'
res = re.findall(pattern,ism)
print(res)
if res:
    print("Moslik bor.")
else:
    print('Moslik yo`q')
#\D matnda harflar ishtirokini tekshirish
pattern = '\D'
ism = 'To`rabek Meni ismim'
res = re.findall(pattern,ism)
print(res)
if res:
    print("Moslik bor.")
else:
    print('Moslik yo`q')
#\s matnda probel yoki tabulyatsiya ishtirokini tekshirish
pattern = '\s'
ism = 'To`rabek Meni ismim'
res = re.findall(pattern,ism)
print(res)
if res:
    print("Moslik bor.")
else:
    print('Moslik yo`q')
#\S matnda probel yo`qligini tekshirish
pattern = '\S'
ism = 'To`rabek Meni ismim'
res = re.findall(pattern,ism)
print(res)
if res:
    print("Moslik bor.")
else:
    print('Moslik yo`q')
#Sub mos keladigan matnni siz tanlagan matn bilan almashtiradi
ism = 'To`rabek Meni ismim'
res = re.sub('i','e',ism)
print(res)
#Sub ichiga raqam bersak shuncha moslikni almashtiradi
ism = 'To`rabek Meni ismim'
res = re.sub('i','e',ism,1)
print(res)
#split() matndan probellarni olib tashlaydi.
pattern = '\s'
ism = 'To`rabek Meni ismim'
res = re.split(pattern,ism)
print(res)






















