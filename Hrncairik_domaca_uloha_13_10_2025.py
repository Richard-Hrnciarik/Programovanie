import tkinter as tk

def otvor_canvas2():
    #vytvori nove okno
    okno2 = tk.Toplevel(root)
    okno2.title('Canvas 2')

    frame = tk.Frame(okno2)
    frame.pack(fill = 'both', expand = True)

    #vytvori novy canvas v tomto okne
    canvas2 = tk.Canvas(frame, width = 400, height = 300, bg = 'lightyellow', scrollregion = (0, 0, 800,  1200))
    canvas2.pack(side = 'left', fill = 'both', expand = True)
    '''
    #vertikalny scrollbar
    v_scroll = tk.Scrollbar(frame, orient = 'vertical', command = canvas2.yview)
    v_scroll.pack(side = 'right', fill = 'y')

    #horizontalny scrollbar
    h_scroll = tk.Scrollbar(okno2, orient = 'horizontal', command = canvas2.xview)
    h_scroll.pack(side = 'bottom', fill = 'x')

    #prepojenie canvasu so scrollbarmi
    canvas2.configure(yscrollcommand = v_scroll.set, xscrollcommand = h_scroll.set)

    #nieco nan nakreslime
    rx, ry = 200, 100
    x, y = 300, 200

    canvas2.create_oval(x-rx, y-ry, x+rx, y+ry, width=5, outline='green',tags='oval')

    def zmena1(event):
        global rx
        rx = scale1.get()
        prekresli()

    def zmena2(event):
        global ry
        ry = scale2.get()
        prekresli()

    def prekresli():
        canvas2.coords('oval',[x-rx, y-ry, x+rx, y+ry])

    scale1 = tk.Scale(from_=10, to=200, orient='horizontal',length=600, command=zmena1)
    scale1.pack()
    scale1.set(rx)

    scale2 = tk.Scale(from_=10, to=200, orient='vertical',length=400, command=zmena2)
    scale2.place(x=550, y=0)
    scale2.set(ry)'''

    def kruh():
        global rx, ry, x, y
        rx, ry = 200, 100
        x, y = 300, 200

    kruh()

    canvas2.create_oval(x-rx, y-ry, x+rx, y+ry, width=5, outline='green',tags='oval')

    def zmena1(event):
        global rx
        rx = scale1.get()
        prekresli()

    def zmena2(event):
        global ry
        ry = scale2.get()
        prekresli()

    def prekresli():
        canvas2.coords('oval',[x-rx, y-ry, x+rx, y+ry])

    scale1 = tk.Scale(frame, from_=10, to=200, orient='horizontal',length=600, command=zmena1)
    scale1.pack()
    scale1.set(rx)

    scale2 = tk.Scale(frame, from_=10, to=200, orient='vertical',length=400, command=zmena2)
    scale2.place(x=550, y=0)
    scale2.set(ry)

#--------------------------------------------------------------------------------------------

def otvor_canvas3():
    #vytvori nove okno
    okno3 = tk.Toplevel(root)
    okno3.title('Canvas 3')

    #vytvori novy canvas v tomto okne
    canvas3 = tk.Canvas(okno3, width = 400, height = 600, bg = 'lightyellow')
    canvas3.pack(padx = 10, pady = 10)

    def stvorec():
        v = tk.IntVar()

        radiobutton1 = tk.Radiobutton(text='kruh', variable=v, value=1)
        radiobutton1.pack()

        radiobutton2 = tk.Radiobutton(text='štvorec', variable=v, value=2)
        radiobutton2.pack()

        radiobutton3 = tk.Radiobutton(text='čiara', variable=v, value=3)
        radiobutton3.pack()

        radiobutton4 = tk.Radiobutton(text='text', variable=v, value=4)
        radiobutton4.pack()

    stvorec()

#--------------------------------------------------------------------------------------------

def otvor_canvas4():
    #vytvori nove okno
    okno4 = tk.Toplevel(root)
    okno4.title('Canvas 4')

    frame = tk.Frame(okno4)
    frame.pack(fill = 'both', expand = True)

    #vytvori novy canvas v tomto okne
    canvas4 = tk.Canvas(frame, width = 400, height = 300, bg = 'lightyellow', scrollregion = (0, 0, 800,  1200))
    canvas4.pack(side = 'left', fill = 'both', expand = True)

    v = tk.IntVar()

    radiobutton1 = tk.Radiobutton(frame, text='kruh', variable=v, value=1)
    radiobutton1.pack()

    radiobutton2 = tk.Radiobutton(frame, text='štvorec', variable=v, value=2)
    radiobutton2.pack()

    radiobutton3 = tk.Radiobutton(frame, text='čiara', variable=v, value=3)
    radiobutton3.pack()

    radiobutton4 = tk.Radiobutton(frame, text='text', variable=v, value=4)
    radiobutton4.pack()

    '''def klik(sur):
        typ = v.get()
        if typ == 1:
            canvas4.create_oval(sur.x-10, sur.y-10, sur.x+10, sur.y+10)
        if typ == 2:
            canvas4.create_rectangle(sur.x-10, sur.y-10, sur.x+10, sur.y+10)
        if typ == 3:
            canvas4.create_line(sur.x-10, sur.y, sur.x+10, sur.y)
        if typ == 4:
            canvas4.create_text(sur.x, sur.y, text='['+str(sur.x)+','+str(sur.y)+']')

    def prefarbi(event):
        oznacene = listbox1.curselection()
        canvas4['bg'] = listbox1.get(oznacene)

    def pridaj():
        listbox1.insert('end', entry1.get())

    def vymaz():
        oznacene = listbox1.curselection()
        if len(oznacene) == 1:
            listbox1.delete(oznacene)

    listbox1 = tk.Listbox()
    listbox1.pack()

    farby = ['red', 'green', 'blue', 'orange', 'yellow', 'white']

    for prvok in farby:
        listbox1.insert('end', prvok)

    listbox1.bind('<Double-Button-1>', prefarbi)

    label1 = tk.Label(text='Napíš názov farby:')
    label1.pack()
    entry1 = tk.Entry()
    entry1.pack()
    button1 = tk.Button(text='Pridaj farbu', command=pridaj)
    button1.pack()
    button2 = tk.Button(text='Vymaž označenú farbu', command=vymaz)
    button2.pack()
    
    text1 = tk.Text(height=5, width=30)
    text1.pack(side='left')

    scrollbar1 = tk.Scrollbar()
    scrollbar1.pack(side='right', fill='y')

    #vyplní s ním celý voľný priestor v rozsahu osi y
    scrollbar1.config(command=text1.yview)

    #po posunutí sa posunie aj obsah text1
    text1.config(yscrollcommand=scrollbar1.set)

    #po posunutí obsahu text1 sa posunie aj scrollbar1
    f = open('score.txt', 'r')

    for riadok in f:
        text1.insert('end', riadok)
    f.close()
    
    def vypis():
        predmety = predmet1.get() + ' ' + predmet2.get() + ' ' + predmet3.get()
        predmety = predmety.strip()
        print('Práve máte vybraté predmety:', predmety)

    label1 = tk.Label(text='Z ktorého predmetu idete maturovať?')
    label1.pack()

    predmet1 = tk.StringVar()
    checkbutton1 = tk.Checkbutton(text='slovenský jazyk a literatúra',onvalue='SJL', offvalue='', variable=predmet1,command=vypis)
    checkbutton1.pack(anchor='w')

    predmet2 = tk.StringVar()
    checkbutton2 = tk.Checkbutton(text='anglický jazyk', onvalue='AJ',offvalue='', variable=predmet2, command=vypis)
    checkbutton2.pack(anchor='w')

    predmet3 = tk.StringVar()
    checkbutton3 = tk.Checkbutton(text='nemecký jazyk', onvalue='NJ',offvalue='', variable=predmet3, command=vypis)
    checkbutton3.pack(anchor='w')

    canvas4.bind('<Button-1>', klik)'''

#--------------------------------------------------------------------------------------------

def otvor_canvas5():
    #vytvori nove okno
    okno5 = tk.Toplevel(root)
    okno5.title('Canvas 5')

    #vytvori novy canvas v tomto okne
    canvas5 = tk.Canvas(okno5, width = 400, height = 300, bg = 'lightyellow')
    canvas5.pack(padx = 10, pady = 10)

    def otvor():
        pass

    def uloz():
        pass

    def oprograme():
        text1.place(x=100, y=100)
        button1.place(x=300, y=200)

    def oprograme_zatvor():
        text1.place_forget()
        button1.place_forget()

    menu1 = tk.Menu(root)
    root.config(menu=menu1)

    menu2 = tk.Menu(menu1)
    menu2.add_command(label='Otvoriť', command=otvor)
    menu2.add_command(label='Uložiť', command=uloz)
    menu2.add_separator()
    menu2.add_command(label='Skončiť', command=root.destroy) # alebo quit

    menu1.add_cascade(label='Súbor', menu=menu2)

    menu3 = tk.Menu(menu2)
    menu3.add_command(label='O programe', command=oprograme)

    menu1.add_cascade(label='Pomocník', menu=menu3)

    text1 = tk.Text(height=5, width=42)
    text1.insert('end', 'O programe\ntoto je program na ukážku používania menu\nverzia 1.0')
    text1.config(state='disabled')
    button1 = tk.Button(text='Zatvor', command=oprograme_zatvor)

#--------------------------------------------------------------------------------------------

def otvor_canvas6():
    #vytvori nove okno
    okno6 = tk.Toplevel(root)
    okno6.title('Canvas 6')

    #vytvori novy canvas v tomto okne
    canvas6 = tk.Canvas(okno6, width = 400, height = 300, bg = 'lightyellow')
    canvas6.pack(padx = 10, pady = 10)

    def oznam():
        vysledok = tk.messagebox.showinfo('oznam', 'stlačili ste tlačidlo')
        print(vysledok)

    def otazka1():
        vysledok = tk.messagebox.askyesno('Pokračovanie', 'Chcete pokračovať?')
        print(vysledok)

    def otazka2():
        vysledok = tk.messagebox.askyesnocancel('Pokračovanie','Chcete pokračovať?')
        print(vysledok)

    button1 = tk.Button(text='zobraz oznam', command=oznam)
    button1.pack()

    button2 = tk.Button(text='otazka 1', command=otazka1)
    button2.pack()

    button3 = tk.Button(text='otazka 2', command=otazka2)
    button3.pack()

#--------------------------------------------------------------------------------------------

def otvor_canvas7():
    #vytvori nove okno
    okno7 = tk.Toplevel(root)
    okno7.title('Canvas 7')

    #vytvori novy canvas v tomto okne
    canvas7 = tk.Canvas(okno7, width = 400, height = 300, bg = 'lightyellow')
    canvas7.pack(padx = 10, pady = 10)

    def nacitaj():
        info = tk.filedialog.askopenfile()
        if info != None:
            print('Meno súboru:' + info.name)
            print('Kódovanie znakov:' + info.encoding)
            subor = open(info.name, 'r', encoding=info.encoding)
            obsah = subor.read()
            subor.close()
            text1.delete(1.0, 'end')
            text1.insert('end', obsah)

    def farba():
        farba = tk.colorchooser.askcolor()
        print(farba)
        cislo_farby = farba[1]
        if cislo_farby != None:
            canvas7['bg'] = cislo_farby
            print('zmenil som farbu na:', cislo_farby)
        else:
            print('farba nebola zmenená')

    text1 = tk.Text(width=60, height=10)
    text1.pack()

    button1 = tk.Button(text='otvor súbor', command=nacitaj)
    button1.pack()
    button2 = tk.Button(text='vyber farbu', command=farba)
    button2.pack()

#--------------------------------------------------------------------------------------------



#hlavne okno
root = tk.Tk()
root.title('Hlavne okno')

#vytvorime menu
menu_bar = tk.Menu(root)
root.config(menu = menu_bar)

#pridame menu polozku 'Zobrazit'
zobrazenie_menu = tk.Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = 'Zobrazit', menu = zobrazenie_menu)

#polozka, ktora prida nove okno s Canvasom
zobrazenie_menu.add_command(label = 'Canvas 2', command = otvor_canvas2)
zobrazenie_menu.add_command(label = 'Canvas 3', command = otvor_canvas3)
zobrazenie_menu.add_command(label = 'Canvas 4', command = otvor_canvas4)
zobrazenie_menu.add_command(label = 'Canvas 5', command = otvor_canvas5)
zobrazenie_menu.add_command(label = 'Canvas 6', command = otvor_canvas6)
zobrazenie_menu.add_command(label = 'Canvas 7', command = otvor_canvas7)

#hlavny canvas v hlavnom okne
canvas1 = tk.Canvas(root, width = 400, height = 300, bg = 'white')
canvas1.pack(padx = 10, pady = 10)
canvas1.create_rectangle(50, 50, 200, 200, fill = 'lightblue', outline = 'blue')
canvas1.create_text(200, 250, text = 'Toto je Canvas 1', font = 'Arail 14 bold')

canvas1.mainloop()