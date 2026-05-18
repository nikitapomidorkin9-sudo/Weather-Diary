from tkinter import *
import json
from datetime import datetime

window = Tk()
window.title("Приложение погода")
window.geometry("1200x800")
window.configure(bg="#f0f0f0")

list = []


def add_item():
    global list
    try:
        date = date_entry.get()
        temp = int(temp_entry.get())
        desk = desk_entry.get()
        osadki = osadki_entry.get()

        if date and temp and desk and osadki:
            item = f"{date} | {str(temp)} | {desk} | {osadki}"
            list.append(item)
            update_lb()
            date_entry.delete(0, END)
            temp_entry.delete(0, END)
            desk_entry.delete(0, END)
            osadki_entry.delete(0, END)
            res.config(text="Запись добавлена!", fg="green")
        else:
            res.config(text="Заполните все поля!!!", fg="red")
            return
    except ValueError:
        res.config(text="Температура должно быть числом!", fg="red")
        return


def update_lb():
    global list
    lb.delete(0, END)
    for item in list:
        lb.insert(END, item)


def filter_temp_above():
    try:
        filter_value = int(filter_entry.get())
        lb.delete(0, END)
        count = 0

        for item in list:
            parse = item.strip().split("|")
            temp = int(parse[1].strip())
            if temp >= filter_value:
                lb.insert(END, item)
                count += 1

        if count == 0:
            res.config(text=f"Нет записей с температурой выше {filter_value}°", fg="red")
        else:
            res.config(text=f"Найдено {count} записей с температурой выше {filter_value}°", fg="green")

    except ValueError:
        res.config(text="Введите число для фильтрации!", fg="red")
        return


def filter_temp_below():
    try:
        filter_value = int(filter_entry.get())
        lb.delete(0, END)
        count = 0

        for item in list:
            parse = item.strip().split("|")
            temp = int(parse[1].strip())
            if temp <= filter_value:
                lb.insert(END, item)
                count += 1

        if count == 0:
            res.config(text=f"Нет записей с температурой ниже {filter_value}°", fg="red")
        else:
            res.config(text=f"Найдено {count} записей с температурой ниже {filter_value}°", fg="green")

    except ValueError:
        res.config(text="Введите число для фильтрации!", fg="red")
        return


def show_all():
    update_lb()
    res.config(text="Показаны все записи", fg="green")



Label(text="Weather Diary", font="Arial 24 bold", bg="#f0f0f0", fg="#333333").place(x=500, y=20)


Label(text="Дата (пример: 22.04.2026)", font="Arial 14", bg="#f0f0f0").place(x=50, y=100)
date_entry = Entry(font="Arial 14", width=25, bg="white", relief="solid")
date_entry.place(x=50, y=130)

Label(text="Температура (°C)", font="Arial 14", bg="#f0f0f0").place(x=50, y=180)
temp_entry = Entry(font="Arial 14", width=25, bg="white", relief="solid")
temp_entry.place(x=50, y=210)

Label(text="Описание", font="Arial 14", bg="#f0f0f0").place(x=50, y=260)
desk_entry = Entry(font="Arial 14", width=25, bg="white", relief="solid")
desk_entry.place(x=50, y=290)

Label(text="Осадки (да/нет)", font="Arial 14", bg="#f0f0f0").place(x=50, y=340)
osadki_entry = Entry(font="Arial 14", width=25, bg="white", relief="solid")
osadki_entry.place(x=50, y=370)

Button(text="Добавить запись", font="Arial 14", command=add_item, bg="#4CAF50", fg="white", relief="raised", padx=10,
       pady=5).place(x=50, y=430)


res = Label(font="Arial 10", fg="red", text="", bg="#f0f0f0")
res.place(x=50, y=490)


Label(text="Фильтр по температуре", font="Arial 16 bold", bg="#f0f0f0", fg="#333333").place(x=50, y=540)
filter_entry = Entry(font="Arial 14", width=15, bg="white", relief="solid")
filter_entry.place(x=50, y=580)

Button(text="ВЫШЕ", font="Arial 12", command=filter_temp_above, bg="#2196F3", fg="white", width=10).place(x=50, y=620)
Button(text="НИЖЕ", font="Arial 12", command=filter_temp_below, bg="#2196F3", fg="white", width=10).place(x=160, y=620)

Button(text="ПОКАЗАТЬ ВСЕ", font="Arial 12", command=show_all, bg="#FF9800", fg="white", width=12).place(x=50, y=660)


lb = Listbox(font="Arial 12", width=70, height=28, bg="white", relief="solid", selectbackground="#4CAF50")
lb.place(x=400, y=80)

window.mainloop()
