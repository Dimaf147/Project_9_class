from tkinter import *

window = Tk() # Создание окна
window.geometry("420x420") # Задаём размер окна
window.title("Settings")
window.config(background="black")

button = Button(window, text = "Upload photo")
button.config(font=(50))
button.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()  # Вывод окна

