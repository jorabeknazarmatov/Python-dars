#1-masala
n=int(input('Son kiriting: '))
c=lambda x: x+15
print(c(n))
#2-masala
for i in range(20,40):
    res=lambda i: i%2==0
    if res(i):
        print(i)
    else:
        continue
#3-masala
n=int(input('Son kiriting: '))
daraja=lambda y: n**y
kvadrat=daraja(2)
kub=daraja(3)
print(f"{n} ning kvadrati {kvadrat} ga, kubi esa {kub} ga teng")
#4-masala
n=input('Text kiriting: ')
simb=input('Bitta xarf kiriting: ')
z=lambda x: x.startswith(simb) 
print(z(n))
#5-masala
n=list(map(int, input('Sonlar kiriting: ').split()))
juft=0
toq=0
for i in n:
    res=lambda x: x%2==0
    if res(i):
        juft+=1
    else:
        toq+=1
print(f"{n}\nichida {juft} ta juft va {toq} ta toq son bor")
#6-masala
n=list(map(str, input('Textlar kiriting: ').split()))
for i in n:
    res=lambda x: len(x)==6
    if res(i):
        print(f'uzunligi 6 ga teng text bu : {i} ')
    else:
        continue

