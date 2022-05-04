import mysql.connector as s
def true(data):
    sql = s.connect(host='localhost', user='root', password='password')
    a = sql.cursor()
    a.execute('CREATE DATABASE IF NOT EXISTS {}'.format(data))
    sql.close
    create(data)
def create(data):
    sql=s.connect(host='localhost', user='root', password='password', db=data)
    a = sql.cursor()

    a.execute("""CREATE TABLE IF NOT EXISTS books (
      bookname varchar(20) NOT NULL,
      bookno int(20) PRIMARY KEY NOT NULL
    )""")

    a.execute("""CREATE TABLE IF NOT EXISTS issuebook (
      rollno int(20) NOT NULL,
      bookname varchar(20) NOT NULL,
      bookno int(20) PRIMARY KEY NOT NULL,
      issuedate varchar(20) NOT NULL,
      returndate varchar(20) NOT NULL
    )""")


    a.execute("""CREATE TABLE IF NOT EXISTS login (
      username varchar(200) PRIMARY KEY NOT NULL,
      password varchar(200) NOT NULL
    );""")
    a.execute("""INSERT IGNORE INTO login (username, password) VALUES
    ('admin', 'root')""")


    a.execute("""CREATE TABLE IF NOT EXISTS student (
      rollno int(20) PRIMARY KEY NOT NULL,
      studname varchar(20) NOT NULL,
      fathername varchar(20) NOT NULL,
      mothername varchar(20) NOT NULL,
      dob varchar(20) NOT NULL,
      branch varchar(20) NOT NULL
    ) """)

    a.execute("""CREATE TABLE IF NOT EXISTS history (
      bookno varchar(20) NOT NULL,
      rollno int(20) PRIMARY KEY NOT NULL,
      issuedate varchar(20) NOT NULL,
      returnddate varchar(20) NOT NULL
    )""")
    sql.commit()
    sql.close()
