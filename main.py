from cProfile import label
from pathlib import Path
from tkinter import Tk, Button, Label
import config

count = 0


def path_with_file():
    folder = Path(config.TARGET_FOLDER)
    png_files = [p for p in folder.glob("*")]

    print("Путь к файлам:")
    c = 0
    for file in png_files:
        c += 1
        print(file.resolve())
    return c

def create_window():
    global count

    window = Tk()  # Создание окна
    window.geometry("420x420")  # Задаём размер окна
    window.title("Settings")
    window.config(background="grey")

    def click():
            label1.config(text=max_files)

    button = Button(window, text="Receipt recognition")
    button.config(font=(50))
    button.place(relx=0.5, rely=0.45, anchor="center")
    button.config(command=click)

    label = Label(window, text="From the folder with receipts", background="grey", fg="black")
    label.config(font=(20))
    label.place(relx=0.5, rely=0.55, anchor="center")

    label1 = Label(window, text=count)
    label1.config(font=("Monospace", 50))
    label1.config(background="grey")
    label1.pack()


    window.mainloop()  # Вывод окна




if __name__ == "__main__":
    max_files = path_with_file()
    create_window()

