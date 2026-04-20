import tkinter
canvas = tkinter.Canvas(height = 800, width = 800)
canvas.pack()

subor = open('kresliaci_robot2.txt', 'r')
smer = 0
x, y = 400, 400
def ciara():
    if smer == 0:
        canvas.create_line(x, y, x, y - 50)
    elif smer == 180:
        canvas.create_line(x, y, x, y + 50)
    elif smer == 90:
        canvas.create_line(x, y, x - 50, y)
    else:
        canvas.create_line(x, y, x + 50, y)

def vlavo():
    global smer
    if smer > 90:
        smer -= 90
    else:
        smer = 270

def vpravo():
    global smer
    if smer < 270:
        smer += 90
    else:
        smer = 0

opakovanie = False
pamet = []
pocet = 0
for riadok in subor:
    if 'opakuj' in riadok:
        opakovanie == True
        medzera = riadok.find(' ')
        pocet = riadok.strip()[medzera + 1:]
        print('preslo')
    if 'koniecopakuj' in riadok:
        opakovanie = False
    if opakovanie == True:
        if riadok.strip() == 'ciara':
            pamet.append('ciara')
        elif riadok.strip() == 'vlavo':
            pamet.append('vlavo')
        elif riadok.strip() == 'vpravo':
            pamet.append('vpravo')
    else:
        if len(pocet) > 0:
            for i in range(len(pocet)):
                if pamet[i] == 'ciara':
                    ciara()
                elif pamet[i] == 'vlavo':
                    vlavo()
                elif pamet[i] == 'vpravo':
                    vpravo()
            pocet = 0
            pamet = []
        if riadok.strip() == 'ciara':
            ciara()
        elif riadok.strip() == 'vlavo':
            vlavo()
        elif riadok.strip() == 'vpravo':
            vpravo()

subor.close()
canvas.mainloop()