from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import pygame
import datetime
import time

window=Tk()
window.title("Напоминание")

label=Label(text="Установить напоминание")
label.pack(pady=15)

set_button=Button(text="Установить",command=set)
set_button.pack(pady=15)

window.mainloop()

