from tkinter import *
import numpy as np
import random
from PIL import Image, ImageTk, ImageDraw  #Подключим необходимые библиотеки. 
from tkinter import filedialog
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv

def open_img():
    btn.grid_forget()
    global x 
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    global panel
    panel= Label(root, image=img)
    panel.image = img
    panel.grid(row=2, column=1, padx=5, pady=5)
    btn2.grid(row=1, column=1, padx=5, pady=5)


def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename


def qwe():
    global x
    #mode = int(input('mode:')) #Считываем номер преобразования. 
    imageO = Image.open(x)       #Открываем изображение. 
    draw = ImageDraw.Draw(imageO)   #Создаем инструмент для рисования. 
    width = imageO.size[0]       #Определяем ширину. 
    height = imageO.size[1]       #Определяем высоту. 	
    pix = imageO.load()         #Выгружаем значения пикселей.
    pixarr = np.array(imageO)
    xyi=pixarr.shape
    shap = int(np.prod(xyi)/3)
    pixarr.shape=(shap,3)
    pixarr2 = np.unique(pixarr, axis=0)
    differ = pixarr.shape[0] - pixarr2.shape[0]
    sa = 0
    sb = 0
    sc = 0
    rty=0
    redarr = np.array([])
    greenarr = np.array([])
    bluearr = np.array([])
    for i in range(width):
        for j in range(height):
#-------------------------------------------------------
            a = pix[i, j][0]

            redarr = np.append(redarr, a)
            sa += a
            b = pix[i, j][1]
            greenarr = np.append(greenarr,b)
            sb += b
            c = pix[i, j][2]
            bluearr = np.append(bluearr,c)
            sc += c

    return(sa,sb,sc,differ,draw,imageO,redarr,greenarr,bluearr)
    #		S = (a + b + c) // 3
    #		draw.point((i, j), (S, S, S))
    #image.save("c:\\Python\\tx2.jpg", "JPEG")
#--------------------------------------------------------
    del draw


def Graf():
    global x
    sa,sb,sc,differ,draw,imageO,r,g,b= qwe()
    del draw
    red25=(r<25)
    red50=(r>24)&(r<50)
    red75=(r>49)&(r<75)
    red100=(r>74)&(r<100)
    red125=(r>99)&(r<125)
    red150=(r>124)&(r<150)
    red175=(r>149)&(r<175)
    red200=(r>174)&(r<200)
    red225=(r>199)&(r<225)
    red255=(r>224)&(r<255)
    green25=(g<25)
    green50=(g>24)&(g<50)
    green75=(g>49)&(g<75)
    green100=(g>74)&(g<100)
    green125=(g>99)&(g<125)
    green150=(g>124)&(g<150)
    green175=(g>149)&(g<175)
    green200=(g>174)&(g<200)
    green225=(g>199)&(g<225)
    green255=(g>224)&(g<255)
    blue25=(b<25)
    blue50=(b>24)&(b<50)
    blue75=(b>49)&(b<75)
    blue100=(b>74)&(b<100)
    blue125=(b>99)&(b<125)
    blue150=(b>124)&(b<150)
    blue175=(b>149)&(b<175)
    blue200=(b>174)&(b<200)
    blue225=(b>199)&(b<225)
    blue255=(b>224)&(b<255)

    data_names = ['0-25', '25-50', '50-75', '75-100', 
              '100-125', '125-150', '150-175', '175-200',
              '200-225','225-255']
    data_valuesr = [np.count_nonzero(red25), np.count_nonzero(red50), np.count_nonzero(red75), np.count_nonzero(red100),
                   np.count_nonzero(red125), np.count_nonzero(red150), np.count_nonzero(red175), np.count_nonzero(red200),
                   np.count_nonzero(red225), np.count_nonzero(red255)]
    data_valuesg = [np.count_nonzero(green25), np.count_nonzero(green50), np.count_nonzero(green75), np.count_nonzero(green100),
                   np.count_nonzero(green125), np.count_nonzero(green150), np.count_nonzero(green175), np.count_nonzero(green200),
                   np.count_nonzero(green225), np.count_nonzero(green255)]
    data_valuesb = [np.count_nonzero(blue25), np.count_nonzero(blue50), np.count_nonzero(blue75), np.count_nonzero(blue100),
                   np.count_nonzero(blue125), np.count_nonzero(blue150), np.count_nonzero(blue175), np.count_nonzero(blue200),
                   np.count_nonzero(blue225), np.count_nonzero(blue255)]
    dpi = 80
    fig = plt.figure(dpi = dpi, figsize = (682 / dpi, 484 / dpi) )
    mpl.rcParams.update({'font.size':20})
    ax = plt.axes()
   
    ax.yaxis.grid(True, zorder = 1)
    xs = range(len(data_names))

    plt.bar([x + 0.05 for x in xs], data_valuesr,
        width = 0.2, color = 'red', alpha = 0.7, label = 'red',
        zorder = 2)
    plt.bar([x + 0.3 for x in xs], data_valuesg,
        width = 0.2, color = 'green', alpha = 0.7, label = 'green',
        zorder = 2)
    plt.bar([x + 0.5 for x in xs], data_valuesb,
        width = 0.2, color = 'blue', alpha = 0.7, label = 'blue',
        zorder = 2)
    plt.xticks(xs, data_names)
    fig.autofmt_xdate(rotation = 25)

    fig.savefig("D:\picanylspy\py.jpg")

    img = Image.open("D:\picanylspy\py.jpg")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel2 = Label(root, image=img)
    panel2.image = img
    btn2.grid_forget()
    KLSK.grid(row=1, column=2, padx=5, pady=5)
    KLOR.grid(row=1, column=1, padx=5, pady=5)
    panel2.grid(row=2, column=2, padx=5, pady=5)
    Kkoe = Label(text='Кіл. однак. елем. ' + str(differ) ,font="Arial 12")
    Kkoe.grid(row=3, column=1, padx=5, pady=5)


    os.remove("D:\picanylspy\py.jpg")

root = Tk()
root.geometry("560x360+200+50")
root['bg'] = '#555'

root.resizable(width=True, height=True)
btn = Button(root, text='Відкрити зображення',background="#555", foreground="#ccc",font="Arial 16", command=open_img)
btn.grid(row=1, column=1, padx=150, pady=100)
btn2 = Button(root, text='Провести аналіз',background="#555", foreground="#ccc", command=Graf)
KLSK = Label(text='Cпіввідношшення кольорів',background="#555", foreground="#ccc",font="Arial 16")
KLOR = Label(text='Оригінал',background="#555", foreground="#ccc",font="Arial 16")



root.mainloop()
 