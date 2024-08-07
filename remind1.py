from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import pygame
import datetime
import time


def set():
    rem=sd.askstring("Время напоминания","Введите время напоминания в формате ЧЧ:ММ(в 24 часоввом формате)")
    if rem:
        try:
            hour=int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now=datetime.datetime.now()
            print(now)

            dt=now.replace(hour=hour,minute=minute)
            print(dt)

            t=dt.timestamp()
            print(t)
        except Exception as e:
            mb.showerror("Ошибка",f"Произошла ошибка : {e}")



window=Tk()
window.title("Напоминание")

label=Label(text="Установить напоминание")
label.pack(pady=15)

set_button=Button(text="Установить",command=set)
set_button.pack(pady=15)

window.mainloop()

