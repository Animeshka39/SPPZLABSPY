
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
