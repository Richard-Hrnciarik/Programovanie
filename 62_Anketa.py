import tkinter
WIDTH, HEIGHT = 500, 300
canvas = tkinter.Canvas(width = WIDTH, height = HEIGHT)
canvas.pack()

zoznam = []
otazka, odpovede, najviac = '', '', 'ano'

def citaj():
    global otazka, odpovede, zoznam
    subor = open('anketa.txt', 'r')
    otazka = subor.readline()
    odpovede = subor.readline()
    medzera = odpovede.find(' ')
    medzera2 = odpovede.rfind(' ')
    zoznam.append(int(odpovede[:medzera]))
    zoznam.append(int(odpovede[medzera + 1: medzera2]))
    zoznam.append(int(odpovede[medzera2 + 1:]))
    subor.close()
    porovnaj(int(zoznam[0]), int(zoznam[1]), int(zoznam[2]))

def porovnaj(ano, nie, neviem):
    global najviac
    najvacsie = ano
    if nie > najvacsie:
        najvacsie = nie
        if neviem > nie:
            najvacsie = neviem
            najviac = 'neviem'
        else:
            najviac = 'nie'
    elif neviem > najvacsie:
        if ano > neviem:
            najvacsie = ano
            najviac = 'ano'
        else:
            najvacsie = neviem
            najviac = 'neviem'
    else:
        najvacsie = ano
        najviac = 'ano'
    print(ano, nie, neviem, najvacsie)
    kresli(100, 50, otazka, int(zoznam[0]), int(zoznam[1]), int(zoznam[2]), najviac, int(zoznam[0]) + int(zoznam[1]) + int(zoznam[2]))
    
def kresli(x, y, otazka, ano, nie, neviem, najviac, spolu):
    canvas.delete('all')
    print(spolu)
    farba = 'red'
    canvas.create_text(WIDTH // 2, y - 30, text = otazka, tags = 'otazka')
    canvas.create_text(x, y, text = '1) Ano - ' + str(ano), tags = 'hlasovanie')
    if najviac == 'ano':
        farba = 'green'
    canvas.create_rectangle(x + 100, y - 10, x + 100 + spolu / 100 * ano, y + 10, fill = farba, tags = 'hlasovanie')
    y += 30
    farba = 'red'
    canvas.create_text(x, y, text = '1) Ano - ' + str(nie), tags = 'hlasovanie')
    if najviac == 'nie':
        farba = 'green'
    canvas.create_rectangle(x + 100, y - 10, x + 100 + spolu / 100 * nie, y + 10, fill = farba, tags = 'hlasovanie')
    farba = 'red'
    y += 30
    canvas.create_text(x, y, text = '1) Ano - ' + str(neviem), tags = 'hlasovanie')
    if najviac == 'neviem':
        farba = 'green'
    canvas.create_rectangle(x + 100, y - 10, x + 100 + spolu / 100 * neviem, y + 10, fill = farba, tags = 'hlasovanie')

def pridaj(event):
    if event.keysym == '1':
        zoznam[0] += 1
        zapis(event.keysym)
    elif event.keysym == '2':
        zoznam[1] += 1
        zapis(event.keysym)
    elif event.keysym == '3':
        zoznam[2] += 1
        zapis(event.keysym)

def zapis(hlas):
    subor = open('anketa.txt', 'w')
    subor.write(otazka)
    subor.write(str(zoznam[0]) + ' ' + str(zoznam[1]) + ' ' + str(zoznam[2]))
    subor.close()
    citaj()

citaj()

canvas.bind_all('<Key>', pridaj)
canvas.mainloop()