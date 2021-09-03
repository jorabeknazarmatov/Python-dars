import os
def html(file,html,css):
    n='\n'
    p='    '
    s1='{'
    s2='}'
    os.sys
    os.mkdir(file)
    with open(html,"w") as c:
        c.write(f'<!DOCTYPE html>{n}')
        c.write(f'<html lang="ru">{n}')
        c.write(f'<head>{n}')
        c.write(f'{p}<meta charset="utf-8">{n}')
        c.write(f'{p}<link rel="stylesheet" href="main.css">{n}')
        c.write(f'{p}<title>Birinchi sayt</title>{n}')
        c.write(f'{p}<script>alert("JavaScript ham ishlayapti.")</script>{n}')
        c.write(f'</head>{n}')
        c.write(f'<body>{n}')
        c.write(f'{p}<h1>Python bilan yaratilgan birinchi saytimiz !!!</h1>{n}')
        c.write(f'</body>{n}')
        c.write(f'</html>')
        c.close()
    with open(css,"w") as z:
        z.write(f'body{s1}{n}{p}background: #EEFFF9;{n}{s2}{n}')
        z.write(f'h1{s1}{n}{p}text-align: center;{n}{p}color: #EEEEEE;{n}{p}transition: 1s;{n}{s2}{n}')
        z.write(f'h1:hover{s1}{n}{p}color: red;{n}{p}font-size: 72px;{n}{p}transition: 3s;{n}{s2}{n}')
        z.close()
html('C:/Users/User/Desktop/test','C:/Users/User/Desktop/test/index.html','C:/Users/User/Desktop/test/main.css')
print('Ekranga test papka yaratildi va uning ichiga\n index.html va main.css joylandi.\nTekshirib ko`ring.\nBularning hammasi Python dasturlash tilida yozilgan.')
print('\nhtml() funksiyasi 3 ta argument qabul qiladi.\n1 - yangi papka manzili.\n2 - html fayl manzili\n3 - css fayl manzili.\n')
print('Istasangiz html() ni chaqirib boshqa manzil berishingiz mumkin.')
