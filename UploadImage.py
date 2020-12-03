import shutil, os
import tkinter as tk
import pymysql
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import cv2
top2=tk.Tk()
top2.title("Training")
width = 500
height = 350
screen_width = top2.winfo_screenwidth()
screen_height = top2.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top2.geometry("%dx%d+%d+%d" % (width, height, x, y))
top2.config(bg="LightBlue4")
mydb=pymysql.connect(host="localhost",user="root",password="9405078366",database="pestprediction")
mycursor=mydb.cursor()
def upload():
    d1=E11.get()
    d2=E12.get()
    file = askopenfile(mode ='r')
    name1 = os.path.basename(file.name)
    print(file);
    #-----------------Resizing--------
    img = cv2.imread(file.name, cv2.IMREAD_UNCHANGED)
    scale_percent = 60 # percent of original size
    width = 200
    height = 200
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    imgname=""+name1+""
    cv2.imwrite("Training/"+imgname,resized)

    #---------------------------------------------------------
    #shutil.copy2(str(file.name), 'Training')
    print("file"+file.name)
    sql="insert into dataset (imagename,disease,description)values(%s,%s,%s)"
    values=(imgname,d1,d2)
    mycursor.execute(sql,values)
    mydb.commit()
    messagebox.showinfo("Message", "Image Uploaded Sucessfully")
    top2.quit()
   
L= tk.Label(top2, width=30, font=('arial', 20,"bold"),bg="LightBlue4",fg="dark green", text = "Pest Prediction System",bd=5,pady=15)
L.grid(row=1,column=1)

L1=tk.Label(top2,text="Enter Disease Name:",fg="black",bg="LightBlue4", font=('arial', 14), bd=5)
L1.grid(row=3, column=1)

E11=tk.Entry(top2,font=(14),bd=5)
E11.grid(row=4,column=1)


L2=tk.Label(top2,text="Enter Solution:",fg="black",bg="LightBlue4", font=('arial', 14), bd=5)
L2.grid(row=5, column=1)

E12=tk.Entry(top2,font=(14),bd=5)
E12.grid(row=6,column=1)

L1=tk.Label(top2,text="\nSelect Image to Upload",fg="black",bg="LightBlue4", font=('arial', 14), bd=5)
L1.grid(row=7, column=1)

b2=tk.Button(top2,bg="black",fg="limegreen",text="Upload Image for Training",bd=8,command=upload)
b2.grid(row=15,column=1)
top2.mainloop()
