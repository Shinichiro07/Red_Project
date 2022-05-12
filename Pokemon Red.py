#Pokemon Red

from tkinter import *
import time
from os import read
from random import randint

window= Tk()
window.title("Pokemon Red")
window.geometry("1024x768")
window.config(background= "#0D0D0D")
screen= Canvas(window, width= 1024, height= 768, bg= "#0D0D0D")

MX= 0
MY= 0
direction= 0

screen.place(x= 0 , y= 0)


def mouvLeft(event):
    global direction
    direction= 1

def mouvRight(event):
    global direction
    direction= 2
               
def mouvUp(event):
    global direction
    direction= 3
    

def mouvDown(event):
    global direction
    direction= 4
    

def mouvement():
    global map1, direction, MY, MX

    if direction == 4:
        MY= MY - 10
    
    if direction == 1:
        MX= MX - 10
    
    if direction == 3:
        MY= MY + 10
    
    if direction == 2:
        MX= MX + 10    
    
    screen.delete(map1)
    map1= screen.create_image(MX, MY, image= mapDefinition, anchor= NW)
    redNormalSprite= screen.create_image(450, 500, image= redDefinition, anchor= NW)
    
    window.after(1, mouvement)




mapDefinition= PhotoImage(file= r"C:\Users\adrien\Desktop\Projet-Pokemon\map\Map.png")
mapDefinition= mapDefinition.zoom(4)

map1= screen.create_image(0, 0, image= mapDefinition, anchor= NW)

redDefinition= PhotoImage(file= r"C:\Users\adrien\Desktop\Projet-Pokemon\Sprite\Sprite RED bas_normal.png")
redDefinition= redDefinition.subsample(8, 8)


window.bind("<q>", mouvLeft)
window.bind("<d>", mouvRight)
window.bind("<z>", mouvUp)
window.bind("<s>", mouvDown)


mouvement()

mainloop()

#salut seb