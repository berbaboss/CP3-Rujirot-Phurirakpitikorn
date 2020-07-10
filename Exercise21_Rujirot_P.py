from tkinter import *
import math

def leftclickbutton(event):
    x = (float(textboxweight.get())/math.pow(float(textboxheight.get())/100,2))
    if(x>=30):
        labelresult.configure(text = "อ้วนมาก")
    elif (x<=29.9 and x>=25.0):
        labelresult.configure(text = "อ้วน")
    elif (x<=24.9 and x>=23.0):
        labelresult.configure(text = "น้ำหนักเกิน")
    elif (x<=22.9 and x>=18.6):
        labelresult.configure(text = "น้ำหนักปกติ เหมาะสม")
    else:
        labelresult.configure(text = "ผอมเกินไป")
    print(x)

Mainwindow = Tk() #สร้าง main window
labelHeight = Label(Mainwindow,text = "ส่วนสูง (cm.)")
labelHeight.grid(row = 0,column = 0)
textboxheight = Entry(Mainwindow)
textboxheight.grid(row = 0,column = 1)
labelWeight = Label(Mainwindow,text = "น้ำหนัก (kg.)")
labelWeight.grid(row = 1,column = 0)
textboxweight = Entry(Mainwindow)
textboxweight.grid(row = 1,column = 1)
calculatebutton = Button(Mainwindow,text = "คำนวณ")
calculatebutton.bind("<Button-1>",leftclickbutton)
calculatebutton.grid(row = 2,column = 0)
labelresult = Label(Mainwindow,text = "ผลลัพธ์")
labelresult.grid(row = 2,column = 1)
Mainwindow.mainloop()