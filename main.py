import random
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import filedialog as fd
from config import symbols

# создаём переменную пути файла сохранения паролей
global file_path
file_path = "q"

# создаём функцию записи пути файла
def zapis_puti():
    global file_path
    file_path = fd.askopenfilename()

# создаём функцию вывода информации о программе
def info():
    messagebox.showinfo("Password generation", "This program generates a random password of a user-specified length and writes the resulting data to a .txt file.\nYou can select a save file when creating a password and change it at any time in the corresponding menu section.\n\nVersion: 1.1\nDevelopped by: ihateyourCode")

# создаём функцию обработки нажатия кнопки для проверки заполненных полей
def click_check():
    name_of_site = txt1.get()
    password_length = txt2.get()
    if name_of_site == "":
        messagebox.showinfo('Password Generation', 'Вы не ввели данные!')
    elif password_length == "":
        messagebox.showinfo('Password Generation', 'Вы не ввели данные!')
    else: click()

#создаём функцию генерирования пароля
def click():
    # обрабатываем полученные данные и рандомим пароль
    name_of_site = txt1.get()
    password_length = int(txt2.get())
    password = "".join(random.sample(symbols, password_length))

    # визуализируем процесс генерации
    lbl3 = Label(window, text="Идёт генерация пароля, пожалуйста подождите", bg="gray", fg="white", font=("Arial", 12))
    lbl3.place(x=0, y=150)
    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='green')
    bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
    bar['value'] = 0
    bar.place(x=0, y=170)
    while bar['value'] <= 100:
        bar['value'] += 10
        bar.update()
        time.sleep(0.3)
    bar.destroy()
    lbl3.configure(text="Ваш пароль готов!")
    lbl3.update()
    time.sleep(1)

    # запускаем диалоговое окно
    msg = messagebox.askquestion('Password Generation', f'Сайт: {name_of_site}\nВаш пароль: {password} \n\nСохранить пароль?')
    if msg == 'yes':
        global file_path
        if file_path == "q":
            file_path = fd.askopenfilename()
        else: pass
        file1 = open(file_path, "a", encoding = "utf-8")
        file1.write(f'Сайт: {name_of_site}\nПароль: {password}\n\n')
        file1.close()
        messagebox.showinfo("Password generation", f"Пароль для сайта {name_of_site} успешно сохранён!")
        lbl3.destroy()
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt1.focus()
    elif msg == 'no':
        lbl3.destroy()
        txt1.delete(0, END)
        txt2.delete(0, END)
        txt1.focus()

# создаём окно приложения
window = Tk()
window.geometry("400x400")
window.title("Password Generation")
window.resizable(width=False, height = False)

# создаём фон приложения
filename = PhotoImage(file = "images/111.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# создаём текстовое и вводное окно для названия сайта
lbl1 = Label(window, text="Введите название сайта:", bg= "gray", fg = "white", font=("Arial", 16))
lbl1.place(x = 0, y = 0)
txt1 = Entry(window,  highlightbackground="grey",width=20)
txt1.place(x = 0, y = 25)

# создаём текстовое и вводное окно для длины пароля
lbl2 = Label(window, text="Введите длину пароля:", bg= "gray", fg = "white", font=("Arial",16))
lbl2.place(x = 0, y = 55)
txt2 = Entry(window,  highlightbackground="grey",width=20)
txt2.place(x = 0, y = 80)

# создаём кнопку генерации пароля
btn1 = Button(window, text="Получить пароль", highlightbackground="grey", fg="black", command = click_check)
btn1.place(x= 0,y= 110)

# создаём меню
main_menu = Menu(window)
window.config(menu=main_menu)
filemenu = Menu(main_menu, tearoff=0)
filemenu.add_command(label="Сохранять пароли в...", command = zapis_puti)
helpmenu = Menu(main_menu, tearoff=0)
helpmenu.add_command(label="О программе", command = info)

main_menu.add_cascade(label="Файл", menu=filemenu)
main_menu.add_cascade(label="Справка", menu=helpmenu)

window.mainloop()
