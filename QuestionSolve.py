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
top1.title("User Dashboard")
width = 450
height = 350
screen_width = top1.winfo_screenwidth()
screen_height = top1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top1.geometry("%dx%d+%d+%d" % (width, height, x, y))
top1.config(bg="LightBlue4")
variable = tk.StringVar()
variable.set("--Select Temperature--") # default value

variable1 = tk.StringVar()
variable1.set("--Select Rainfall--") # default value

variable2 = tk.StringVar()
variable2.set("--Select Soil type--") # default value

variable3 = tk.StringVar()
variable3.set("--Select Sunlight--") # default value

variable4 = tk.StringVar()
variable4.set("--Select PH Value--") # default value

variable5 = tk.StringVar()
variable5.set("--Select Season--") # default value

error1=tk.StringVar()

def results():
    
    temp=variable.get().strip()
    rainfall=variable1.get().strip()
    soil=variable2.get().strip()
    light=variable3.get().strip()
    ph=variable4.get().strip()
    season=variable5.get().strip()

    print("temperature",temp)
    print("rainfall",rainfall)
    print("Soil",soil)
    print("light",light)
    print("PH",ph)
    print("Season",season)
    
    
    mycursor.execute("select * from questions")
    myresult = mycursor.fetchall()
    #print(temp)
    prediction=""
    isfound=False
    for x in myresult:
        #print(x[1])
        if(temp==x[1].strip()and rainfall==x[2].strip()and soil==x[3].strip()and light==x[4].strip() and ph==x[5].strip() and season==x[6].strip()):
            #error1.set("Answer")
            prediction=x[7]
            isfound=True
        if(temp==x[1].strip()):
            print("Match Found")
            #error1.set("Answer")
            isfound=True
            
    if(isfound):
        messagebox.showinfo("Prediction",prediction)
    else:
        messagebox.showinfo("Prediction","No Result Found")
        

    
   

    ErL12=tk.Label(top2,text="ssdhjsdh",fg="white",font=('arial', 15),bg="grey",textvariable=error1,bd=3)
    ErL12.grid(row=3,column=1,padx=20,pady=20)


L= tk.Label(top1, width=30, font=('arial bold', 12),fg="dark green",bg="LightBlue4" ,text = "PEST PREDICTION SYSTEM        ")
L.grid(row=1,column=2, pady=20)
#----------------------------Temperature-----------------------
L1=tk.Label(top1,text="   Select Temperature",bg="LightBlue4")
L1.grid(row=2,column=1)
w = tk.OptionMenu(top1, variable,"15-20","20-25", "25-30","30-35 ","35-40")
w.config(bd=5,width="20")
w.grid(row=2,column=2)
#------------------------Rainfall---------------------------
L2=tk.Label(top1,text="Select Rainfall",bg="LightBlue4")
L2.grid(row=3,column=1)
w1 = tk.OptionMenu(top1, variable1,"0-50","50-100", "100-150","150-200","200-250","250-300")
w1.config(bd=5,width="20")
w1.grid(row=3,column=2)

#-------------------Soil Type-----------------------------
L3=tk.Label(top1,text="Select Soil Type",bg="LightBlue4")
L3.grid(row=4,column=1)
w2 = tk.OptionMenu(top1, variable2,"Podzolic alluviul, heavy clay, riverine alluvial, Clayey Loam","Light clay, heavy loam, sandy loam","Loamy Soil","Sandy loam"," Sandy Soil, Black Soil, Red Soil","Fertile sandy, Loam soils, black cotton soils","Black Soil","deep loamy , clay loam, temperate podzol, leached red soils","Sandy loam, heavy clay soil","loam, red volcanic soils, alluvial soils"," sandy, heavy clay, red loam soils","alluvial , loamy soils,  sandy loams, clay loams","loamy,  sandy loam")
w2.config(bd=5,width="20")
w2.grid(row=4,column=2)

#-------------------Sunlight---------------------
L4=tk.Label(top1,text="Select Sunlight",bg="LightBlue4")
L4.grid(row=5,column=1)

w3 = tk.OptionMenu(top1, variable3,"0--1","1--2","2--3","3--4","4--5","5--6","6--7","7--8","8--9","9--10","10--11","11--12","12--13","13--14","14--15","15--16")
w3.config(bd=5,width="20")
w3.grid(row=5,column=2)


#-------------------PH value---------------------
L5=tk.Label(top1,text="Select PH Value",bg="LightBlue4")
L5.grid(row=6,column=1)

w4 = tk.OptionMenu(top1, variable4,"0.0-0.9","1.0-1.9","2.0-2.9","3.0-3.9","4.0-4.9","5.0-5.9","6.0-6.9","7.0-7.9","8.0-8.9","9.0-9.9","10.0-10.9","11.0-11.9","12.0-12.9","13.0-13.9","14.0")
w4.config(bd=5,width="20")
w4.grid(row=6,column=2)

#----------------Season----------
L6=tk.Label(top1,text="Select Season",bg="LightBlue4")
L6.grid(row=7,column=1)
w5 = tk.OptionMenu(top1,variable5,"Kharif","Rabi","Kharif, Rabi\n")
w5.config(bd=5,width="20")
w5.grid(row=7,column=2)

b2=tk.Button(top1,fg="dark green",text="Search",bd=8,command=results)
b2.grid(row=10,column=2,pady=10)



top1.mainloop()









