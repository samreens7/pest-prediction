import shutil, os
import tkinter as tk
import pymysql
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import cv2
from tkinter import *

from skimage.measure import compare_ssim
import argparse
import imutils
import tkinter as tk 

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
L1=tk.Label(top2, width=30, font=('arial bold', 20),fg="dark green",bg="LightBlue4" ,text = "  PEST PREDICTION SYSTEM")
L1.grid(row=1, column=1,pady=30)


ErL12=tk.Label(top2,text="",fg="black",font=('arial', 15),bg="LightBlue4",textvariable=error1,bd=3)
ErL12.grid(row=3,column=1,pady=10)


ErL13=tk.Label(top2,text="",fg="black",font=('arial', 15),bg="LightBlue4",textvariable=error2,bd=3)
ErL13.grid(row=4,column=1,pady=10)

img=""

trainingImage=""
testingimage=""

path = 'Testing'
training="Training"
files = []
for r, d, f in os.walk(path):
    for file in f:
        #print(os.path.join( file))
        testingimage=os.path.join(file)
       


print("path="+testingimage)          
imageA = cv2.imread("Testing/"+testingimage)
q2="delete from imagematches"
mycursor.execute(q2)

for r, d, f1 in os.walk(training):
    for file1 in f1:
        print(os.path.join( file1))
        trainingimg=os.path.join( file1)
        imageB = cv2.imread("Training/"+trainingimg)
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        print("SSIM: {}".format(score))
        
        ql="insert into imagematches(imagename,imgmatch)values(%s,%s)"
        values=(trainingimg,str(format(score)))
        mycursor.execute(ql,values)
        mydb.commit()
 
        thresh = cv2.threshold(diff, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)



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
