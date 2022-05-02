from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
import datetime

lh, rt, pd, da = "localhost", "root", "password", "data"


def hover(button, x='green'):
    button.bind("<Enter>", func=lambda e: button.config(bg=x))
    y = button["bg"]
    button.bind("<Leave>", func=lambda e: button.config(bg=y))


def first():
    def login():
        us = user.get()
        ps = pswd.get()
        try:
            conn = mysql.connector.connect(host=lh, user=rt, password=pd, db=da)
            a = conn.cursor()
            a.execute("select * from login where username='" + us + "' and password = '" + ps + "'")
            results = a.fetchall()
            if len(results) > 0:
                win.destroy()
                open_main()
            else:
                messagebox.showinfo("message", "Wrong username or password")

        except Exception:
            messagebox.showerror("Error", "Database Error")
        else:
            conn.close()

    win = Tk()
    # win.attributes('-zoomed', True)
    win.state('zoomed')
    win.title("Library Management")
    win.configure(bg='gray')
    load = Image.open('icon\\i8.png')

    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0, relheight=1, relwidth=1)

    # top frame
    topframe = Frame(win, width=1800, height=900, bg="pink", bd=10, relief="raised")
    topframe.pack(side=TOP)
    lb = Label(topframe, font=('arial', 45, 'bold'), fg="pink", bg="brown", text='LIBRARY MANAGEMENT SYSTEM', width=30)
    lb.grid(row=0, column=0)

    # middle frame
    mframe = Frame(win, bg="brown", bd=10, relief='raised', padx=30, pady=100)
    mframe.pack(padx=500, pady=140)

    lbl1 = Label(mframe, text='User name', font=('arial', 12, 'bold'), fg="pink", bg="brown")
    lbl1.grid(row=0, column=0, pady=10)
    user = StringVar()
    e1 = Entry(mframe, textvariable=user, justify='center', )
    e1.grid(row=0, column=1, padx=10)

    lbl2 = Label(mframe, text='Password', font=('arial', 12, 'bold'), fg="pink", bg="brown")
    lbl2.grid(row=1, column=0, pady=10)
    pswd = StringVar()
    e2 = Entry(mframe, textvariable=pswd, justify='center', show='*')
    e2.grid(row=1, column=1, padx=10)

    closemain = Button(mframe, font=('arial', 12, 'bold'), bg='brown', text='Close Main', fg="pink",
                       command=win.destroy)
    closemain.grid(row=2, column=0, padx=10)

    e3 = Button(mframe, text='Log in', font=('arial', 12, 'bold'), fg="pink", bg="brown", command=login)
    e3.grid(row=2, column=1, padx=10)

    hover(e3)
    hover(closemain)

    win.mainloop()


def open_main():

    win = Tk()
    win.state('zoomed')
    win.title("Library Management")
    load = Image.open('icon\\i7.png')
    win.configure(bg='gray')

    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0, relheight=1, relwidth=1)

    # Top Frame
    topframe = Frame(win, width=4600, height=3500, bg="pink", bd=10, relief="raised")
    topframe.pack(side=TOP)
    lb = Label(topframe, font=('arial', 45, 'bold'), fg="pink", bg="brown", text='WELCOME', width=30)
    lb.grid(row=0, column=0)

    # middle frame
    mframe = Frame(win, bg="brown", bd=10, relief='raised', padx=100, width=4600, height=3500)
    mframe.pack(padx=150, pady=150)

    lbl1 = Label(mframe, font=('arial', 20, 'bold'), text='Enter the Options to Pull The Records', bg="brown",
                 fg='white')
    lbl1.grid(row=0, columnspan=2)

    e4 = Button(mframe, text='Add Student', font=('arial', 14, 'bold'), bg="brown", command=lambda: (win.destroy(), open_add()))
    e4.grid(row=4, column=0, pady=10)

    e5 = Button(mframe, text='Issue Book', font=('arial', 14, 'bold'), bg="brown", command=lambda: (win.destroy(), open_issue()))
    e5.grid(row=4, column=1, pady=10)

    e6 = Button(mframe, text='Return Book', font=('arial', 14, 'bold'), bg="brown", command=lambda: (win.destroy(), open_return()))
    e6.grid(row=5, column=0, pady=10)

    e7 = Button(mframe, text='Add Book', font=('arial', 14, 'bold'), bg="brown", command=lambda: (win.destroy(), open_book()))
    e7.grid(row=5, column=1, pady=10)

    e8 = Button(mframe, text='View Student Details', font=('arial', 14, 'bold'), bg="brown", command=lambda: (win.destroy(), open_details()))
    e8.grid(row=6, column=0, pady=10)

    e9 = Button(mframe, text='Delete Student', font=('arial', 14, 'bold'), bg="brown", command=lambda: (win.destroy(), open_delete()))
    e9.grid(row=6, column=1, pady=10)

    closemain = Button(font=('arial', 14, 'bold'), bg='brown', text='Close Main', fg="pink", command=win.destroy)
    closemain.pack(side=BOTTOM)

    for i in [e4, e5, e6, e7, e8, e9, closemain]:
        hover(i)

    win.mainloop()


def open_add():
    def add_student():
        rollnum = rnum.get()
        stdname = sname.get()
        faname = fanm.get()
        mname = mtnm.get()
        dobr = datebox.get()
        brnch = bran.get()

        try:
            conn = mysql.connector.connect(host=lh, user=rt, password=pd, db=da)
            a = conn.cursor()
            a.execute("select * from student where rollno='" + rollnum + "'")
            x = a.fetchall()
            if not len(x) and stdname and faname and mname and dobr and brnch:
                a.execute(
                    "insert into student (rollno, studname, fathername, mothername, dob, branch)values('" + rollnum + "',  '" + stdname + "',  '" + faname + "',  '" + mname + "',  '" + dobr + "',  '" + brnch + "')")
                conn.commit()
                messagebox.showinfo("message", "Student saved successfully")
                print('save')
            elif len(x):
                conn.rollback()
                messagebox.showinfo("message", "Duplicate Entry")
            else:
                messagebox.showinfo("message", "Please Enter Some values")

        except Exception:
            print('Not Save')
            messagebox.showinfo("message", "Error")

        else:
            conn.close()

    win = Tk()
    win.state('zoomed')
    win.overrideredirect(False)
    win.attributes('-fullscreen', False)
    win.title("Library Management")
    win.configure(bg='gray')
    load = Image.open('icon\\i6.png')
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0, relheight=1, relwidth=1)

    # middle frame
    mframe = Frame(win, bg="brown", bd=10, relief='raised', padx=50, pady=30)
    mframe.pack(padx=50, pady=50)

    lbl1 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Roll Number :')
    lbl1.grid(row=0, column=0)
    rnum = StringVar()
    e1 = Entry(mframe, textvariable=rnum)
    e1.grid(row=0, column=1, padx=10)

    lbl2 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Student Name :')
    lbl2.grid(row=1, column=0, pady=10)
    sname = StringVar()
    e2 = Entry(mframe, textvariable=sname)
    e2.grid(row=1, column=1, padx=10)

    lbl3 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Fathers Name :')
    lbl3.grid(row=2, column=0, pady=10)

    fanm = StringVar()
    e3 = Entry(mframe, textvariable=fanm)
    e3.grid(row=2, column=1, padx=10)

    lbl4 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Mother Name :')
    lbl4.grid(row=3, column=0, pady=10)
    mtnm = StringVar()
    e4 = Entry(mframe, textvariable=mtnm)
    e4.grid(row=3, column=1, padx=10)

    lbl5 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Date of Birth :')
    lbl5.grid(row=4, column=0, pady=10)
    datebox = StringVar()
    e5 = Entry(mframe, textvariable=datebox)
    e5.grid(row=4, column=1, padx=10)

    lbl6 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Branch')
    lbl6.grid(row=5, column=0, pady=10)
    bran = StringVar()
    e6 = Entry(mframe, textvariable=bran)
    e6.grid(row=5, column=1, padx=10)

    exitmain = Button(mframe, font=('arial', 14, 'bold'), bg='brown', text='GO TO Main', fg="pink", command=lambda: (win.destroy(), open_main()))
    exitmain.grid(row=6, column=0, padx=10)
    closemain = Button(mframe, font=('arial', 14, 'bold'), bg='brown', text='Close', fg="pink", command=win.destroy)
    closemain.grid(row=6, column=2, padx=10)

    e3 = Button(mframe, font=('arial', 14, 'bold'), bg='brown', text='Add Student', fg="pink", command=add_student)
    e3.grid(row=6, column=1, padx=10)

    win.mainloop()


def open_issue():
    cn = False
    today = datetime.date.today()
    ret = today + datetime.timedelta(days=14)
    today, ret = today.isoformat(), ret.isoformat()

    def reset():
        nonlocal cn
        e0.config(text=' ')
        e2.config(text=' ')
        e6.config(text='Submit')

        cn = False

        e1.config(state='normal')
        e1.delete(0, 'end')
        e3.config(state='normal')
        e3.delete(0, 'end')

        exitmain.config(text="GO TO Main", command=lambda: (win.destroy(), open_main()))

    def issue_book():
        nonlocal cn
        rollnum = rnum.get()
        bknum = booknum.get()
        datofiss = dateofiss.get()
        lastdateret = lstdate.get()

        if rollnum != '' or bknum != '':
            conn = mysql.connector.connect(host=lh, user=rt, password=pd, db=da)
            try:
                a = conn.cursor()
                nonlocal e1, e3
                a.execute("SELECT bookname FROM books where bookno='" + bknum + "'")
                bname = a.fetchall()

                a.execute("SELECT studname FROM student where rollno=" + rollnum + "")
                sname = a.fetchall()

                cn = True if e6['text'] == "Confirm" else False

                a.execute("SELECT rollno FROM issuebook where rollno=" + rollnum + "")
                a.fetchall()
                c = a.rowcount

                if not sname:
                    messagebox.showinfo("Error", "Student Not found")

                elif not bname:
                    messagebox.showinfo("Error", "Book Not found")

                elif c < 2:
                    sname, bname = sname[0][0], bname[0][0]
                    e2.config(text=bname)
                    e0.config(text=sname)

                    e6.config(text='Confirm')

                    e1.config(state='disabled')
                    e3.config(state='disabled')

                    exitmain.config(text="Back", command=reset)
                else:
                    messagebox.showinfo("Error", "2 books on hold")

                if cn:
                    a.execute("insert into issuebook(rollno, bookno, issuedate, returndate, bookname)values("
                              + rollnum + ", " + bknum + ", '" + datofiss + "', '" + lastdateret + "', '" + bname + "')")
                    conn.commit()
                    messagebox.showinfo("message", "Book Issued")

            except mysql.connector.errors.IntegrityError:
                messagebox.showerror("Error", "Duplicate Entry")
                reset()
                conn.rollback()
                conn.close()

            else:
                conn.close()
        else:
            messagebox.showinfo("message", "Please Enter Some values")

    win = Tk()
    win.state('zoomed')
    win.overrideredirect(False)
    win.attributes('-fullscreen', False)
    win.title("Library Management")
    win.configure(bg='gray')
    load = Image.open('icon\\i2.png')
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0, relheight=1, relwidth=1)

    # middle frame
    mframe = Frame(win, width=800, height=800, bg="brown", bd=10, relief='raised', padx=50, pady=30)
    mframe.pack(padx=50, pady=100)

    lbl0 = Label(mframe, font=('arial', 14, 'bold'), bg="brown", text='Student Name :')
    lbl0.grid(row=0, column=0, pady=10)
    e0 = Label(mframe, text=' ', font=('arial', 14, 'bold'), bg="brown")
    e0.grid(row=0, column=1, padx=10)

    lbl2 = Label(mframe, font=('arial', 14, 'bold'), bg="brown", text='Book Name :')
    lbl2.grid(row=1, column=0, pady=10)
    e2 = Label(mframe, text=' ', font=('arial', 14, 'bold'), bg="brown")
    e2.grid(row=1, column=1, padx=10)

    lbl1 = Label(mframe, font=('arial', 14, 'bold'), bg="brown", text='Roll Number :')
    lbl1.grid(row=2, column=0, pady=10)
    rnum = StringVar()
    e1 = Entry(mframe, textvariable=rnum, justify='center')
    e1.grid(row=2, column=1, padx=10)

    lbl3 = Label(mframe, font=('arial', 14, 'bold'), bg="brown", text='Book Number :')
    lbl3.grid(row=3, column=0, pady=10)
    booknum = StringVar()
    e3 = Entry(mframe, textvariable=booknum, justify='center')
    e3.grid(row=3, column=1, padx=10)

    lbl4 = Label(mframe, font=('arial', 14, 'bold'), bg="brown", text='Date of Issue :')
    lbl4.grid(row=4, column=0, pady=10)

    dateofiss = StringVar()
    e4 = Entry(mframe, textvariable=dateofiss, justify='center')
    e4.insert(0, today)
    e4.grid(row=4, column=1, padx=10)
    e4.bind('<FocusIn>',
            lambda e: e4.delete(0, "end") if dateofiss.get() == today else None)
    e4.bind("<FocusOut>",
            lambda e: e4.insert(0, today) if dateofiss.get() == "" else None)

    lbl5 = Label(mframe, font=('arial', 14, 'bold'), bg="brown", text='Last Date to return :')
    lbl5.grid(row=5, column=0, pady=10)

    lstdate = StringVar()
    e5 = Entry(mframe, textvariable=lstdate, justify='center')
    e5.insert(0, ret)
    e5.grid(row=5, column=1, padx=10)
    e5.bind('<FocusIn>',
            lambda e: e5.delete(0, "end") if lstdate.get() == ret else None)
    e5.bind("<FocusOut>",
            lambda e: e5.insert(0, ret) if lstdate.get() == "" else None)

    exitmain = Button(mframe, font=('arial', 14, 'bold'), bg='brown', text='GO TO Main', fg="pink",
                      command=lambda: (win.destroy(), open_main()))
    exitmain.grid(row=6, column=0, padx=10)
    closemain = Button(mframe, font=('arial', 14, 'bold'), bg='brown', text='Close', fg="pink", command=win.destroy)
    closemain.grid(row=6, column=2, padx=10)

    e6 = Button(mframe, text='Submit', font=('arial', 14, 'bold'), bg="brown", command=issue_book)
    e6.grid(row=6, column=1, pady=10)

    win.mainloop()


def open_return():

    def reset():
        e2.config(text='')
        e1.config(state='normal')
        g.config(text="GET", command=return_)
        e3.config(state="disabled")
        e3.config(bg='brown')
        hover(e3, 'brown')

    def return_():
        bknm = bknum.get()
        try:
            conn = mysql.connector.connect(host=lh, user=rt, password=pd, db=da)
            a = conn.cursor()
            bknm = '0' if bknm == '' else bknm
            a.execute("select bookname from issuebook where bookno=" + bknm)
            results = a.fetchall()

            cn = True if g['text'] == "Back" else False

            if len(results) > 0:
                x = results[0][0]
                e2.config(text=x)
                e1.config(state='disabled')
                g.config(text="Back", command=reset)
                e3.config(state="normal")
                hover(e3)

            else:
                messagebox.showinfo("message", "Record Not Found")

            if cn:
                a.execute("delete from issuebook where bookno='" + bknm + "'")
                conn.commit()
                messagebox.showinfo("Message", "Book returned")
                reset()

        except Exception:
            messagebox.showinfo("message", "not delete")

        else:
            conn.close()

    win = Tk()
    win.state('zoomed')
    win.title("Library Management")
    win.configure(bg='gray')

    load = Image.open('icon\\i1.png')
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0, relheight=1, relwidth=1)

    # middle frame
    mframe = Frame(win, width=800, height=800, bg="brown", bd=10, relief='raised', padx=40, pady=30)
    mframe.pack(padx=50, pady=70)

    lbl1 = Label(mframe, font=('arial', 14, 'bold'), bg="brown", text='Book Number :')
    lbl1.grid(row=0, column=0, pady=10)
    bknum = StringVar()
    e1 = Entry(mframe, textvariable=bknum)
    e1.grid(row=0, column=1, padx=10)

    g = Button(mframe, text='GET', font=('arial', 14, 'bold'), fg="pink", bg="brown", command=return_)
    g.grid(row=0, column=2, pady=10)

    lbl2 = Label(mframe, font=('arial', 14, 'bold'), bg="brown", text='Book Name :')
    lbl2.grid(row=1, column=0, pady=10)
    e2 = Label(mframe, text=' ', font=('arial', 14, 'bold'), bg="brown")
    e2.grid(row=1, column=1, padx=10)

    exitmain = Button(mframe, font=('arial', 14, 'bold'), bg='brown', text='GO TO Main', fg="pink", command=lambda: (win.destroy(), open_main()))
    exitmain.grid(row=2, column=0, padx=10)
    closemain = Button(mframe, font=('arial', 14, 'bold'), bg='brown', text='Close', fg="pink", command=win.destroy)
    closemain.grid(row=2, column=2, padx=10)

    e3 = Button(mframe, text='Submit', font=('arial', 14, 'bold'), fg="pink", bg="brown", command=return_, state='disabled')
    e3.grid(row=2, column=1, pady=10)

    hover(exitmain)
    hover(g)
    hover(closemain)

    win.mainloop()


def open_details():
    def details():
        rollnum = rnum.get()
        print(rollnum)
        conn = mysql.connector.connect(host=lh, user=rt, password=pd, db=da)
        a = conn.cursor()
        a.execute("select * from student where rollno='" + rollnum + "'")

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
        conn = mysql.connector.connect(host=lh, user=rt, password=pd, db=da)
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

    win = Tk()
    win.state('zoomed')
    win.overrideredirect(False)
    win.attributes('-fullscreen', False)
    win.title("Library Management")
    win.configure(bg='gray')
    load = Image.open('icon\\i3.png')
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0, relheight=1, relwidth=1)
    # top frame
    topframe = Frame(win, width=4600, height=3500, bg="pink", bd=10, relief="raised")
    topframe.pack(side=TOP)
    lb = Label(topframe, font=('arial', 30, 'bold'), fg="pink", bg="brown", text='Students Detail', width=40)
    lb.grid(row=0, column=0)

    rframe = Frame(win, bg="brown", bd=10, relief='raised', padx=10, pady=10)
    rframe.pack(padx=5, pady=5)
    labelroll = Label(rframe, font=('arial', 14, 'bold'), bg='brown', text='Enter Roll Number :')
    labelroll.grid(row=0, column=0)
    rnum = StringVar()
    r1 = Entry(rframe, textvariable=rnum)
    r1.grid(row=0, column=1, padx=10)

    roll3 = Button(rframe, text='Submit', font=('arial', 14, 'bold'), fg="white", bg="brown",
                   command=details_and_bookdetails)
    roll3.grid(row=0, column=2, pady=10)
    # middle frame

    mframe = Frame(win, bg="brown", bd=10, relief='raised', padx=20, pady=10)
    mframe.pack(padx=5, pady=10)
    lbl1 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Roll Number :')
    lbl1.grid(row=1, column=0)
    rnum1 = StringVar()
    e1 = Entry(mframe, textvariable=rnum1)
    e1.grid(row=1, column=1, padx=10)

    lbl2 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Student Name :')
    lbl2.grid(row=2, column=0, pady=10)
    sname = StringVar()
    e2 = Entry(mframe, textvariable=sname)
    e2.grid(row=2, column=1, padx=10)

    lbl3 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Fathers Name :')
    lbl3.grid(row=3, column=0, pady=10)

    fanm = StringVar()
    e3 = Entry(mframe, textvariable=fanm)
    e3.grid(row=3, column=1, padx=10)

    lbl4 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Mother Name :')
    lbl4.grid(row=4, column=0, pady=10)
    mtnm = StringVar()
    e4 = Entry(mframe, textvariable=mtnm)
    e4.grid(row=4, column=1, padx=10)

    lbl5 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Date of Birth :')
    lbl5.grid(row=5, column=0, pady=10)
    dateob = StringVar()
    e5 = Entry(mframe, textvariable=dateob)
    e5.grid(row=5, column=1, padx=10)

    lbl6 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Branch')
    lbl6.grid(row=6, column=0, pady=10)
    bran = StringVar()
    e6 = Entry(mframe, textvariable=bran)
    e6.grid(row=6, column=1, padx=10)

    sideframe = Frame(win, bg="brown", bd=10, relief='raised', padx=20, pady=10)
    sideframe.pack(padx=5, pady=10)
    lbs1 = Label(mframe, font=('arial', 14, 'bold'), bg="brown", text='Book Name :')
    lbs1.grid(row=7, column=0, pady=10)
    booknm = StringVar()
    s1 = Entry(mframe, textvariable=booknm)
    s1.grid(row=8, column=0, padx=10)

    lbs2 = Label(mframe, font=('arial', 14, 'bold'), bg="brown", text='Book Number :')
    lbs2.grid(row=7, column=1, pady=10)
    booknum = StringVar()
    s2 = Entry(mframe, textvariable=booknum)
    s2.grid(row=8, column=1, padx=10)

    lbs3 = Label(mframe, font=('arial', 14, 'bold'), bg="brown", text='Date of Issue :')
    lbs3.grid(row=7, column=2, pady=10)
    dateofiss = StringVar()
    s3 = Entry(mframe, textvariable=dateofiss)
    s3.grid(row=8, column=2, padx=10)

    lbs4 = Label(mframe, font=('arial', 14, 'bold'), bg="brown", text='Last Date to return :')
    lbs4.grid(row=7, column=3, pady=10)
    lstdate = StringVar()
    s4 = Entry(mframe, textvariable=lstdate)
    s4.grid(row=8, column=3, padx=10)

    mframe = Frame(win, bg="brown", bd=10, relief='raised', padx=50, pady=30)
    mframe.pack(padx=50, pady=20)
    closemain = Button(mframe, font=('arial', 14, 'bold'), bg='brown', text='Close', fg="pink", command=win.destroy)
    closemain.grid(row=2, column=1, padx=10)

    exitmain = Button(mframe, font=('arial', 14, 'bold'), bg='brown', text='GO TO Main', fg="pink", command=lambda: (win.destroy(), open_main()))
    exitmain.grid(row=2, column=0, padx=10)
    win.mainloop()


def open_delete():
    def delete():
        rollnum = rnum.get()
        try:
            conn = mysql.connector.connect(host=lh, user=rt, password=pd, db=da)
            a = conn.cursor()
            a.execute("select * from student where rollno='" + rollnum + "'")
            resultb = a.fetchall()
            countb = a.rowcount
            print(resultb)
            print(countb)
            if countb > 0:
                a.execute("delete from student where rollno='" + rollnum + "'")
                conn.commit()
                # print('delete')
                messagebox.showinfo("message", " deleted")
            else:
                messagebox.showinfo("message", "Student Not Found")

        except:
            conn.rollback()
            # print('not delete')
            messagebox.showinfo("message", "Error")

        else:
            conn.close()

    win = Tk()
    win.state('zoomed')
    win.overrideredirect(False)
    win.attributes('-fullscreen', False)

    win.title("Library Management")
    win.configure(bg='gray')
    load = Image.open('icon\\i4.png')
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0, relheight=1, relwidth=1)

    # middle frame
    mframe = Frame(win, width=800, height=800, bg="brown", bd=10, relief='raised', padx=40, pady=30)
    mframe.pack(padx=50, pady=20)

    lbl1 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Roll Number :')
    lbl1.grid(row=0, column=0)
    rnum = StringVar()
    e1 = Entry(mframe, textvariable=rnum)
    e1.grid(row=0, column=1, padx=10)

    exitmain = Button(mframe, font=('arial', 14, 'bold'), bg='brown', text='GO TO Main', fg="pink", command=lambda: (win.destroy(), open_main()))
    exitmain.grid(row=2, column=0, padx=10)
    closemain = Button(mframe, font=('arial', 14, 'bold'), bg='brown', text='Close', fg="pink", command=win.destroy)
    closemain.grid(row=2, column=2, padx=10)
    e3 = Button(mframe, text='Delete', font=('arial', 14, 'bold'), fg="pink", bg="brown", command=delete)
    e3.grid(row=2, column=1, pady=10)

    win.mainloop()


def open_book():
    def add_book():
        bkname = booknm.get()
        bknum = booknum.get()
        try:
            conn = mysql.connector.connect(host=lh, user=rt, password=pd, db=da)
            a = conn.cursor()
            a.execute("insert into books(bookname, bookno)values('" + bkname + "', '" + bknum + "')")
            conn.commit()
            print('save')
        except:
            conn.rollback()
            print('Not Save')
            conn.close()

    win = Tk()
    win.state('zoomed')
    win.overrideredirect(False)
    win.attributes('-fullscreen', False)

    win.title("Library Management")
    win.configure(bg='gray')
    load = Image.open('icon\\i5.png')
    render = ImageTk.PhotoImage(load)
    img = Label(win, image=render)
    img.image = render
    img.place(x=0, y=0, relheight=1, relwidth=1)

    # middle frame
    mframe = Frame(win, width=800, height=800, bg="brown", bd=10, relief='raised', padx=80)
    mframe.pack(padx=50, pady=200)

    lbl1 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Book Name :')
    lbl1.grid(row=0, column=0)
    booknm = StringVar()
    e1 = Entry(mframe, textvariable=booknm)
    e1.grid(row=0, column=1, padx=10, pady=10)

    lbl2 = Label(mframe, font=('arial', 14, 'bold'), bg='brown', text='Book Number :')
    lbl2.grid(row=1, column=0, pady=10)
    booknum = StringVar()
    e2 = Entry(mframe, textvariable=booknum)
    e2.grid(row=1, column=1, padx=10)

    exitmain = Button(mframe, font=('arial', 14, 'bold'), bg='brown', text='GO TO Main', fg="pink", command=lambda: (win.destroy(), open_main()))
    exitmain.grid(row=2, column=0, padx=10)
    closemain = Button(mframe, font=('arial', 14, 'bold'), bg='brown', text='Close', fg="pink", command=win.destroy)
    closemain.grid(row=2, column=2, padx=10)

    e3 = Button(mframe, text='Submit', font=('arial', 14, 'bold'), fg="white", bg="brown", command=add_book)
    e3.grid(row=2, column=1, pady=10)

    win.mainloop()


first()
