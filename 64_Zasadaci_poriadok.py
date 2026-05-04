import tkinter
from random import shuffle
HEIGHT, WIDTH = 1000, 1000
canvas = tkinter.Canvas(height = HEIGHT, width = WIDTH)
canvas.pack()
subor = open('zasadaci_poriadok.csv', 'r', encoding='UTF-8')

zoznam = []
for riadok in subor:
    zoznam.append(riadok.strip())

shuffle(zoznam)
print(zoznam)

def lavica(x, y, meno, priezvisko, velkost):
    canvas.create_rectangle(x, y, x + velkost, y + velkost // 2)
    canvas.create_text(x + velkost // 2, y + velkost // 5, text = priezvisko, fill = 'red')
    canvas.create_text(x + velkost // 2, y + velkost // 3, text = meno, fill = 'blue')

def usad():
    pocet_ziakov = len(zoznam)
    pocet_r = int(pocet_radov.get())
    pocet_l = int(pocet_lavic.get())
    pocet_lavic_cislo = pocet_r * pocet_l
    if pocet_ziakov > pocet_lavic_cislo:
        canvas.create_text(WIDTH // 2, HEIGHT // 2, text = 'Mate malo lavic na usadenie studentov.', font = 'Arial 20', fill = 'red')
    else:
        x, y, velkost = 20, 20, 100
        for i in range(pocet_r):
            for j in range(pocet_l):
                if len(zoznam) > 0:
                    clovek = zoznam[-1]
                    bodkociarka = clovek.find(';')
                    meno = clovek[:bodkociarka]
                    priezvisko = clovek[bodkociarka + 1:]
                    zoznam.pop()
                    lavica(x, y, meno, priezvisko, velkost)
                else:
                    lavica(x, y, '', '', velkost)
                x += velkost * 1.2
            y += (velkost // 2) * 1.2
            x = 20

p_r_text = tkinter.Label(text = 'Pocet radov')
p_r_text.pack()
pocet_radov = tkinter.Entry()
pocet_radov.pack()
p_l_text = tkinter.Label(text = 'Pocet lavic')
p_l_text.pack()
pocet_lavic = tkinter.Entry()
pocet_lavic.pack()
potvrd = tkinter.Button(text = 'Potvrd vstup', command = usad)
potvrd.pack()
canvas.mainloop()