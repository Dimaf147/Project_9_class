from pathlib import Path
from tkinter import Tk, Button, Label
import config


def create_window():
    window = Tk()  # Создание окна
    window.geometry("420x420")  # Задаём размер окна
    window.title("Settings")
    window.config(background="grey")

    button = Button(window, text="Receipt recognition")
    button.config(font=(50))
    button.place(relx=0.5, rely=0.45, anchor="center")

    label = Label(window, text="From the folder with receipts", background="grey", fg="black")
    label.config(font=(20))
    label.place(relx=0.5, rely=0.55, anchor="center")

    window.mainloop()  # Вывод окна


if __name__ == "__main__":
    create_window(config)
