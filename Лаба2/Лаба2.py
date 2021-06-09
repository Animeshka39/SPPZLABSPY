from tkinter import *
import os
 
 
def dir():
    qwe2 = ['']
    qwe = os.listdir(os.getcwd())
    sith = len(qwe)
    i=0
    while(i<sith):
        qwe2.append(qwe[i])
        i+=1
    return(qwe2)

def back():
    os.chdir("..")
    listb()

def open_f():
    selection = languages_listbox.curselection()
    a = languages_listbox.get(selection[0])
    for j in range(len(a)):
        if a[j] == ".":
            os.startfile(os.getcwd()  + "\\" + a)
            listb()
            return()
    os.chdir(os.getcwd()  + "\\" + a)
    listb()
def go():
    folder = language_entry.get()
    os.chdir(folder )
    listb()

def create_f():
    new_f = language_entry.get()
    open(new_f, "w")
    listb()
def create_p():
    new_p = language_entry.get()
    os.mkdir(new_p)
    listb()
def del_f():
    selection = languages_listbox.curselection()
    new_d = languages_listbox.get(selection[0])
    for j in range(len(new_d)):
        if new_d[j] == ".":
            os.remove(new_d)
            listb()
            return()

    os.rmdir(new_d)
    listb()
def renam():
    selection = languages_listbox.curselection()
    new_bif = languages_listbox.get(selection[0])
    new_aft = language_entry.get()

    os.rename(new_bif, new_aft)
    listb()
def repl():
    selection = languages_listbox.curselection()
    new_bif = languages_listbox.get(selection[0])
    new_aft = language_entry.get()

    os.replace(new_bif, new_aft)
    listb()
 
root = Tk()
root.title("Comander")
root['bg'] = '#555'
 
language_entry = Entry(width=35)
language_entry.grid(column=0, row=0, padx=6, pady=6)
create_f_button = Button(text="Створ.Файл",background="#555", foreground="#ccc", command=create_f).grid(column=2, row=0, padx=6, pady=6)
create_p_button = Button(text="Створ.Папку",background="#555", foreground="#ccc", command=create_p).grid(column=1, row=0, padx=6, pady=6)
 
languages_listbox = Listbox(height=20, width=50)
languages_listbox.grid(row=1, column=0, columnspan=2,rowspan=20, sticky=W+E, padx=5, pady=5)
 
def listb():
    languages_listbox.delete(0,'end')
    for language in dir():
        languages_listbox.insert(END, language) 

back_button = Button(text="Назад",background="#555", foreground="#ccc", command=back, width=8).grid(row=3, column=2, padx=5, pady=5)
open_button = Button(text="Открить",background="#555", foreground="#ccc", command=open_f, width=8).grid(row=4, column=2, padx=5, pady=5)
go_button = Button(text="Перейти",background="#555", foreground="#ccc", command=go, width=8).grid(row=2, column=2, padx=5, pady=5)
del_button = Button(text="Удалить",background="#555", foreground="#ccc", command=del_f, width=8).grid(row=5, column=2, padx=5, pady=5)
renam_button = Button(text="Переімен.",background="#555", foreground="#ccc", command=renam, width=8).grid(row=6, column=2, padx=5, pady=5)
repl_button = Button(text="Переміст.",background="#555", foreground="#ccc", command=repl, width=8).grid(row=7, column=2, padx=5, pady=5)
listb()
root.mainloop()
