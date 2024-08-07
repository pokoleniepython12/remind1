from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import pygame
import datetime
import time



def set():
    global t
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


def check():
    global t
    if t:
        now=time.time()
        if now>=t:
            play_snd()
            t=0
    window.after(10000,check)

def play_snd():
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()



t=0

window=Tk()
window.title("Напоминание")

label=Label(text="Установить напоминание")
label.pack(pady=15)

set_button=Button(text="Установить",command=set)
set_button.pack(pady=15)


check()
window.mainloop()

