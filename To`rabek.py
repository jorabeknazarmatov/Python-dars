from time import *
#To`rabek
def harf(a):
    if a == 't' or a == 'T':
        for i in range(7):
            for j in range(7):
                if i==1 or (j==3 and i!=0):
                    print('*',end="")
                else:
                    print(' ',end="")
            print()
        print()
    elif a == 'o`' or a == 'O`':
        for i in range(7):
            for j in range(7):
                if i==0 and j==6 or ((i==1 or i==6) and j!=6) or (i!=0 and (j==0 or j==5)):
                    print('*',end="")
                else:
                    print(' ',end="")
            print()
        print()
    elif a == 'r' or a == 'R':
        for i in range(7):
            for j in range(7):
                if (i==0 or i==3) and j!=6 or (j==5 and (i==1 or i==2 or i==6)) or (i==4 and j==3) or (i==5 and j==4) or j==0:
                    print('*',end="")
                else:
                    print(' ',end="")
            print()
        print()
    elif a == 'a' or a == 'A':
        for i in range(7):
            for j in range(7):
                if (j==0 or j==5) and i!=0 or (i==0 and j!=6 and (j!=0 or j!=5 or j!=6)) or i==3 and j!=6:
                    print('*',end="")
                else:
                    print(' ',end="")
            print()
        print()
    elif a == 'b' or a == 'B':
        for i in range(7):
            for j in range(7):
                if j==0 or ((i==0 or i==3 or i==6) and (j!=5 and j!=6)) or (j==5 and (i==1 or i==2 or i==4 or i==5)):
                    print('*',end="")
                else:
                    print(' ',end="")
            print()
        print()
    elif a == 'e' or a == 'E':
        for i in range(7):
            for j in range(7):
                if (i==0 or i==3 or i==6 or j==0) and j!=6:
                    print('*',end="")
                else:
                    print(' ',end="")
            print()
        print()
    elif a == 'k' or a == 'K':
        for i in range(7):
            for j in range(7):
                if j==0 or ((i==0 or i==6) and j==4) or ((i==1 or i==5) and j==3) or ((i==2 or i==4) and j==2) or (i==3 and j==1):
                    print('*',end="")
                else:
                    print(' ',end="")
            print()
        print()
    else:
        print('Faqat harf kiriting.')
n=input('Biron bir harf kiriting: ')
harf(n)
sleep(5)
