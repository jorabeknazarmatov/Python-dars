maxsulot = {
        'olma': 3000,
        'kofe': 35000,
        'choy': 8000,
        'shakar': 3000,
        'gurunch': 7000,
        'go`sht': 75000,
        'shaftoli': 12000,
        'gilos': 9000,
        'banan': 16000,
        'nok': 8000,
        'bexi': 15000,
    }
print('\nAssalom aleykum. Bizning do`konchamizga hush kelibsiz.')
print('Bizda eng shirin va eng kerakli maxsulotlar mavjud.')
print('tovarlarimiz katalogi bilan tanishib chiqing.\n')
for i,j in maxsulot.items():
    print(f"    {i} - {j} so`m.")
res=0
jami=0
while True:
    n = input('\nTovar nomini yozing (to`xtatish uchun "Q" ni kiriting): ')
    if n=='q' or n=='Q':
        if jami==0:
            print("Siz hech narsa harid qilmadingiz.")
        else:
            print(f"Siz {res} ta maxsulot sotib oldingiz. Sizdan {jami} so'm.")
        break
    kg = int(input('Nechi kg olasiz: '))
    for i,j in maxsulot.items():
        if n==i:
            res+=1
            jami+=(j*kg)
