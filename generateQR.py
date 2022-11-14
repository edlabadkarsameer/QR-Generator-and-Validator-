#sameer_edlabadkar
#Project_buddy
import xlsxwriter
import qrcode
from numpy import random
import sys
import os
import openpyxl
import csv
from tkinter import *
import sys
from PIL import ImageTk, Image
def generate_qr():
    n = Text_Area.get()
    p = Text_Area2.get()
    parent_dir = "C:\\Users\\edlab\\PycharmProjects\\QR\\"
    path = os.path.join(parent_dir, str(n))
    os.mkdir(path)
    print("Directory '% s' created" % str(n))
    x=random.randint(1024, size=(int (p)))
    workbook = xlsxwriter.Workbook(str(n)+".xlsx")
    worksheet = workbook.add_worksheet()
    row = 0
    column = 0
    for item in x:
        item = str(n)+str(item)
        worksheet.write(row, column, item)
        qr_img = qrcode.make(item)
        qr_img.save("C:\\Users\\edlab\\PycharmProjects\\QR\\"+str(n)+"\\"+ str(item)+".png")
        row += 1
    workbook.close()
    inputExcelFile = str(str(n)+".xlsx")
    newWorkbook = openpyxl.load_workbook(inputExcelFile)
    firstWorksheet = newWorkbook.active
    OutputCsvFile = csv.writer(open(str(str(n)+".csv"), 'w',newline=""))
    for eachrow in firstWorksheet.rows:
        OutputCsvFile.writerow([cell.value for cell in eachrow])
    print("successfully created the QRs")
    sys.exit()
if __name__=="__main__":
    root = Tk()
    root.geometry("500x300")
    root.configure(bg='#7F7FFF')
    root.title("QR Generator- Sameer Edlabadkar")
    Text_Area = StringVar()
    Text_Area2 = IntVar()
    img = ImageTk.PhotoImage(Image.open("pexels-gradienta-6985001.jpg"))
    label2 = Label(root, image=img)
    label2.pack()
    label = Label(root, text="Enter Name of project")
    label.place(x=185, y=90)
    Input = Entry(root, textvariable=Text_Area, width=30)
    Input.place(x=150, y=110)
    label = Label(root, text="Enter Number of QR")
    label.place(x=185, y=160)
    Input = Entry(root, textvariable=Text_Area2, width=30)
    Input.place(x=150, y=180)
    button = Button(root, text="Submit", command=generate_qr, bg="pink")
    button.place(x=210, y=210)
    n = Text_Area.get()
    p = Text_Area2.get()
    root.mainloop()

