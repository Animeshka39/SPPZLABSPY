<<<<<<< Updated upstream
import math

while True:
    menu = int(input(  "Ведіть номер задачі від 1 до 10 або введіть: 999 для заверщення роботи "))
    if menu == 1:
        x = input(  "x =  ")
        y = input(  "y =  ")

        s = float(x) + float(y)
        r = float(x) - float(y)
        d = float(x) * float(y)

        prfloat ("Сума " + str(s) + "\n")
        prfloat ("Рiзниця " + str(r) + "\n")
        prfloat ("Добуток " + str(d) + "\n")

    if menu == 2:
        x = input(  "x =  ")
        y = input(  "y =  ")
        s = (math.fabs(float(x)) - math.fabs(float(y))) / (1 + math.fabs(float(x) * float(y)))
        prfloat ("Результат "  + str(s) + "\n")

    if menu == 3:
        x = input(  "Довжина ребра куба =  ")
        o = float(x) * float(x) * float(x) 
        s = float(x) * float(x)
        print ("Обєм куба " + str(o) + "\n")
        print ("Площа бокової поверхностi " + str(s) + "\n")

    if menu == 4:
        x = input(  "x =  ")
        y = input(  "y =  ")
        s = (float(x) + float(y)) / 2
        p = math.sqrt(float(x) * float(y) )
        print ("Сер. ариф. " + str(s) + "\n")
        print ("Сер. геом. "  + str(p) + "\n")

    if menu == 5:
        x = input(  "x =  ")
        y = input(  "y =  ")
        s = (float(x) + float(y)) / 2
        p = math.sqrt(math.fabs(float(x)) * math.fabs(float(y)) )
        print ("Сер. ариф. " + str(s) + "\n")
        print ("Сер. геом. "  + str(p) + "\n")

    if menu == 6:
        x = input(  "Катет а = ")
        y = input(  "Катет б = ")
        s = math.sqrt((float(x) * float(x)) + (float(y) * float(y)))
        p = float(x) + float(y)
        print ("Гiпотенуза "  + str(s) + "\n")
        print ("Площа "  + str(p) + "\n")

    if menu == 7:
        o1 = input(  "Обєм 1 = ")
        o2 = input(  "Обєм 2 = ")
        t1 = input(  "Температура 1 = ")
        t2 = input(  "Температура 2 = ")
        oz = float(o1) * float(o2) 
        tz = (float(o1) * float(t1) + float(o2) * float(t2)) / oz
        print ("Загальний обєм = "  + str(oz) + "\n")
        print ("Загальна температура = "  + str(tz) + "\n")


    if menu == 8:
        r = input(  "Радiус =  ")
        n = input(  "Кiлькiсть сторiн = ")
        p = 2 * float(r) * float(n) * math.sin(math.pi / float(n))* math.cos(math.pi / float(n))
        print ("Периметр = "  + str(p) + "\n")

    if menu == 9:
        r1 = input(  "Опiр 1 =  ")
        r2 = input(  "Опiр 2 =  ")
        r3 = input(  "Опiр 3 =  ")
        t = 1/float(r1) + 1/float(r2) + 1/float(r3)
        print ("Заг. опiр = "  + str(t) + "\n")

    if menu == 10:
        h = input(  "Висота = ")
        t = math.sqrt((2 * float(h)) / 9.81)
        print ("Час = "   + str(t) + "\n")
    if menu == 999:
        break
=======
import os
from tkinter import *
from tkinter import messagebox
import time
import pyautogui as pag


clicks = 0

root = Tk()
root.title("GUI на Python")
root.geometry("377x200")
root['bg'] = '#555'

type = IntVar()
timeout = StringVar()

Label1 = Label(text="Enter timeout value:", background="#555", foreground="#ccc")
Label1.pack()
Label1.place(x=0,y=60)

timeout_entry = Entry(textvariable=timeout)
timeout_entry.place(x=140,y=60)

hour_checkbutton = Radiobutton(text = "Hours",background="#555", foreground="#ccc", value=1, variable=type)
hour_checkbutton.pack()
hour_checkbutton.place(x=0, y=90)

minute_checkbutton = Radiobutton(text = "Minutes",background="#555", foreground="#ccc", value=2, variable=type)
minute_checkbutton.pack()
minute_checkbutton.place(x=0, y=120)

seconds_checkbutton = Radiobutton(text = "Seconds",background="#555", foreground="#ccc", value=3, variable=type)
seconds_checkbutton.pack()
seconds_checkbutton.place(x=0, y=150)
 
def click_button():
    global clicks
    clicks += os.system("shutdown /s /t " + str(timeout.get()))
def hibernation():
    global clicks
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
def reboot():
    global clicks
    clicks += os.system("shutdown /r /t " + str(timeout.get()))
def close_windows():
    global clicks
    clicks += os.system("%windir%\explorer.exe shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}" + str(timeout.get()))
def open_windows():
    global clicks
    pag.hotkey('win','home',interval=str(timeout.get()))
 

 
btn = Button(text="Shutdown", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.place(x=0, y=0)

btn1 = Button(text="Hibernation", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=hibernation)

btn1.place(x=130, y=0)

btn2 = Button(text="Reboot", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=reboot)
btn2.place(x=275, y=0)

btn3 = Button(text="Close windows", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=close_windows)
btn3.place(x=200, y=90)

btn4 = Button(text="Open windows", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=open_windows)
btn4.place(x=200, y=145)

root.mainloop()
>>>>>>> Stashed changes
