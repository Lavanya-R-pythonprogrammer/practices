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

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.Numberoftablets=StringVar()
        self.lot=StringVar()
        self.issuedate=StringVar()
        self.expdate=StringVar()
        self.dailydose=StringVar()
        self.sideeffects=StringVar()
        self.furtherinformation=StringVar()
        self.drivingusingmachine=StringVar()
        self.strorageadivce=StringVar()
        self.medication=StringVar()
        self.patineid=StringVar()
        self.nhsnumber=StringVar()
        self.patientname=StringVar()
        self.dateofbrith=StringVar()
        self.patientaddress=StringVar()


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

        comName=ttk.Combobox(dataframeleft,textvariable=self.Nameoftablets,state="readonly",font=("time new roman ",12,"bold"),
                             width=30)
        comName["values"]=("Nice","corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativian")
        comName.grid(row=0,column=1)

        lable16=Label(dataframeleft,font=("arial",12,"bold"),text="Refence No :",padx=4)
        lable16.grid(row=1,column=0,sticky=W)
        entry16=Entry(dataframeleft,textvariable=self.ref,font=("arial",13,"bold"),width=32)
        entry16.grid(row=1,column=1)

        lable17=Label(dataframeleft,font=("arial",12,"bold"),text="Dose :",padx=2,pady=6)
        lable17.grid(row=2,column=0,sticky=W)
        entry17=Entry(dataframeleft,textvariable=self.Dose,font=("arial",13,"bold"),width=32)
        entry17.grid(row=2,column=1)


        lable1=Label(dataframeleft,font=("arial",12,"bold"),text="No of Tablets :",padx=2,pady=6)
        lable1.grid(row=3,column=0,sticky=W)
        entry1=Entry(dataframeleft,textvariable=self.Numberoftablets,font=("arial",13,"bold"),width=32)
        entry1.grid(row=3,column=1)

        lable2=Label(dataframeleft,font=("arial",12,"bold"),text="Lot :",padx=2,pady=6)
        lable2.grid(row=4,column=0,sticky=W)
        entry2=Entry(dataframeleft,textvariable=self.lot,font=("arial",13,"bold"),width=32)
        entry2.grid(row=4,column=1)

        lable3=Label(dataframeleft,font=("arial",12,"bold"),text="Issue Date :",padx=2,pady=6)
        lable3.grid(row=5,column=0,sticky=W)
        entry3=Entry(dataframeleft,textvariable=self.issuedate,font=("arial",13,"bold"),width=32)
        entry3.grid(row=5,column=1)

        lable4=Label(dataframeleft,font=("arial",12,"bold"),text="Exp Date :",padx=2,pady=6)
        lable4.grid(row=6,column=0,sticky=W)
        entry4=Entry(dataframeleft,textvariable=self.expdate,font=("arial",13,"bold"),width=32)
        entry4.grid(row=6,column=1)

        lable5=Label(dataframeleft,font=("arial",12,"bold"),text="Daily Dose :",padx=2,pady=6)
        lable5.grid(row=7,column=0,sticky=W)
        entry5=Entry(dataframeleft,textvariable=self.dailydose,font=("arial",13,"bold"),width=32)
        entry5.grid(row=7,column=1)

        lable6=Label(dataframeleft,font=("arial",12,"bold"),text="Side Effect :",padx=2,pady=6)
        lable6.grid(row=8,column=0,sticky=W)
        entry6=Entry(dataframeleft,textvariable=self.sideeffects,font=("arial",13,"bold"),width=32)
        entry6.grid(row=8,column=1)

        lable7=Label(dataframeleft,font=("arial",12,"bold"),text="Further Information :",padx=20,pady=2)
        lable7.grid(row=0,column=2,sticky=W)
        entry7=Entry(dataframeleft,textvariable=self.furtherinformation,font=("arial",13,"bold"),width=32)
        entry7.grid(row=0,column=3)

        lable8=Label(dataframeleft,font=("arial",12,"bold"),text="Blood Pressure :",padx=20,pady=4)
        lable8.grid(row=1,column=2,sticky=W)
        entry8=Entry(dataframeleft,textvariable=self.drivingusingmachine,font=("arial",13,"bold"),width=32)
        entry8.grid(row=1,column=3)

        
        lable9=Label(dataframeleft,font=("arial",12,"bold"),text="Storage Advice :",padx=20,pady=6)
        lable9.grid(row=2,column=2,sticky=W)
        entry9=Entry(dataframeleft,textvariable=self.strorageadivce,font=("arial",13,"bold"),width=32)
        entry9.grid(row=2,column=3)

        
        lable10=Label(dataframeleft,font=("arial",12,"bold"),text="Medication :",padx=20,pady=6)
        lable10.grid(row=3,column=2,sticky=W)
        entry10=Entry(dataframeleft,textvariable=self.medication,font=("arial",13,"bold"),width=32)
        entry10.grid(row=3,column=3)


        lable11=Label(dataframeleft,font=("arial",12,"bold"),text="Patient Id :",padx=20,pady=6)
        lable11.grid(row=4,column=2,sticky=W)
        entry11=Entry(dataframeleft,textvariable=self.patineid,font=("arial",13,"bold"),width=32)
        entry11.grid(row=4,column=3)
       
        lable12=Label(dataframeleft,font=("arial",12,"bold"),text="NHS Number :",padx=20,pady=6)
        lable12.grid(row=5,column=2,sticky=W)
        entry12=Entry(dataframeleft,textvariable=self.nhsnumber,font=("arial",13,"bold"),width=32)
        entry12.grid(row=5,column=3)

        lable13=Label(dataframeleft,font=("arial",12,"bold"),text="Patient Name :",padx=20,pady=6)
        lable13.grid(row=6,column=2,sticky=W)
        entry13=Entry(dataframeleft,textvariable=self.patientname,font=("arial",13,"bold"),width=32)
        entry13.grid(row=6,column=3)

        lable14=Label(dataframeleft,font=("arial",12,"bold"),text="Date of Brith :",padx=20,pady=6)
        lable14.grid(row=7,column=2,sticky=W)
        entry14=Entry(dataframeleft,textvariable=self.dateofbrith,font=("arial",13,"bold"),width=32)
        entry14.grid(row=7,column=3)

        lable15=Label(dataframeleft,font=("arial",12,"bold"),text="Patient Address :",padx=20,pady=6)
        lable15.grid(row=8,column=2,sticky=W)
        entry15=Entry(dataframeleft,textvariable=self.patientaddress,font=("arial",13,"bold"),width=32)
        entry15.grid(row=8,column=3)


     #datafram right

        self.txtPrescription=Text(dataframerightt,font=("arial",12,"bold"),width=51,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #buttons
        

        btn1=Button(Buttonframe,command=self.iPrecscription,text="Prescription",bg="green",fg="white" ,font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btn1.grid(row=0,column=0)

        btn2=Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="green",fg="white" ,font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btn2.grid(row=0,column=1)

        btn3=Button(Buttonframe,command=self.update_data,text="Update",bg="green",fg="white" ,font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btn3.grid(row=0,column=2)

        btn4=Button(Buttonframe,command=self.delete1,text="Delete",bg="green",fg="white" ,font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btn4.grid(row=0,column=3)

        btn5=Button(Buttonframe,text="clear",bg="green",fg="white" ,font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btn5.grid(row=0,column=4)

        btn6=Button(Buttonframe,text="Exit",bg="green",fg="white" ,font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btn6.grid(row=0,column=5)

        # table

        scroll1=ttk.Scrollbar(Detailframe,orient=HORIZONTAL)
        scroll2=ttk.Scrollbar(Detailframe,orient=VERTICAL)
        self.Hospital1_table=ttk.Treeview(Detailframe,column=("nameoftable","ref","dose","nooftablets","lot","issuedate",
                                                           "expdate","dailydose","storage","nbsnumber","pname","dob","address"),
                                                           xscrollcommand=scroll1.set,yscrollcommand=scroll2.set)  
        scroll1.pack(side=BOTTOM,fill=X)
        scroll2.pack(side=RIGHT,fill=Y)

        scroll1=ttk.Scrollbar(command=self.Hospital1_table.xview)
        scroll2=ttk.Scrollbar(command=self.Hospital1_table.yview)

        self.Hospital1_table.heading("nameoftable",text="Name of Table")
        self.Hospital1_table.heading("ref",text="Reference No")
        self.Hospital1_table.heading("dose",text="Dose")
        self.Hospital1_table.heading("nooftablets",text="No Of Tablets")
        self.Hospital1_table.heading("lot",text="Lot")
        self.Hospital1_table.heading("issuedate",text="Issue Date")
        self.Hospital1_table.heading("expdate",text="Exp Date")
        self.Hospital1_table.heading("dailydose",text="Daily Dose")
        self.Hospital1_table.heading("storage",text="Storage")
        self.Hospital1_table.heading("nbsnumber",text="NHS Number")
        self.Hospital1_table.heading("pname",text="Patient Number")
        self.Hospital1_table.heading("dob",text="Date of Birth")
        self.Hospital1_table.heading("address",text="Address")

        self.Hospital1_table["show"]="headings"
         

        self.Hospital1_table.column("nameoftable", width=100)
        self.Hospital1_table.column("ref", width=100)
        self.Hospital1_table.column("dose", width=100)
        self.Hospital1_table.column("nooftablets", width=100)
        self.Hospital1_table.column("lot", width=100)
        self.Hospital1_table.column("issuedate", width=100)
        self.Hospital1_table.column("expdate", width=100)
        self.Hospital1_table.column("dailydose", width=100)
        self.Hospital1_table.column("storage", width=100)
        self.Hospital1_table.column("nbsnumber", width=100)
        self.Hospital1_table.column("pname", width=100)
        self.Hospital1_table.column("dob", width=100)
        self.Hospital1_table.column("address", width=100)
        self.Hospital1_table.pack(fill=BOTH,expand=1)
        self.Hospital1_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        #functionality declaration

    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","ALL fields are requried")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="dakshika") 
            my_cursor=conn.cursor()
            my_cursor.execute("insert into Hospital values(%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                           self.Nameoftablets.get(),
                                                                                                           self.ref.get(),
                                                                                                           self.Dose.get(),
                                                                                                           self.Numberoftablets.get(),
                                                                                                           self.lot.get(),
                                                                                                           self.issuedate.get(),
                                                                                                           self.expdate.get(),
                                                                                                           self.dailydose.get(),
                                                                                                           self.sideeffects.get(),
                                                                                                           self.furtherinformation.get(),
                                                                                                           self.drivingusingmachine.get(),
                                                                                                           self.strorageadivce.get(),
                                                                                                           self.medication.get(),
                                                                                                           self.patineid.get(),
                                                                                                           self.nhsnumber.get(),
                                                                                                           self.patientname.get(),
                                                                                                           self.dateofbrith.get(),
                                                                                                           self.patientaddress.get()
            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("success","record has been instered")

    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="dakshika") 
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Nameoftables=%s,Dose=%s, Numberoftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, sideeffects=%s, furtherinformation=%s, drivangusingmachine=%s, storageadvice=%s, medication=%s, patinetid=%s, nhsnumber=%s, patientname=%s, dateofbrith=%s, patientaddress=%s  where ref=%s",(
                                                                                                           
                                                                                                           self.Nameoftablets.get(),
                                                                                                           self.Dose.get(),
                                                                                                           self.Numberoftablets.get(),
                                                                                                           self.lot.get(),
                                                                                                           self.issuedate.get(),
                                                                                                           self.expdate.get(),
                                                                                                           self.dailydose.get(),
                                                                                                           self.sideeffects.get(),
                                                                                                           self.furtherinformation.get(),
                                                                                                           self.drivingusingmachine.get(),
                                                                                                           self.strorageadivce.get(),
                                                                                                           self.medication.get(),
                                                                                                           self.patineid.get(),
                                                                                                           self.nhsnumber.get(),
                                                                                                           self.patientname.get(),
                                                                                                           self.dateofbrith.get(),
                                                                                                           self.patientaddress.get(),
                                                                                                           self.ref.get(),
        
          ))
        conn.commit()
        conn.close() 
        messagebox.showinfo("success","record has been updated")    













    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="dakshika") 
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Hospital1_table.delete(*self.Hospital1_table.get_children())
            for i in rows:
                self.Hospital1_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event):
        cursor_row=self.Hospital1_table.focus()
        content=self.Hospital1_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.Numberoftablets.set(row[3])
        self.lot.set(row[4])
        self.issuedate.set(row[5])
        self.expdate.set(row[6])
        self.dailydose.set(row[7])
        self.sideeffects.set(row[8])
        self.furtherinformation.set(row[9])
        self.drivingusingmachine.set(row[10])
        self.strorageadivce.set(row[11])
        self.medication.set(row[12])
        self.patineid.set(row[13])
        self.nhsnumber.set(row[14])
        self.patientname.set(row[15])
        self.dateofbrith.set(row[16])
        self.patientaddress.set(row[17])

    def iPrecscription(self):
        self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"ef no:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"lot:\t\t\t"+self.lot.get()+"\n")
        self.txtPrescription.insert(END,"issuedate:\t\t\t"+self.issuedate.get()+"\n")
        self.txtPrescription.insert(END,"expdate:\t\t\t"+self.expdate.get()+"\n")
        self.txtPrescription.insert(END,"dailydose:\t\t\t"+self.dailydose.get()+"\n")
        self.txtPrescription.insert(END,"sideeffects:\t\t\t"+self.sideeffects.get()+"\n")
        self.txtPrescription.insert(END,"further information:\t\t\t"+self.furtherinformation.get()+"\n")
        self.txtPrescription.insert(END,"drivingusingmachine:\t\t\t"+self.drivingusingmachine.get()+"\n")
        self.txtPrescription.insert(END,"strorageadivce\t\t\t"+self.strorageadivce.get()+"\n")
        self.txtPrescription.insert(END,"medication:\t\t\t"+self.medication.get()+"\n")
        self.txtPrescription.insert(END,"patineid:\t\t\t"+self.patineid.get()+"\n")
        self.txtPrescription.insert(END,"nhsnumber:\t\t\t"+self.nhsnumber.get()+"\n")
        self.txtPrescription.insert(END,"atientname:\t\t\t"+self.patientname.get()+"\n")
        self.txtPrescription.insert(END,"dateofbrith:\t\t\t"+self.dateofbrith.get()+"\n")
        self.txtPrescription.insert(END,"patientaddress:\t\t\t"+self.patientaddress.get()+"\n")
        
    def delete1(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="dakshika") 
        my_cursor=conn.cursor()
        query="delete from hospital where ref=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("deleted data")                                                                                                   
                                          
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                                                                                           
                                        

                 








                                     
                                     
                                     
                                     
                                     
                                     
                                     
                                




    











root=Tk()
ob=Hospital(root)
root.mainloop()

