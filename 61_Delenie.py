import tkinter
from random import randint
canvas = tkinter.Canvas(width = 800, height = 300)
canvas.pack()

vysledok, zvysok, delenec, delitel = 0, 0, 0, 0
def priklad(x, y):
    global vysledok, zvysok, delenec, delitel
    delenec = randint(11, 20)
    delitel = randint(2, 9)
    vysledok = delenec // delitel
    zvysok = delenec % delitel
    canvas.create_text(x, y, text = str(delenec) + ' : ' + str(delitel) + ' =', font = 'Arial 20')

def over():
    zadane = int(entry.get())
    if zadane == vysledok:
        canvas.create_text(90, 60, text = 'SPRAVNE', font = 'Arial 20')
    else:
        canvas.create_text(90, 60, text = 'NESPRAVNE', font = 'Arial 20')
    vygulickuj()

farba = ['green', 'blue', 'red', 'yellow', 'orange', 'brown', 'purple', 'pink', 'lime_green', 'cyan']
def vygulickuj():
    farba_i = 0
    x = 20
    for i in range(vysledok):
        for j in range(delitel):
            canvas.create_oval(x, 120, x + 15, 135, fill = farba[farba_i])
            x += 20
        farba_i += 1
    x += 40
    farba_i += 1
    for k in range(delenec % delitel):
        canvas.create_oval(x, 120, x + 15, 135, fill = farba[farba_i + 1])
        x += 20
    
priklad(80, 30)

entry = tkinter.Entry()
entry.pack()
button = tkinter.Button(text = 'Over', command = over)
button.pack()
canvas.mainloop()