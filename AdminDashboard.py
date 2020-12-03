import tkinter as tk
import sys
import os
import gc
import cv2
from tkinter.filedialog import askopenfile
from subprocess import Popen
from tkinter import messagebox
from subprocess import call


top1=tk.Tk()
top1.title("Admin Dashboard")
width = 830
height = 600
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

def viewquestion():
    call('python viewquestion.py', shell=True)
    #os.system("ViewUsers.py")
def uploadtraining():
    call('python UploadImage.py', shell=True)
    #os.system("ViewAllSearches.py")
def prediction():
    call('python prediction2.py', shell=True)
    #os.system("AddWordDictionary.py")
    
def addquesion():
    call('python AddQuestion.py', shell=True)
    #messagebox.showinfo("Message", "Question Uploaded Sucessfully")
    #os.system("BlackListedLink.py")
def uploadfromexcel():
    call('python UploadFromExcel.py', shell=True)
    messagebox.showinfo("Message", "Data Uploaded Sucessfully")
    #os.system("index.py")
def logout():
    top1.destroy()
    call('python index.py', shell=True)
    #os.system("index.py")

    

L= tk.Label(top1, width=30, font=('arial bold', 20),fg="black",bg="LightBlue4" ,text = "PEST PREDICTION SYSTEM",pady=20)
L.grid(row=1,column=2)

photo = tk.PhotoImage(file = r"C:\Users\samreen syeda\Desktop\FinalCode\images\upload.png")
photoimage = photo.subsample(4, 4) 
b2= tk.Button(top1,bg="white",fg="green",text="Upload to Training",bd=8,command=uploadtraining,image = photoimage,compound ="top")  
b2.config(width="100")
b2.config(height="100")
b2.grid(row=2,column=1,padx=20,pady=30)


photo2 = tk.PhotoImage(file = r"C:\Users\samreen syeda\Desktop\FinalCode\images\searches.png")
photoimage2 = photo2.subsample(4, 4) 
b3= tk.Button(top1,bg="white",fg="green",text="Upload For Testing",bd=8,command=uploadtesting,image = photoimage2,compound ="top" )
b3.config(width="100")
b3.config(height="100")  
b3.grid(row=2,column=2)

photo4 = tk.PhotoImage(file = r"C:\Users\samreen syeda\Desktop\FinalCode\images\blacklink.png")
photoimage4 = photo4.subsample(4, 4)
b5= tk.Button(top1,bg="white",fg="green",text="Prediction",bd=8,command=prediction,image = photoimage4,compound ="top" )
b5.config(width="100")
b5.config(height="100")   
b5.grid(row=2,column=3)

photo5 = tk.PhotoImage(file = r"C:\Users\samreen syeda\Desktop\FinalCode\images\showword.png")
photoimage5 = photo5.subsample(4, 4)
b6= tk.Button(top1,bg="white",fg="green",text="View Recommender\nDataset",bd=8,command=viewquestion,image = photoimage5,compound ="top"  )
b6.config(width="100")
b6.config(height="100")  
b6.grid(row=3,column=3)


photo3 = tk.PhotoImage(file = r"C:\Users\samreen syeda\Desktop\FinalCode\images\addword.png")
photoimage3 = photo3.subsample(4, 4) 
b4= tk.Button(top1,bg="white",fg="green",text="Add Recommender",bd=8,command=addquesion,image = photoimage3,compound ="top")
b4.config(width="100")
b4.config(height="100") 
b4.grid(row=3,column=2)


photo6 = tk.PhotoImage(file = r"C:\Users\samreen syeda\Desktop\FinalCode\images\excel.png")
photoimage6 = photo6.subsample(4, 4)
b7= tk.Button(top1,bg="white",fg="green",text="Upload Dataset\n(Excel)",bd=8,command=uploadfromexcel,image = photoimage6,compound ="top"  )
b7.config(width="100")
b7.config(height="100")  
b7.grid(row=3,column=1)


photo7 = tk.PhotoImage(file = r"C:\Users\samreen syeda\Desktop\FinalCode\images\logout.png")
photoimage7 = photo7.subsample(4, 4)
b8= tk.Button(top1,bg="white",fg="green",text="Log Out",bd=8,command=logout,image = photoimage7,compound ="top"  )
b8.config(width="100")
b8.config(height="100")  
b8.grid(row=5,column=2,padx=20,pady=30)
top1.mainloop()
