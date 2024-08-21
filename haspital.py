from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        labeltitle=Label(self.root,relief=RIDGE, bd=20,text="HOSPITAL MANAGEMENT SYSYTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        labeltitle.pack(side=TOP,fill=X)

        #Frame

        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                            font=("times new roman",12,"bold"),text="Patient Information")
        dataframeleft.place(x=0,y=5,width=980,height=350)
        dataframerightt=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                            font=("times new roman",12,"bold"),text="Prescription")
        dataframerightt.place(x=990,y=5,width=500,height=350)


        #button frames
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

       #details frames

        Detailframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailframe.place(x=0,y=600,width=1530,height=190)

        lbname=Label(dataframeleft,text="Name of Tablet", font=("time new roman ",12,"bold"),padx=2,pady=6)
        lbname.grid(row=0,column=0)

        comName=ttk.Combobox(dataframeleft,font=("time new roman ",12,"bold"),
                             width=30)
        comName["values"]=("Nice","corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativian")
        comName.grid(row=0,column=1)

        lable1=Label(dataframeleft,font=("arial",12,"bold"),text="Refence No :",padx=4)
        lable1.grid(row=1,column=0,sticky=W)
        entry1=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry1.grid(row=1,column=1)

        lable1=Label(dataframeleft,font=("arial",12,"bold"),text="Dose :",padx=2,pady=6)
        lable1.grid(row=2,column=0,sticky=W)
        entry1=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry1.grid(row=2,column=1)


        lable1=Label(dataframeleft,font=("arial",12,"bold"),text="No of Tablets :",padx=2,pady=6)
        lable1.grid(row=3,column=0,sticky=W)
        entry1=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry1.grid(row=3,column=1)

        lable2=Label(dataframeleft,font=("arial",12,"bold"),text="Lot :",padx=2,pady=6)
        lable2.grid(row=4,column=0,sticky=W)
        entry2=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry2.grid(row=4,column=1)

        lable3=Label(dataframeleft,font=("arial",12,"bold"),text="Issue Date :",padx=2,pady=6)
        lable3.grid(row=5,column=0,sticky=W)
        entry3=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry3.grid(row=5,column=1)

        lable4=Label(dataframeleft,font=("arial",12,"bold"),text="Exp Date :",padx=2,pady=6)
        lable4.grid(row=6,column=0,sticky=W)
        entry4=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry4.grid(row=6,column=1)

        lable5=Label(dataframeleft,font=("arial",12,"bold"),text="Daily Dose :",padx=2,pady=6)
        lable5.grid(row=7,column=0,sticky=W)
        entry5=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry5.grid(row=7,column=1)

        lable6=Label(dataframeleft,font=("arial",12,"bold"),text="Side Effect :",padx=2,pady=6)
        lable6.grid(row=8,column=0,sticky=W)
        entry6=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry6.grid(row=8,column=1)

        lable7=Label(dataframeleft,font=("arial",12,"bold"),text="Further Information :",padx=20,pady=2)
        lable7.grid(row=0,column=2,sticky=W)
        entry7=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry7.grid(row=0,column=3)

        lable8=Label(dataframeleft,font=("arial",12,"bold"),text="Blood Pressure :",padx=20,pady=4)
        lable8.grid(row=1,column=2,sticky=W)
        entry8=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry8.grid(row=1,column=3)

        
        lable9=Label(dataframeleft,font=("arial",12,"bold"),text="Storage Advice :",padx=20,pady=6)
        lable9.grid(row=2,column=2,sticky=W)
        entry9=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry9.grid(row=2,column=3)

        
        lable10=Label(dataframeleft,font=("arial",12,"bold"),text="Medication :",padx=20,pady=6)
        lable10.grid(row=3,column=2,sticky=W)
        entry10=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry10.grid(row=3,column=3)


        lable11=Label(dataframeleft,font=("arial",12,"bold"),text="Patient Id :",padx=20,pady=6)
        lable11.grid(row=4,column=2,sticky=W)
        entry11=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry11.grid(row=4,column=3)
       
        lable12=Label(dataframeleft,font=("arial",12,"bold"),text="NHS Number :",padx=20,pady=6)
        lable12.grid(row=5,column=2,sticky=W)
        entry12=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry12.grid(row=5,column=3)

        lable13=Label(dataframeleft,font=("arial",12,"bold"),text="Patient Name :",padx=20,pady=6)
        lable13.grid(row=6,column=2,sticky=W)
        entry13=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry13.grid(row=6,column=3)

        lable14=Label(dataframeleft,font=("arial",12,"bold"),text="Date of Brith :",padx=20,pady=6)
        lable14.grid(row=7,column=2,sticky=W)
        entry14=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry14.grid(row=7,column=3)

        lable15=Label(dataframeleft,font=("arial",12,"bold"),text="Patient Address :",padx=20,pady=6)
        lable15.grid(row=8,column=2,sticky=W)
        entry15=Entry(dataframeleft,font=("arial",13,"bold"),width=32)
        entry15.grid(row=8,column=3)


     #datafram right

        self.txtPrescription=Text(dataframerightt,font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)











root=Tk()
ob=Hospital(root)
root.mainloop()

