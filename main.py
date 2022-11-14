# main module with tikinter window to start the program
from tkinter import *
import sys
import os
from PIL import ImageTk, Image
root=Tk()
root.geometry("500x300")
root.configure(bg='#7F7FFF')
root.title("QRbuddy-Sameer Edlabadkar")
def ticketCallBack():
    os.system('ticket.py')
def validateCallBack():
    os.system('validate.py')
def generateCallBack():
    os.system('generateQR.py')
img = ImageTk.PhotoImage(Image.open("pexels-gradienta-6985001.jpg"))
label = Label(root, image = img)
label.pack()
button1=Button(root,text="Ticket Generator",command=ticketCallBack,bg="white")
button1.place(x=200,y=100)
button2=Button(root,text="Validate QR",command=validateCallBack,bg="white")
button2.place(x=211,y=130)
button3=Button(root,text="Generate QR",command=generateCallBack,bg="white")
button3.place(x=209,y=160)
root.mainloop()


