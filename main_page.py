from  tkinter import *
from  tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector
import datetime


def first():
    def login():
        us = user.get()
        ps = pswd.get()
        conn = mysql.connector.connect(host='localhost', user='root', password='password', db='data')
        a = conn.cursor()
        a.execute("select * from login where username='" + us + "' and password = '" + ps + "'")
        results = a.fetchall()
        if len(results) > 0:
            win.destroy()
            open_main()
        else:
            messagebox.showinfo("message","Wrong username or password")
        conn.close()

    global win  
    win=Tk()
    win.overrideredirect(True)
    win.overrideredirect(False)
    win.attributes('-fullscreen',False)

    win.title("windows application")
    win.configure(bg='gray')
    load = Image.open('icon\\i8.png')
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0)

    #top frame
    topframe=Frame(win,width=1800,height=900,bg="pink",bd=10,relief="raise")
    topframe.pack(side=TOP)
    lb=Label(topframe,font=('arial',45,'bold'),fg="pink",bg="brown",text='LIBRARY MANAGEMENT SYSTEM', width=30)
    lb.grid(row=0,column=0)

    #middle frame
    mframe=Frame(win,bg="brown",bd=10,relief='raise', padx=30, pady=100)
    mframe.pack(padx=500,pady=40)

    lbl1 = Label(mframe, text='User name',font=('arial',12,'bold'),fg="pink",bg="brown")
    lbl1.grid(row=0, column=0,pady=10)
    user=StringVar()
    e1 = Entry(mframe,textvariable = user)
    e1.grid(row=0, column=1, padx=10)

    lbl2 = Label(mframe, text='Password',font=('arial',12,'bold'),fg="pink",bg="brown")
    lbl2.grid(row=1, column=0, pady=10)
    pswd=StringVar()
    e2 = Entry(mframe,textvariable = pswd)
    e2.grid(row=1, column=1, padx=10)

    closemain = Button(mframe, font=('arial',12,'bold'), bg='brown',text='Close Main',fg="pink",command=win.destroy)
    closemain.grid(row=2, column=0, padx=10)

    e3 = Button(mframe, text='Log in', font=('arial',12,'bold'),fg="pink",bg="brown",command=login)
    e3.grid(row=2, column=1, padx=10)

    win.mainloop()

def open_return():
    def return_():
        bknm = bknum.get()
        try:
            conn=mysql.connector.connect(host='localhost',user='root',password='password',db='data')
            a=conn.cursor()
            a.execute("select * from issuebook where bookno='"+bknm+"'")
            resultb = b.fetchall()
            countb = b.rowcount
            print(resultb)
            print(countb)
            if countb > 0:
                a.execute("delete from issuebook where bookno='"+bknm+"'")
                conn.commit()
            else:
            # print('delete')
                messagebox.showinfo("message","delete")
        except:
            conn.rollback()
            # print('not delete')
            messagebox.showinfo("message","not delete")
        conn.close()
    global win    
    win=Tk()
    win.title("windows application")
    win.configure(bg='gray')
    load = Image.open('icon\\i1.png')
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0)

    #middle frame
    mframe=Frame(win,width=800,height=800,bg="brown",bd=10,relief='raise', padx=40, pady=30)
    mframe.pack(padx=50,pady=70)

    lbl1 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Book Number :')
    lbl1.grid(row=0, column=0)
    bknum=StringVar()
    e1 = Entry(mframe)
    e1.grid(row=0, column=1, padx=10)

    exitmain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='GO TO Main',fg="pink",command=open_main)
    exitmain.grid(row=3, column=0, padx=10)
    closemain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='Close',fg="pink",command=win.destroy)
    closemain.grid(row=3, column=2, padx=10)


    e3 = Button(mframe, text='Submit', font=('arial',14,'bold'),fg="pink",bg="brown",command=return_)
    e3.grid(row=3, column=1, pady=10)


    win.mainloop()

def open_issue():
    win.destroy()
    def issue_book():
        rollnum = rnum.get()
        bknum=booknum.get()
        datofiss=dateofiss.get()
        lastdateret=lstdate.get()

        if(rollnum!='' or bknum!='' or datofiss!='' or lastdateret!=''):
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='password', db='data')
                a = conn.cursor()
                a.execute("insert into issuebook(rollno,bookno,issuedate,returndate)values('"
                    +rollnum+"','"+bknum+"','"+datofiss+"','"+lastdateret+"')")

                a.execute("SELECT * FROM books where bookno='"+bknum+"'")
                booknm.set(row[0])
                bkname=booknm.get()
                a.execute("Update issuebook set bookname='"+bkname+"'  WHERE bookno'"+bknum+"'")
                conn.commit()
                print('save')
                messagebox.showinfo("message","Book Issued")
            except:
                conn.rollback()
                print('Not Save')
                messagebox.showinfo("message", "Book Not Issued")
                conn.close()
        else:
            messagebox.showinfo("message", "Please Enter Some values")
    global win
    win=Tk()
    win.overrideredirect(True)
    win.overrideredirect(False)
    win.attributes('-fullscreen',False)
    win.title("windows application")
    win.configure(bg='gray')
    load = Image.open('icon\\i2.png')
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0)


    #middle frame
    mframe=Frame(win,width=800,height=800,bg="brown",bd=10,relief='raise', padx=50, pady=30)
    mframe.pack(padx=50,pady=100)

    lbl1 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Roll Number :')
    lbl1.grid(row=0, column=0)
    rnum=StringVar()
    e1 = Entry(mframe,textvariable=rnum)
    e1.grid(row=0, column=1, padx=10)

    lbl2 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Book Name :')
    lbl2.grid(row=1, column=0, pady=10)
    booknm=StringVar()
    e2 = Entry(mframe,textvariable=booknm)
    e2.grid(row=1, column=1, padx=10)

    lbl3 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Book Number :')
    lbl3.grid(row=2, column=0, pady=10)
    booknum=StringVar()
    e3 = Entry(mframe,textvariable=booknum)
    e3.grid(row=2, column=1, padx=10)

    lbl4 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Date of Issue :')
    lbl4.grid(row=3, column=0, pady=10)
    dateofiss=StringVar()
    e4 = Entry(mframe,textvariable=dateofiss)
    e4.grid(row=3, column=1, padx=10)

    lbl5 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Last Date to return :')
    lbl5.grid(row=4, column=0, pady=10)
    lstdate=StringVar()
    e5 = Entry(mframe,textvariable=lstdate)
    e5.grid(row=4, column=1, padx=10)

    exitmain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='GO TO Main',fg="pink",command=open_main)
    exitmain.grid(row=5, column=0, padx=10)
    closemain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='Close',fg="pink",command=win.destroy)
    closemain.grid(row=5, column=2, padx=10)

    e6 = Button(mframe, text='Submit', font=('arial',14,'bold'), bg="brown",command=issue_book)
    e6.grid(row=5, column=1, pady=10)


    win.mainloop()

    
def open_details():
    win.destroy()
    def details():
        rollnum = rnum.get()
        print(rollnum)
        conn = mysql.connector.connect(host='localhost', user='root', password='password', db='data')
        a = conn.cursor()
        a.execute("select * from student where rollno='"+rollnum+"'")

        results = a.fetchall()
        count = a.rowcount

        print(results)

        print(count)

        if count > 0:
            for row in results:
                rnum1.set(row[0])
                sname.set(row[1])
                fanm.set(row[2])
                mtnm.set(row[3])
                dateob.set(row[4])
                bran.set(row[5])
        else:
            messagebox.showinfo("record not found")
        conn.close()

    def bookdetails():
        rollnum = rnum.get()
        print(rollnum)
        conn = mysql.connector.connect(host='localhost', user='root', password='password', db='data')
        b = conn.cursor()
        b.execute("select * from issuebook where rollno='" + rollnum + "'")
        resultb = b.fetchall()
        countb = b.rowcount
        print(resultb)
        print(countb)
        if countb > 0:
            for row in resultb:
                booknm.set(row[1])
                booknum.set(row[2])
                dateofiss.set(row[3])
                lstdate.set(row[4])

        else:
            messagebox.showinfo("record not found")
        conn.close()
    def details_and_bookdetails():
        details()
        bookdetails()
    global win
    win=Tk()
    win.overrideredirect(True)
    win.overrideredirect(False)
    win.attributes('-fullscreen',False)
    win.title("windows application")
    win.configure(bg='gray')
    load = Image.open('icon\\i3.png')
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0)
    #top frame
    topframe=Frame(win,width=4600,height=3500,bg="pink",bd=10,relief="raise")
    topframe.pack(side=TOP)
    lb=Label(topframe,font=('arial',30,'bold'),fg="pink",bg="brown",text='Students Detail', width=40)
    lb.grid(row=0,column=0)

    rframe=Frame(win,bg="brown",bd=10,relief='raise', padx=10, pady=10)
    rframe.pack(padx=5,pady=5)
    labelroll = Label(rframe,font=('arial',14,'bold'), bg='brown', text='Enter Roll Number :')
    labelroll.grid(row=0, column=0)
    rnum=StringVar()
    r1 = Entry(rframe,textvariable=rnum)
    r1.grid(row=0, column=1, padx=10)

    roll3 = Button(rframe, text='Submit', font=('arial',14,'bold'),fg="white",bg="brown",command=details_and_bookdetails)
    roll3.grid(row=0, column=2, pady=10)
    #middle frame

    mframe=Frame(win,bg="brown",bd=10,relief='raise', padx=20, pady=10)
    mframe.pack(padx=5,pady=10)
    lbl1 = Label(mframe,font=('arial',14,'bold'), bg='brown', text='Roll Number :')
    lbl1.grid(row=1, column=0)
    rnum1=StringVar()
    e1 = Entry(mframe,textvariable=rnum1)
    e1.grid(row=1, column=1, padx=10)


    lbl2 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Student Name :')
    lbl2.grid(row=2, column=0, pady=10)
    sname=StringVar()
    e2 = Entry(mframe,textvariable=sname)
    e2.grid(row=2, column=1, padx=10)

    lbl3 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Fathers Name :')
    lbl3.grid(row=3, column=0, pady=10)

    fanm=StringVar()
    e3 = Entry(mframe,textvariable=fanm)
    e3.grid(row=3, column=1, padx=10)

    lbl4 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Mother Name :')
    lbl4.grid(row=4, column=0, pady=10)
    mtnm=StringVar()
    e4 = Entry(mframe,textvariable=mtnm)
    e4.grid(row=4, column=1, padx=10)

    lbl5 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Date of Birth :')
    lbl5.grid(row=5, column=0, pady=10)
    dateob=StringVar()
    e5 = Entry(mframe,textvariable=dateob)
    e5.grid(row=5, column=1, padx=10)

    lbl6 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Branch')
    lbl6.grid(row=6, column=0, pady=10)
    bran=StringVar()
    e6 = Entry(mframe,textvariable=bran)
    e6.grid(row=6, column=1, padx=10)

    sideframe=Frame(win,bg="brown",bd=10,relief='raise', padx=20, pady=10)
    sideframe.pack(padx=5,pady=10)
    lbs1 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Book Name :')
    lbs1.grid(row=7, column=0, pady=10)
    booknm=StringVar()
    s1 = Entry(mframe,textvariable=booknm)
    s1.grid(row=8, column=0, padx=10)

    lbs2 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Book Number :')
    lbs2.grid(row=7, column=1, pady=10)
    booknum=StringVar()
    s2 = Entry(mframe,textvariable=booknum)
    s2.grid(row=8, column=1, padx=10)

    lbs3 = Label(mframe, font=('arial',14,'bold'), bg="brown", text='Date of Issue :')
    lbs3.grid(row=7, column=2, pady=10)
    dateofiss=StringVar()
    s3 = Entry(mframe,textvariable=dateofiss)
    s3.grid(row=8, column=2, padx=10)

    lbs4= Label(mframe, font=('arial',14,'bold'), bg="brown", text='Last Date to return :')
    lbs4.grid(row=7, column=3, pady=10)
    lstdate=StringVar()
    s4 = Entry(mframe,textvariable=lstdate)
    s4.grid(row=8, column=3, padx=10)

    mframe=Frame(win,bg="brown",bd=10,relief='raise', padx=50, pady=30)
    mframe.pack(padx=50,pady=20)
    closemain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='Close',fg="pink",command=win.destroy)
    closemain.grid(row=2, column=1, padx=10)

    exitmain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='GO TO Main',fg="pink",command=open_main)
    exitmain.grid(row=2, column=0, padx=10)
    win.mainloop()

    
def open_delete():
    
    win.destroy()
    def delete():
        rollnum = rnum.get()
        try:
            conn=mysql.connector.connect(host='localhost',user='root',password='password',db='data')
            a=conn.cursor()
            a.execute("select * from student where rollno='"+rollnum+"'")
            resultb = a.fetchall()
            countb = a.rowcount
            print(resultb)
            print(countb)
            if countb > 0:
                a.execute("delete from student where rollno='"+rollnum+"'")
                conn.commit()
                # print('delete')
                messagebox.showinfo("message"," deleted")
            else:
                messagebox.showinfo("message","Student Not Found")

        except:
            conn.rollback()
            #print('not delete')
            messagebox.showinfo("message","Error")
        conn.close()
        
    global win
    win=Tk()
    win.overrideredirect(True)
    win.overrideredirect(False)
    win.attributes('-fullscreen',False)

    win.title("windows application")
    win.configure(bg='gray')
    load = Image.open('icon\\i4.png')
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0)


    #middle frame
    mframe=Frame(win,width=800,height=800,bg="brown",bd=10,relief='raise', padx=40, pady=30)
    mframe.pack(padx=50,pady=20)

    lbl1 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Roll Number :')
    lbl1.grid(row=0, column=0)
    rnum=StringVar()
    e1 = Entry(mframe,textvariable=rnum)
    e1.grid(row=0, column=1, padx=10)
    
    exitmain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='GO TO Main',fg="pink",command=open_main)
    exitmain.grid(row=2, column=0, padx=10)
    closemain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='Close',fg="pink",command=win.destroy)
    closemain.grid(row=2, column=2, padx=10)
    e3 = Button(mframe, text='Delete', font=('arial',14,'bold'),fg="pink",bg="brown",command=delete)
    e3.grid(row=2, column=1, pady=10)
    
    win.mainloop()

def open_book():
    win.destroy()
    def add_book():
        bkname=booknm.get()
        bknum=booknum.get()
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='password', db='data')
            a = conn.cursor()
            a.execute("insert into books(bookname,bookno)values('"+bkname+"','"+bknum+"')")
            conn.commit()
            print('save')
        except:
            conn.rollback()
            print('Not Save')
            conn.close()
            
    global win        
    win=Tk()
    win.overrideredirect(True)
    win.overrideredirect(False)
    win.attributes('-fullscreen',False)
    
    win.title("windows application")
    win.configure(bg='gray')
    load = Image.open('icon\\i5.png')
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0)

    #middle frame
    mframe=Frame(win,width=800,height=800,bg="brown",bd=10,relief='raise', padx=80)
    mframe.pack(padx=50,pady=200)

    lbl1 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Book Name :')
    lbl1.grid(row=0, column=0)
    booknm=StringVar()
    e1 = Entry(mframe,textvariable=booknm)
    e1.grid(row=0, column=1, padx=10, pady=10)

    lbl2 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Book Number :')
    lbl2.grid(row=1, column=0, pady=10)
    booknum=StringVar()
    e2 = Entry(mframe,textvariable=booknum)
    e2.grid(row=1, column=1, padx=10)
    
    exitmain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='GO TO Main',fg="pink",command=open_main)
    exitmain.grid(row=2, column=0, padx=10)
    closemain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='Close',fg="pink",command=win.destroy)
    closemain.grid(row=2, column=2, padx=10)

    e3 = Button(mframe, text='Submit', font=('arial',14,'bold'),fg="white",bg="brown",command=add_book)
    e3.grid(row=2, column=1, pady=10)

    win.mainloop()
    
def open_add():
    win.destroy()
    def add_student():
        rollnum=rnum.get()
        stdname=sname.get()
        faname=fanm.get()
        mname=mtnm.get()
        dobr=dateob.get()
        brnch=bran.get()
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='password', db='data')
            a = conn.cursor()
            a.execute("select * from student where rollno='"+rollnum+"'")
            x=a.fetchall()
            y=a.rowcount
            if(y==0):
                a.execute("insert into student (rollno,studname,fathername,mothername,dob,branch)values('"+rollnum+"', '"+stdname+"', '"+faname+"', '"+mname+"', '"+dobr+"', '"+ brnch+"')")
                conn.commit()
                messagebox.showinfo("message","Student saved succesfully")
                print('save')
            else:
                messagebox.showinfo("message","Duplicate Entry")

        except:
            conn.rollback()
            print('Not Save')
            messagebox.showinfo("message","Error")
            conn.close()

    global win
    win=Tk()
    win.overrideredirect(True)
    win.overrideredirect(False)
    win.attributes('-fullscreen',False)
    win.title("windows application")
    win.configure(bg='gray')
    load = Image.open('icon\\i6.png')
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0)

    #middle frame
    mframe=Frame(win,bg="brown",bd=10,relief='raise', padx=50, pady=30)
    mframe.pack(padx=50,pady=50)

    lbl1 = Label(mframe,font=('arial',14,'bold'), bg='brown', text='Roll Number :')
    lbl1.grid(row=0, column=0)
    rnum=StringVar()
    e1 = Entry(mframe,textvariable=rnum)
    e1.grid(row=0, column=1, padx=10)


    lbl2 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Student Name :')
    lbl2.grid(row=1, column=0, pady=10)
    sname=StringVar()
    e2 = Entry(mframe,textvariable=sname)
    e2.grid(row=1, column=1, padx=10)

    lbl3 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Fathers Name :')
    lbl3.grid(row=2, column=0, pady=10)

    fanm=StringVar()
    e3 = Entry(mframe,textvariable=fanm)
    e3.grid(row=2, column=1, padx=10)

    lbl4 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Mother Name :')
    lbl4.grid(row=3, column=0, pady=10)
    mtnm=StringVar()
    e4 = Entry(mframe,textvariable=mtnm)
    e4.grid(row=3, column=1, padx=10)

    lbl5 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Date of Birth :')
    lbl5.grid(row=4, column=0, pady=10)
    dateob=StringVar()
    e5 = Entry(mframe,textvariable=dateob)
    e5.grid(row=4, column=1, padx=10)

    lbl6 = Label(mframe, font=('arial',14,'bold'), bg='brown', text='Branch')
    lbl6.grid(row=5, column=0, pady=10)
    bran=StringVar()
    e6 = Entry(mframe,textvariable=bran)
    e6.grid(row=5, column=1, padx=10)

    exitmain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='GO TO Main',fg="pink",command=open_main)
    exitmain.grid(row=6, column=0, padx=10)
    closemain = Button(mframe, font=('arial',14,'bold'), bg='brown',text='Close',fg="pink",command=win.destroy)
    closemain.grid(row=6, column=2, padx=10)


    e3 = Button(mframe, font=('arial',14,'bold'), bg='brown',text='Add Student',fg="pink",command=add_student)
    e3.grid(row=6, column=1, padx=10)

    win.mainloop()

def open_main():
    try:
        win.destroy()
    except:
        pass
        
    global win
    win=Tk()
    win.overrideredirect(True)
    win.overrideredirect(False)
    win.attributes('-fullscreen',False)
    win.title("windows application")
    load = Image.open('icon\\i7.png')
    win.configure(bg='gray')
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0)

    #Top Frame
    topframe=Frame(win,width=4600,height=3500,bg="pink",bd=10,relief="raise")
    topframe.pack(side=TOP)
    lb=Label(topframe,font=('arial',45,'bold'),fg="pink",bg="brown",text='WELCOME', width=30)
    lb.grid(row=0,column=0)

    #middle frame
    mframe=Frame(win,bg="brown",bd=10,relief='raise', padx=100, width=4600, height=3500)
    mframe.pack(padx=150,pady=150)

    lbl1 = Label(mframe,font=('arial',20,'bold'), text='Enter the Options to Pull The Records', bg="brown", fg='white')
    lbl1.grid(row=0, columnspan=2)

    e4 = Button(mframe, text='Add Student', font=('arial',14,'bold'),bg="brown",command=open_add)
    e4.grid(row=4, column=0, pady=10)

    e4 = Button(mframe, text='Issue Book', font=('arial',14,'bold'),bg="brown",command=open_issue)
    e4.grid(row=4, column=1, pady=10)

    e4 = Button(mframe, text='Return Book', font=('arial',14,'bold'),bg="brown",command=open_return)
    e4.grid(row=5, column=0, pady=10)

    e4 = Button(mframe, text='Add Book', font=('arial',14,'bold'),bg="brown",command=open_book)
    e4.grid(row=5, column=1, pady=10)

    e4 = Button(mframe, text='View Student Details', font=('arial',14,'bold'),bg="brown",command=open_details)
    e4.grid(row=6, column=0, pady=10)

    e4 = Button(mframe, text='Delete Student', font=('arial',14,'bold'),bg="brown",command=open_delete)
    e4.grid(row=6, column=1, pady=10)

    closemain = Button( font=('arial',14,'bold'), bg='brown',text='Close Main',fg="pink",command=win.destroy)
    closemain.pack(side=BOTTOM)

    win.mainloop()
    

open_main()
#first()










