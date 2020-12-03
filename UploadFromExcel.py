# Program extracting all columns 
# name in Python 
import xlrd 
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
imagename=""
disease=""
prediction=""
for k in range(1,num_rows):
     sheet.cell_value(k, 0)
     print(sheet.cell_value(k, 0))
     imagename=sheet.cell_value(k, 0)
     disease=sheet.cell_value(k, 1)
     prediction=sheet.cell_value(k, 2)
     sql="insert into dataset (imagename,disease,description)values(%s,%s,%s)"
     values=(imagename,disease,prediction)
     mycursor.execute(sql,values)
     mydb.commit()
     print("row")

        
    
 
  

