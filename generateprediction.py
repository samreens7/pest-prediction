import shutil, os
import tkinter as tk
import pymysql
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import cv2
from tkinter import *
top2=tk.Tk()
top2.title("Images Results")
width = 810
height = 350
screen_width = top2.winfo_screenwidth()
screen_height = top2.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top2.geometry("%dx%d+%d+%d" % (width, height, x, y))
top2.config(bg="LightBlue4")

mydb=pymysql.connect(host="localhost",user="root",password="9405078366",database="pestprediction")
mycursor=mydb.cursor()
error1=tk.StringVar()
error2=tk.StringVar()
k=1
post=""
str1=tk.StringVar()
L1=tk.Label(top2, width=30, font=('arial bold', 20),fg="black",bg="LightBlue4" ,text = "  PEST PREDICTION SYSTEM")
L1.grid(row=1, column=1,pady=30)


ErL12=tk.Label(top2,text="",fg="white",font=('arial', 15),bg="LightBlue4",textvariable=error1,bd=3)
ErL12.grid(row=3,column=1,pady=10)


ErL13=tk.Label(top2,text="",fg="white",font=('arial', 15),bg="LightBlue4",textvariable=error2,bd=3)
ErL13.grid(row=4,column=1,pady=10)

img=""

mycursor.execute("select * from imagematches order by imgmatch desc limit 1")
myresult = mycursor.fetchall()
for x in myresult:
    post="Disease Name:  "+x[1]+" | Disease Solution:  "+x[2]
    img=x[1]

disease=""
description=""
print(img)
mycursor.execute("select * from dataset")
myresult = mycursor.fetchall()
img11=""

for x1 in myresult:
    img11=x1[1]
    print(img11)
    if (img11==img):
        post="Disease Name:  "+x1[2]+" | Disease Prediction:  "+x1[3]
        error1.set("Disease Name  :  "+x1[2])
        error2.set("Disease Solution  :  "+x1[3])
        
    
   



top2.mainloop()
