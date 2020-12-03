import tkinter as tk
import pymysql
import sys
import os
import gc
import cv2
from tkinter.filedialog import askopenfile
from subprocess import Popen
from tkinter import messagebox
from subprocess import call
from PIL import ImageTk, Image
mydb=pymysql.connect(host="localhost",user="root",password="root",database="maliciousurl")
mycursor=mydb.cursor()

top1=tk.Tk()
top1.title("Admin Dashboard")
width = 600
height = 700
screen_width = top1.winfo_screenwidth()
screen_height = top1.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
top1.geometry("%dx%d+%d+%d" % (width, height, x, y))
top1.config(bg="grey")

path = 'D:\Abstract and Details 2017\Pest Controll System using python\FinalCode\images\a1.jpg'


img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(top1, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.grid(row=1,column=1)



top1.mainloop()
