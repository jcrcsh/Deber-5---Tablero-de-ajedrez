from tkinter import *
ventana = Tk()
ventana.geometry("1000x1000+100+100")
ventana.title("Tablero de ajedrez")
for i in range(7): //0, 1, 2, 3, 4, 5, 6, 7
    for j in range(7):
        b = Button(ventana, text = "A 1", heigh = 10, width = 10).place(x = i * 20, y = j * 20)
