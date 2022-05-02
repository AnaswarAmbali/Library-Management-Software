
CREATE DATABASE data;
USE data;

CREATE TABLE books (
  bookname varchar(20) NOT NULL,
  bookno varchar(20) PRIMARY KEY NOT NULL
);


CREATE TABLE issuebook (
  rollno int(20) NOT NULL,
  bookname varchar(20) NOT NULL,
  bookno int(20) PRIMARY KEY NOT NULL,
  issuedate varchar(20) NOT NULL,
  returndate varchar(20) NOT NULL
);


CREATE TABLE login (
  username varchar(200) PRIMARY KEY NOT NULL,
  password varchar(200) NOT NULL
);
INSERT INTO login (username, password) VALUES
('admin', 'root');


CREATE TABLE student (
  rollno int(20) PRIMARY KEY NOT NULL,
  studname varchar(20) NOT NULL,
  fathername varchar(20) NOT NULL,
  mothername varchar(20) NOT NULL,
  dob varchar(20) NOT NULL,
  branch varchar(20) NOT NULL,
  bk int(2) NOT NULL
) ;

CREATE TABLE history (
  bookno varchar(20) NOT NULL,
  rollno int(20) PRIMARY KEY NOT NULL,
  issuedate varchar(20) NOT NULL,
  returnddate varchar(20) NOT NULL
};

