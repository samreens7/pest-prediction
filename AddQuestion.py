import tkinter as tk
import pymysql
import sys
import os
import gc
from tkinter.filedialog import askopenfile
from subprocess import Popen
from tkinter import messagebox
import cv2
mydb=pymysql.connect(host="localhost",user="root",password="9405078366",database="pestprediction")
mycursor=mydb.cursor()

top1=tk.Tk()
top1.title("Admin Dashboard")
width = 500
height = 400
screen_width = top1.winfo_screenwidth()
screen_height = top1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top1.geometry("%dx%d+%d+%d" % (width, height, x, y))
top1.config(bg="LightBlue4")
variable = tk.StringVar()
variable.set("--Select Temperature--") # default value

variable1 = tk.StringVar()
variable1.set("--Select RainFall--") # default value

variable2 = tk.StringVar()
variable2.set("--Select Soiltype--") # default value

variable3 = tk.StringVar()
variable3.set("--Select Sunlight--") # default value

variable4 = tk.StringVar()
variable4.set("--Select PH Value--") # default value

variable5 = tk.StringVar()
variable5.set("--Select Season--") # default value

error1=tk.StringVar()

def results():
    temp=variable.get()
    rainfall=variable1.get()
    soil=variable2.get()
    light=variable3.get()
    ph=variable4.get()
    season=variable5.get()

    sql="insert into questions (temperature,rainfall,soil,light,ph,season,answer)values(%s,%s,%s,%s,%s,%s,%s)"
    values=(temp,rainfall,soil,light,ph,season,E1.get())
    mycursor.execute(sql,values)
    mydb.commit()
    messagebox.showinfo("Message", "Question Added Sucessfully")
    top1.destroy()
    #if(temp=="20 -- 27" and rainfall=="175 - 300" and soil==" podzolic alluviul, heavy clay, riverine alluvial, Clayey Loam" and light=="12" and ph=="6" and season=="Kharif"):
        #error1.set("तुम्ही आपल्या शेतामध्ये तांदळाची शेती घेऊ शकता  ")
        #print("sdaf")
    



L= tk.Label(top1, width=30, font=('arial', 20),bg="LightBlue4",fg="dark green", text = "Pest Prediction System",bd=5)
L.grid(row=1,column=1)
#----------------------------Temperature-----------------------
w = tk.OptionMenu(top1, variable,"15-20","20-25", "25-30","30-35 ","35-40")
w.config(bd=5,width="20")
w.grid(row=2,column=1)
#------------------------Rainfall---------------------------

w1 = tk.OptionMenu(top1, variable1,"0-50","50-100", "100-150","150-200","200-250","250-300")
w1.config(bd=5,width="20")
w1.grid(row=3,column=1)

#-------------------Soil Type-----------------------------
w2 = tk.OptionMenu(top1, variable2," Podzolic alluviul, heavy clay, riverine alluvial, Clayey Loam","Light clay, heavy loam, sandy loam","Loamy Soil","Sandy loam"," Sandy Soil, Black Soil, Red Soil","Fertile sandy, Loam soils, black cotton soils","Black Soil","deep loamy , clay loam, temperate podzol, leached red soils","Sandy loam, heavy clay soil","loam, red volcanic soils, alluvial soils"," sandy, heavy clay, red loam soils","alluvial , loamy soils,  sandy loams, clay loams","loamy,  sandy loam")
w2.config(bd=5,width="20")
w2.grid(row=4,column=1)

#-------------------Sunlight---------------------

w3 = tk.OptionMenu(top1, variable3,"0--1","1--2","2--3","3--4","4--5","5--6","6--7","7--8","8--9","9--10","10--11","11--12","12--13","13--14","14--15","15--16")
w3.config(bd=5,width="20")
w3.grid(row=5,column=1)


#-------------------PH value---------------------

w4 = tk.OptionMenu(top1, variable4,"0.0-0.9","1.0-1.9","2.0-2.9","3.0-3.9","4.0-4.9","5.0-5.9","6.0-6.9","7.0-7.9","8.0-8.9","9.0-9.9","10.0-10.9","11.0-11.9","12.0-12.9","13.0-13.9","14.0")
w4.config(bd=5,width="20")
w4.grid(row=6,column=1)

#----------------Season----------
w5 = tk.OptionMenu(top1,variable5,"Kharif","Rabi","Kharif, Rabi\n")
w5.config(bd=5,width="20")
w5.grid(row=7,column=1)

L3=tk.Label(top1,text="Enter Answer")
L3.grid(row=8,column=1,pady=10)

E1=tk.Entry(top1)
E1.config(bd=5,width="30")
E1.grid(row=9,column=1)


b2=tk.Button(top1,bg="black",fg="limegreen",text="Submit",bd=8,command=results)

b2.grid(row=10,column=1,pady=10)


ErL12=tk.Label(top1,text="",fg="red",font=('arial', 15),bg="grey",textvariable=error1,bd=3)
ErL12.grid(row=12,column=1)

top1.mainloop()









