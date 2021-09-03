import os
'''#1-masala
with open('sonlar.txt','w') as r:
    r.write('Mening ismim To`rabek.\nYoshim 25 da.')
    r.close()
with open('sonlar.txt','r') as r:
    a=r.read(20)
    r.close()
print(a)
#2-masala
with open('sonlar.txt','r') as s:
    print(s.readline())
    s.close()
#4-masala
with open('sonlar.txt','a') as re:
    re.write('\nMen Dasturchiman.')
    re.close()
#5-masala
with open('sonlar.txt','r') as fo:
    res=fo.readlines()
    print(f'sonlar.txt da {len(res)} ta qator bor.')
    fo.close()
#6-masala
with open('sonlar.txt','r') as ko:
    mas=ko.readlines()
    print(mas)
    ko.close()
#7-masala
with open('sonlar.txt','r') as a:
    for i in a.readlines(): 
        print(i)
    a.close()
#8-masala
with open('sonlar.txt','r') as b:
    for i in b:
        if i=='\n':
            i=' '
        else:
            continue
    print(b.readelines())
    b.close()
'''
