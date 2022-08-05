import tkinter

window = tkinter.Tk()
elemento = tkinter.StringVar()
listbox = tkinter.Listbox(window)

for item in ["Audi", "Seat", "Volvo", "Ferrari"]:
    listbox.insert(tkinter.END, item)

listbox.pack()

label = tkinter.Label(text="Lista de nombres de autos")
label.pack()

window.mainloop()
