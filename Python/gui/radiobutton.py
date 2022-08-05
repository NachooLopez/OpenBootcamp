import tkinter


def main():
    def seleccion():
        monitor.config(text='{}'.format(opcion.get()))

    def reiniciar():
        opcion.set(None)
        monitor.config(text="")

    window = tkinter.Tk()
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)

    opcion = tkinter.StringVar()
    opcion.set(None)
    r1 = tkinter.Radiobutton(window, text='Seat', value='Seat',
                             variable=opcion, command=seleccion)
    r2 = tkinter.Radiobutton(window, text='Volvo', value='Volvo',
                             variable=opcion, command=seleccion)
    r3 = tkinter.Radiobutton(window, text='Audi', value='Audi',
                             variable=opcion, command=seleccion)
    r4 = tkinter.Radiobutton(window, text='Dacia', value='Dacia',
                             variable=opcion, command=seleccion)

    r1.grid(column=0, row=1, pady=5, padx=5)
    r2.grid(column=0, row=2, pady=5, padx=5)
    r3.grid(column=0, row=3, pady=5, padx=5)
    r4.grid(column=0, row=4, pady=5, padx=5)

    monitor = tkinter.Label(window)
    monitor.grid(column=0, row=9, pady=7, padx=7)
    boton = tkinter.Button(window, text='Reiniciar', command=reiniciar)
    boton.grid(column=0, row=8, pady=7, padx=7)

    window.mainloop()


if __name__ == "__main__":
    main()
