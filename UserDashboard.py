import tkinter as tk
import pymysql
import sys
import os
import gc
import cv2
import subprocess
from tkinter.filedialog import askopenfile
from subprocess import Popen
from tkinter import messagebox
from subprocess import call


top1=tk.Tk()
top1.title("User Dashboard")
width = 800
height = 700
screen_width = top1.winfo_screenwidth()
screen_height = top1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top1.geometry("%dx%d+%d+%d" % (width, height, x, y))
top1.config(bg="LightBlue4")

def uploadtesting():
    path = 'Testing'
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            testingimage=os.path.join(file)
            os.remove("Testing/"+testingimage)
    file1 = askopenfile(mode ='r')
    #----------------------------------------resize testing image-------
    name1 = os.path.basename(file1.name)
    img = cv2.imread(file1.name, cv2.IMREAD_UNCHANGED)
    scale_percent = 60 # percent of original size
    width = 200
    height = 200
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    imgname=""+name1+""
    cv2.imwrite("Testing/"+imgname,resized)
    messagebox.showinfo("Message", "Image Uploaded For Testing")

#def viewusers():
    #call('python ViewUsers.py', shell=True)
    #os.system("ViewUsers.py")
def uploadtraining():
    call('python UploadImage.py', shell=True)
    #os.system("ViewAllSearches.py")
def prediction():
    subprocess.call('python pred_user.py', shell=True)
    #os.system("pred_user.py")
def solvequestion():
    call('python QuestionSolve.py', shell=True)
    #os.system("BlackListedLink.py")
def logout():
    top1.destroy()
    call('python index.py', shell=True)
    #os.system("index.py")
    
        



L= tk.Label(top1, width=30, font=('arial', 20,'bold'),fg="black",bg="LightBlue4" ,text = "                                PEST PREDICTION \n                             SYSTEM ")
L.grid(row=2,column=1,pady=20)


L1= tk.Label(top1, width=30, font=('arial bold', 19),fg="white",bg="LightBlue4" ,text = "Prediction:")
L1.grid(row=3,column=1,pady=20)

photo2 = tk.PhotoImage(file = r"C:\Users\samreen syeda\Desktop\FinalCode\images\searches.png")
photoimage2 = photo2.subsample(4, 4) 
b3= tk.Button(top1,bg="white",fg="green",text="Upload For Testing",bd=8,command=uploadtesting,image = photoimage2,compound ="top" )
b3.config(width="100")
b3.config(height="100")  
b3.grid(row=4,column=1)



photo4 = tk.PhotoImage(file = r"C:\Users\samreen syeda\Desktop\FinalCode\images\blacklink.png")
photoimage4 = photo4.subsample(4, 4)
b5= tk.Button(top1,bg="white",fg="green",text="Prediction",bd=8,command=prediction,image = photoimage4,compound ="top" )
b5.config(width="100")
b5.config(height="100")   
b5.grid(row=4,column=3)


L2= tk.Label(top1, width=30, font=('arial bold', 19),fg="white",bg="LightBlue4" ,text = "\nRecommendation:")
L2.grid(row=6,column=1,pady=20)

photo5 = tk.PhotoImage(file = r"C:\Users\samreen syeda\Desktop\FinalCode\images\question.png")
photoimage5 = photo5.subsample(4, 4)
b6= tk.Button(top1,bg="white",fg="green",text="Recommend Crop",bd=8,command=solvequestion,image = photoimage5,compound ="top"  )
b6.config(width="100")
b6.config(height="100")  
b6.grid(row=7,column=1)

photo6 = tk.PhotoImage(file = r"C:\Users\samreen syeda\Desktop\FinalCode\images\logout.png")
photoimage6 = photo6.subsample(4, 4)
b7= tk.Button(top1,bg="white",fg="green",text="Admin Login",bd=8,command=logout,image = photoimage6,compound ="top"  )
b7.config(width="100")
b7.config(height="100")  
b7.grid(row=7,column=3)


L1= tk.Label(top1, width=30, font=('arial bold', 10),fg="black",bg="LightBlue4" ,text ="\n\nHow to Use :                                 ")
L1.grid(row=8,column=1)

L2= tk.Label(top1, width=40, font=('arial bold', 10),fg="BEIGE",bg="LightBlue4" ,text = "    1. Upload image for Testing                        ")
L2.grid(row=9,column=1,pady=5)

L3= tk.Label(top1, width=40, font=('arial bold', 10),fg="BEIGE",bg="LightBlue4" ,text = "2. Click On Prediction                             ")
L3.grid(row=10,column=1,pady=5)

L4= tk.Label(top1, width=40, font=('arial bold', 10),fg="BEIGE",bg="LightBlue4" ,text = "        3. For recommendation click on Recommend\nCrop")
L4.grid(row=11,column=1,pady=5)






top1.mainloop()
