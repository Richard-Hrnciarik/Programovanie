import tkinter
from random import *
canvas = tkinter.Canvas(height = 800, width = 1100, bg = 'black')
canvas.pack()

hodnoty = [] #ntica na vysku stlpcov
vysky = ['31', '62', '125', '250', '500', '1k', '2k', '4k', '8k', '16k', 'Hz'] #popisy

#generovanie random vysok do ntice
def random_hodnoty(): 
    global hodnoty
    canvas.delete('all') #zmaze stary graf
    hodnoty = [] #vyprazdni nticu
    for i in range(10): #10 hodnot
        hodnota = randint(0, 700) #nahodna hodnota on 0 do 700
        hodnoty.insert(i, hodnota) #zapise hodnotu do ntice
    vykresli() #spusti definiciu vykresli

#kreslenie
def vykresli():
    global hodnoty
    for i in range(len(hodnoty)): #opakuj podla poctu hodnot
        canvas.create_rectangle(i * 100 + 30, 700, i * 100 + 80, 700 - hodnoty[i], fill = 'green', outline = '') #stlpce kreslenie
        canvas.create_text(i * 100 + 55, 750, text = vysky[i], fill = 'green', font = 'Arial 20 bold') #text kreslenie
    canvas.create_text((i + 1) * 100 + 55, 750, text = vysky[i + 1], fill = 'green', font = 'Arial 20 bold') #posledny text - hz
    canvas.update() #aktualizacia grafickeho pola
    canvas.after(1000, random_hodnoty) #kazdu sekundu spusti proces znovu

random_hodnoty() #spustenie
canvas.mainloop()