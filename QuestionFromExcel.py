# Program extracting all columns 
# name in Python 
import xlrd

import cv2
import pymysql
from tkinter.filedialog import askopenfile
import shutil, os
file = askopenfile(mode ='r')
name1 = os.path.basename(file.name)
print(name1)
loc = (name1) 
mydb=pymysql.connect(host="localhost",user="root",password="9405078366",database="pestprediction")
mycursor=mydb.cursor()

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
num_rows=sheet.nrows
num_col=sheet.ncols

print(num_rows)
print(num_col)
temp=""
rainfall=""
soil=""
light=""
ph=""
season=""
answer=""
for k in range(1,num_rows):
     sheet.cell_value(k, 0)
     print(sheet.cell_value(k, 0))
     temp=sheet.cell_value(k, 0)
     rainfall=sheet.cell_value(k, 1)
     soil=sheet.cell_value(k, 2)
     light=sheet.cell_value(k, 3)
     ph=sheet.cell_value(k, 4)
     season=sheet.cell_value(k, 5)
     answer=sheet.cell_value(k, 6)

     
     sql="insert into questions(temperature,rainfall,soil,light,ph,season,answer)values(%s,%s,%s,%s,%s,%s,%s)"
     values=(temp,rainfall,soil,light,ph,season,answer)
     mycursor.execute(sql,values)
     mydb.commit()
     print("row")

        
    
 
  

