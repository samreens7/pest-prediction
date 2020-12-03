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
width = 500
height = 370
screen_width = top2.winfo_screenwidth()
screen_height = top2.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top2.geometry("%dx%d+%d+%d" % (width, height, x, y))
top2.config(bg="LightBlue4")

def click():
    os.system("generateprediction.py")
    top2.quit()
 
L1= tk.Label(top2, width=30, font=('arial bold', 20),fg="black",bg="LightBlue4" ,text = "PEST PREDICTION SYSTEM")
L1.grid(row=1,column=1,pady=10)


L2=tk.Label(top2,text="Results Found" ,bg="LightBlue4",fg="white", font=('arial', 19), bd=5)
L2.grid(row=2, column=1)
b1=tk.Button(top2,fg="dark green",width="30",text="View Final Results",bd=8,command=click)
b1.grid(row=3,column=1,pady=10)

Lb1 = tk.Listbox(top2,width=50,bd=3,font=("arial",12))

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


       
#------------------------------------Show results--------------------------------------------

mycursor.execute("select * from imagematches order by imgmatch desc")
myresult = mycursor.fetchall()
k=1
post=""
for x in myresult:
     post="Img Name: "+x[1]+" | Match Ration: "+x[2]
    #tk.Label(top2,text=post,fg="red",bg="black", font=('arial', 14), bd=5).grid(row=k,column=2)
     Lb1.insert(k, post)
     k=k+1
Lb1.grid(row=12, column=1)
top2.mainloop();

#convert the images to grayscal
    
#cv2.imshow("Original", imageA)
#cv2.imshow("Modified", imageB)
#cv2.imshow("Diff", diff)
#cv2.imshow("Thresh", thresh)
#cv2.waitKey(0)
    
