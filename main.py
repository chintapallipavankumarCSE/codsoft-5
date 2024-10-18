from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from Attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        img1 = Image.open(r"Images/girl_ai.jpg")
        img1 = img1.resize((500,130),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img2 = Image.open(r"Images/recognize_ai.jpg")
        img2 = img2.resize((500,130),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        img3 = Image.open(r"Images/brain_ai.jpg")
        img3 = img3.resize((500,130),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        # Back Ground Image

        img4 = Image.open(r"C:\Users\99220\OneDrive\Desktop\FACE RECOGNITION SYSTEM\background.jpg")
        img4 = img4.resize((1530,710),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg='white',fg='darkgreen')
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #******* TIME ***********
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font=("times new roman",14,"bold"),bg='white',fg='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        # Student button
    

        img5 = Image.open(r"C:\Users\99220\OneDrive\Desktop\FACE RECOGNITION SYSTEM\Images\std1.jpg")
        img5 = img5.resize((220,220),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text = "Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg='dark blue',fg='white')
        b1_1.place(x=200,y=300,width=220,height=40)

        #Detect Face button

        img6 = Image.open(r"C:\Users\99220\OneDrive\Desktop\FACE RECOGNITION SYSTEM\Images\f_det.jpg")
        img6 = img6.resize((220,220),Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b2_2 = Button(bg_img,text = "Face Recognition",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg='dark blue',fg='white')
        b2_2.place(x=500,y=300,width=220,height=40)

        #Attendance button

        img7 = Image.open(r"C:\Users\99220\OneDrive\Desktop\FACE RECOGNITION SYSTEM\Images\att.jpg")
        img7 = img7.resize((220,220),Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b3 = Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=100,width=220,height=220)

        b3_3 = Button(bg_img,text = "Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg='dark blue',fg='white')
        b3_3.place(x=800,y=300,width=220,height=40)

        #Help button

        img8 = Image.open(r"C:\Users\99220\OneDrive\Desktop\FACE RECOGNITION SYSTEM\Images\hlp.jpg")
        img8 = img8.resize((220,220),Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b4 = Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data)
        b4.place(x=1100,y=100,width=220,height=220)

        b4_4 = Button(bg_img,text = "Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg='dark blue',fg='white')
        b4_4.place(x=1100,y=300,width=220,height=40)

        #Train data button

        img9 = Image.open(r"C:\Users\99220\OneDrive\Desktop\FACE RECOGNITION SYSTEM\Images\bg.png")
        img9 = img9.resize((220,220),Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b5 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data,)
        b5.place(x=200,y=380,width=220,height=220)

        b5_5 = Button(bg_img,text = "Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg='dark blue',fg='white')
        b5_5.place(x=200,y=580,width=220,height=40)

        #Photos

        img10 = Image.open(r"C:\Users\99220\OneDrive\Desktop\FACE RECOGNITION SYSTEM\Images\profile.png")
        img10 = img10.resize((220,220),Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b6 = Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=380,width=220,height=220)

        b6_6 = Button(bg_img,text = "Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg='dark blue',fg='white')
        b6_6.place(x=500,y=580,width=220,height=40)

        #Develeoper Button

        img11 = Image.open(r"C:\Users\99220\OneDrive\Desktop\FACE RECOGNITION SYSTEM\Images\dev.jpg")
        img11 = img11.resize((220,220),Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b7 = Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b7.place(x=800,y=380,width=220,height=220)

        b7_7 = Button(bg_img,text = "Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg='dark blue',fg='white')
        b7_7.place(x=800,y=580,width=220,height=40)

        #Exit Button

        img12 = Image.open(r"C:\Users\99220\OneDrive\Desktop\FACE RECOGNITION SYSTEM\Images\exi.jpg")
        img12 = img12.resize((220,220),Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b8 = Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.iExit)
        b8.place(x=1100,y=380,width=220,height=220)

        b8_8 = Button(bg_img,text = "Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg='dark blue',fg='white')
        b8_8.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return



    #***********FUNCTION*******************
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()