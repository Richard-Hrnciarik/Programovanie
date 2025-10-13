import tkinter
from random import *
canvas = tkinter.Canvas(height = 600, width = 1200, bg = 'purple')
canvas.pack()

vstup_x = open('x.txt', 'r')
vstup_y = open('y.txt', 'r')

for riadok in vstup_x:
    x = riadok
    y = vstup_y.readline()
    canvas.create_oval(int(x) - 5, int(y) -5, int(x) + 5, int(y) + 5, outline = 'white')

canvas.mainloop()
