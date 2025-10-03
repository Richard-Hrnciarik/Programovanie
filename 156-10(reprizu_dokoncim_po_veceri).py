import tkinter
from random import *
pocet_zapaliek = int(input('Zadaj počet zápaliek: ')) #input cez konzolu na pocet zapaliek
WIDTH = pocet_zapaliek * 145 + 90 #sirka canvasu (velkost zapalky, ktoru som pouzil bola 145 px na sirku, pri inom obrazku treba zmenit)
HEIGHT = 1000
canvas = tkinter.Canvas(height = HEIGHT, width = WIDTH)
canvas.pack()

zapalka = tkinter.PhotoImage(file = 'zapalka.png') #nacita zapalku
hrac = 1 #aktivny hrac
pocet_klikov = 0
mazanie = [False] * pocet_zapaliek #ntica s tym, ktore zapalky su este v hre

def zapalky(): #kreslenie zapaliek
    for i in range(pocet_zapaliek): #opakuj kolko je zapaliek
        canvas.create_image(i * 145 + 90, 500, image = zapalka, tags = str(i)) #1 zapalka
    canvas.create_text(WIDTH / 2, 50, text = 'Na rade je hrač ' + str(hrac) + '.' , tags = 'text', font = 'Arial 20 bold') #text - na rade je hrac - vykona sa raz na zaciatku

def dalsi(): #2. hrac
    global hrac, pocet_klikov
    if pocet_klikov != 0: #len pokial aspon raz klikol
        if hrac == 1: #z hraca 1 na hraca 2
            hrac = 2
            pocet_klikov = 0 #reset klikov
        else:
            hrac = 1 #z hraca 2 na hraca 1
            pocet_klikov = 0 #reset klikov
        canvas.delete('text') #vymaze text
        canvas.create_text(WIDTH / 2, 50, text = 'Na rade je hrač ' + str(hrac) + '.' , tags = 'text', font = 'Arial 20 bold') #novy text
    else: #ak hrac neklikol ani raz - upozornenie
        canvas.delete('text')
        canvas.create_text(WIDTH / 2, 50, text = 'Na rade je hrač ' + str(hrac) + '. \n Musí spraviť aspoň 1 ťah.' , tags = 'text', font = 'Arial 20 bold')

def klik(suradnice): #klikanie
    global pocet_klikov, mazanie
    x = suradnice.x
    y = suradnice.y
    if 200 < y < 800: #orezanie na zapalky (opat napresno podla velkosti obrazku zapalky)
        for i in range(10, WIDTH - 10, 145): #system na porovnavanie kliknutia a aktualnej zapalky
            if i < x:
                najblizsie = i #najblizsie zhoda = spravna zapalka
        if mazanie[(najblizsie + 135) // 145 - 1] != True: #ak este nebola zakliknuta
            canvas.delete(str((najblizsie + 135) // 145))
            mazanie[(najblizsie + 135) // 145 - 1] = True #prepis hodnoty v ntici
            pocet_klikov += 1
        if mazanie == [True] * pocet_zapaliek: #overenie vyhry
            canvas.delete('all')
            canvas.create_text(WIDTH / 2, 500, text = 'Vyhral hrač ' + str(hrac), font = 'Arial 80 bold')
        if pocet_klikov >= 3: #ak hrac pouzil vsetky kliky
            dalsi() #zmeni hraca

def repriza():
    canvas.delete('all')
    zapalky()
    for i in range(pocet_zapaliek):
        canvas.after(500)
        #canvas.delete()

button_dalsi = tkinter.Button(text = 'dalsi', command = dalsi, font = 'Arial 20 bold') #button na manualne posunutie na dalsieho hraca (ak nechcete pouzit vsetky 3 tahy)
button_dalsi.place(x = WIDTH / 1.3, y = 900)
button_repriza = tkinter.Button(text = 'Repríza', command = repriza, font = 'Arial 20 bold') #button na reprizu
button_repriza.place(x = WIDTH / 6, y = 900)
canvas.bind('<Button-1>', klik) #klikanie
zapalky()

canvas.mainloop()