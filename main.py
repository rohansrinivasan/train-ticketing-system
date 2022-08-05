from Tkinter import *
import pickle
import os
import random
import time
#====================MAIN WINDOW============================
root = Tk()
root.geometry("1600x800+0+0")
root.title("Railway Management System")

Tops=Frame(root, width = 1600,height = 50, bg="powder blue" , relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root, width = 800, height = 700, bg="powder blue" , relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root, width = 300, height = 700,bg="powder blue" , relief=SUNKEN)
f2.pack(side=RIGHT)

#========================TIME==================================
localtime=time.asctime(time.localtime(time.time()))

linfo=Label(Tops, font=('times new roman',50,"bold","italic"), text="TICKET RESERVATION SYSTEM", fg="steel blue", bd=10, anchor='w')  
linfo.grid(row=0,column=0)

linfo=Label(Tops, font=('times new roman',20,"bold","italic"), text=localtime, fg="steel blue", bd=10, anchor='w')  
linfo.grid(row=1,column=0)

 
#=====================PASSENGER DETAILS=======================
passname = StringVar()
fstat = StringVar()
tstat = StringVar()
doj = StringVar()
gender = StringVar()
tno = StringVar()
pnr = StringVar()
seatno = StringVar()

lname=Label(f1, font=('times new roman',16,"bold","italic"),text="Passenger Name", bd=16, anchor='w')
lname.grid(row=0,column=0)
txtname=Entry(f1,font=('times new roman',16,"bold","italic"),textvariable=passname, bd=10, insertwidth=4,
                   bg="powder blue", justify="right")
txtname.grid(row=0,column=1)

lfrom=Label(f1, font=('times new roman',16,"bold","italic"),text="Journey From Station", bd=16, anchor='w')
lfrom.grid(row=1,column=0)
txtfrom=Entry(f1,font=('times new roman',16,"bold","italic"),textvariable=fstat, bd=10, insertwidth=4,
                   bg="powder blue", justify="right")
txtfrom.grid(row=1,column=1)

lto=Label(f1, font=('times new roman',16,"bold","italic"),text="To Which Station", bd=16, anchor='w')
lto.grid(row=2,column=0)
txtto=Entry(f1,font=('times new roman',16,"bold","italic"),textvariable=tstat, bd=10, insertwidth=4,
                   bg="powder blue", justify="right")
txtto.grid(row=2,column=1)

ldoj=Label(f1, font=('times new roman',16,"bold","italic"),text="Date Of Journey", bd=16, anchor='w')
ldoj.grid(row=3,column=0)
txtdoj=Entry(f1,font=('times new roman',16,"bold","italic"),textvariable=doj, bd=10, insertwidth=4,
                   bg="powder blue", justify="right")
txtdoj.grid(row=3,column=1)

lgender=Label(f1, font=('times new roman',16,"bold","italic"),text="Enter Gender", bd=16, anchor='w')
lgender.grid(row=4,column=0)
txtgender=Entry(f1,font=('times new roman',16,"bold","italic"),textvariable=gender, bd=10, insertwidth=4,
                   bg="powder blue", justify="right")
txtgender.grid(row=4,column=1)

ltno=Label(f1, font=('times new roman',16,"bold","italic"),text="Train Number", bd=16, anchor='w')
ltno.grid(row=5,column=0)
txttno=Entry(f1,font=('times new roman',16,"bold","italic"),textvariable=tno, bd=10, insertwidth=4,
                   bg="powder blue", justify="right")
txttno.grid(row=5,column=1)

lpnrno=Label(f1, font=('times new roman',16,"bold","italic"),text="PNR Number", bd=16, anchor='w')
lpnrno.grid(row=6,column=0)
txtpnrno=Entry(f1,font=('times new roman',16,"bold","italic"),textvariable=pnr, bd=10, insertwidth=4,
                   bg="powder blue", justify="right")
txtpnrno.grid(row=6,column=1)


#=====================FUNCTIONS================================
def pass_details():
    global pnr
    global passname
    global fstat
    global tsat
    global doj
    global gender
    global tno
    x = random.randint(10000,99999)
    randompnr = str(x)
    pnr.set(randompnr)
    passname.set(txtname.get())
    fstat.set(txtfrom.get())
    tstat.set(txtto.get())
    doj.set(txtdoj.get())
    gender.set(txtgender.get())
    tno.set(txttno.get())
    print ("=====================#@#=====================")
    print ("YOUR TICKET HAS BEEN SUCCESSFULLY RESERVED")
    print ("=====================#@#=====================")  
    
def display_details():
    global e1
    global e2
    pnr.get()
    master = Tk()
    master.title("Check Details")
    label1= Label (master, text="Enter Passenger Name").grid(row=0)
    label2= Label (master, text="Enter PNR number").grid(row=1)
    e1 = Entry(master)
    e2 = Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

 
def printSomething():
    global seatno
    sn=random.randint(1,99)
    randomseatno = str(sn)
    seatno.set(randomseatno)
    if e1.get()==passname.get() and e2.get()==pnr.get():
        print ("====================#@# ROYAL TRAVELS #@#========================")
        print ("YOUR DETAILS ARE:")
        print ("---------------------------")
        print ("===========================")
        print ("Passenger Name:",passname.get()) 
        print ("Journey From Station:",fstat.get()) 
        print ("Journey To Station:",tstat.get())
        print ("Date Of Journey:",doj.get())
        print ("Gender:",gender.get())
        print ("Ticket Number:",tno.get())
        print ("Seat Number:",seatno.get())
        print ("PNR Number:",pnr.get())
        print ("===========================")
        print ("---------------------------")
    else :
       print ("====================#@# ROYAL TRAVELS #@#========================")
       print ("Your Name Or PNR Number Is Incorrect!")

def cancel():
    global q1
    global q2
    pnr.get()
    passname.get()
    masters = Tk()
    masters.title("Delete Details")
    labels1= Label (masters, text="Enter Passenger Name").grid(row=0)
    labels2= Label (masters, text="Enter PNR number").grid(row=1)
    q1 = Entry(masters)
    q2 = Entry(masters)
    q1.grid(row=0, column=1)
    q2.grid(row=1, column=1)
 
def buttoncancel():
    if q1.get()==passname.get() and q2.get()==pnr.get():
        pnr.set('')
        passname.set('')
        fstat.set('')
        tstat.set('')
        doj.set('')
        gender.set('')
        tno.set('')
        print ("====================#@# ROYAL TRAVELS #@#========================")
        print ("Your Ticket Has Been Cancelled")
        

#=================================BUTTONS===================================
btnDetails=Button(f2,padx=16, pady=8, bd=16, fg="black",font=('times new roman',16,"bold","italic"), width=10,
                  text="Passenger Detail",bg="powder blue", command = pass_details).grid(row=0, column=1)

btnDetails=Button(f2,padx=16, pady=8, bd=16, fg="black",font=('times new roman',16,"bold","italic"), width=10,
                  text="Display Details",bg="powder blue", command = display_details).grid(row=1, column=1)

btnDetails=Button(f2,padx=16, pady=8, bd=16, fg="black",font=('times new roman',16,"bold","italic"), width=10,
                  text="Check Details",bg="powder blue", command = printSomething).grid(row=2, column=1)

btnDetails=Button(f2,padx=16, pady=8, bd=16, fg="black",font=('times new roman',16,"bold","italic"), width=10,
                  text="Cancel Ticket",bg="powder blue", command = cancel).grid(row=3, column=1)

btnDetails=Button(f2,padx=16, pady=8, bd=16, fg="black",font=('times new roman',16,"bold","italic"), width=10,
                  text="Confirm Cancel",bg="powder blue", command = buttoncancel).grid(row=4, column=1)


root.mainloop()

