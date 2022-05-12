from tkinter import *
window=Tk()
window.title("Pokémon Red")
window.geometry("1024x768")
window.iconbitmap("Pokemon/image pokeball.ico")

#label_title=Label(window,text="Pokémon",font=("PokemonNormal",40),bg="DarkBlue")
#label_title.place(x=100,y=100)

w=1024
h=768

image = PhotoImage(file='Red_Project/image/image menu pokemon red.png', master=window)
canvas = Canvas(window, width=w, height=h)
canvas.pack()
canvas.create_image((w//2, h//2), image=image)


Button_start=Button()

window.mainloop()

