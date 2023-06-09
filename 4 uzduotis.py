from tkinter import *

def F_to_C():
    ivesta = laukas.get()
    celsius = (int(ivesta) - 32) * 5/9
    status["text"] = f'F to C rezultatas {celsius} C'

def C_to_F():
    ivesta = laukas.get()
    fahrenheit = int(ivesta) * 9/5 + 32
    status["text"] = f'C to F rezultatas {fahrenheit} F'

def isvalyti():
    laukas.delete(0, END)
    status.config(text=" ")
    status["text"] = "Ištrinta"

langas = Tk()


laukas = Entry(langas)
mygtukas1 = Button(langas, text="F to C", command= F_to_C, cursor="hand2")
mygtukas2 = Button(langas, text="C to F", command= C_to_F, cursor="hand2")
status = Label(langas, text = "", bd=1, relief=SUNKEN, anchor=W)

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)

meniu.add_cascade(label = "Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=quit)

langas.bind("<Escape>", lambda event: quit())

laukas.grid(row = 0, column = 0, sticky=EW)
mygtukas1.grid(row = 1, column=0,sticky=EW)
mygtukas2.grid(row = 2, column=0,sticky=EW)
status.grid(row=3, column=0, columnspan=2, sticky=EW)

langas.mainloop()