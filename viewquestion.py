from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
import os
import pymysql
import tkinter as tk 
mydb=pymysql.connect(host="localhost",user="root",password="9405078366",database="pestprediction")
mycursor=mydb.cursor()

top2=tk.Tk()
top2.title("Images Results")
width = 1180
height = 350
screen_width = top2.winfo_screenwidth()
screen_height = top2.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top2.geometry("%dx%d+%d+%d" % (width, height, x, y))
top2.config(bg="LightBlue4")

def click():
    os.system("generateprediction.py")
    top2.quit()

Lb1 = tk.Listbox(top2,width=130,bd=3,font=("arial",12))



       
#------------------------------------Show results--------------------------------------------

mycursor.execute("select * from questions")
myresult = mycursor.fetchall()
k=1
post=""
for x in myresult:
     post="Temperature: "+x[1]+" | Rainfall: "+x[2]+" | Soil: "+x[3]+" | Light: "+x[4]+" | PH: "+x[5]+" | Season: "+x[6]+" | Answer: "+x[7]
    #tk.Label(top2,text=post,fg="red",bg="black", font=('arial', 14), bd=5).grid(row=k,column=2)
     Lb1.insert(k, post)
     k=k+1
Lb1.grid(row=12, column=1)
top2.mainloop();


