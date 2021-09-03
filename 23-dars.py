from time import sleep
from typing_extensions import TypeVarTuple

class Person:
    def __init__ (self, name):
        self.name = name
        '''
        self.l_name = l_name
        self.age = age

n = input('Ism : ')
m = input('Familiya : ')
x = int(input('Yosh : '))
'''
talaba = Person('Farrux')
print(talaba.name)
sleep(5)
