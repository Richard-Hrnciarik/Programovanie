import tkinter
from random import choice
subor = open('lodicky.txt', 'r')
prvy = subor.readline().strip()
medzera = prvy.find(' ')
mierka = 100
canvas = tkinter.Canvas(width = int(prvy[:medzera]) * mierka, height = int(prvy[medzera + 1:]) * mierka)
canvas.pack()

def stvorcek(x, y, mierka, farba):
    canvas.create_rectangle(x, y, x + mierka, y + mierka, fill = farba, outline = '')

def lodicka(x, y, mierka, farba):
    canvas.create_rectangle(x, y, x + mierka * 3, y + mierka, fill = farba)

def kresli_lodicku():
    if miesta != []: 
        poloha = choice(miesta)
        print(poloha)
        lodicka(poloha[0], poloha[1], mierka, 'yellow')
        miesta.remove(poloha)
    else:
        canvas.create_text((int(prvy[:medzera]) * mierka) // 2, (int(prvy[medzera + 1:]) * mierka) // 2, text = 'PRISTAV JE PLNY', font = 'Arial 30 bold')

y = 0
volne = 0
miesta = []
for riadok in subor:
    if volne == 3:
        miesta.append([x - mierka * 3, y - mierka])
    volne = 0
    x = 0
    for znak in riadok.strip().split():
        print(x, y, volne, miesta)
        if int(znak) == 1:
            if volne == 3:
                miesta.append([x - mierka * 3, y])
            elif volne == 4:
                miesta.append([x - mierka * 4, y])
            farba = 'grey'
            volne = 0
        else:
            farba = 'lightblue'
            if volne < 4:
                volne += 1
            else:
                volne = 1
                miesta.append([x - mierka * 4, y])
        stvorcek(x, y, mierka, farba)
        x += mierka
    y += mierka

print(miesta)
button = tkinter.Button(text = 'Pridaj lodku', command = kresli_lodicku)
button.pack()

subor.close()
canvas.mainloop()