
-- Database: `data`

CREATE DATABASE `data`;
USE `data`;


-- --------------------------------------------------------


-- Table structure for table `books`


CREATE TABLE `books` (
  `bookname` varchar(20) NOT NULL,
  `bookno` varchar(20) PRIMARY KEY NOT NULL
);


----------------------------------------------------------


-- Table structure for table `issuebook`


CREATE TABLE `issuebook` (
  `rollno` int(20) NOT NULL,
  `bookname` varchar(20) NOT NULL,
  `bookno` varchar(20) NOT NULL,
  `issuedate` varchar(20) NOT NULL,
  `returndate` varchar(20) NOT NULL
);


-----------------------------------------------------------


-- Table structure for table `login`


CREATE TABLE `login` (
  `username` varchar(200) PRIMARY KEY NOT NULL,
  `password` varchar(200) NOT NULL
);


-- Dumping data for table `login`
-- Type the required username and password in place of admin and root

INSERT INTO `login` (`username`, `password`) VALUES
(<admin>, <root>);

----------------------------------------------------------


-- Table structure for table `student`


CREATE TABLE `student` (
  `rollno` int(20) PRIMARY KEY NOT NULL,
  `studname` varchar(20) NOT NULL,
  `fathername` varchar(20) NOT NULL,
  `mothername` varchar(20) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `branch` varchar(20) NOT NULL
) ;
