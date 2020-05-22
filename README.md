# Advanced-Database-Management-Systems-Course-Project3

CPSC 531 - Advanced Databases

**RDBMS and Database**

The RDBMS for this project is following program implemented:

A program in Python using the dbm or shelve modules for indexing.

The database format is a binary file of disk blocks. The disk block size is 4,096 bytes, and the blocking factor bfr is 10. Each record is the equivalent of the following SQL DDL statement:
CREATE TABLE Person
(
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    job VARCHAR(70) NOT NULL,
    company VARCHAR(40) NOT NULL,
    address VARCHAR(80) NOT NULL,
    phone VARCHAR(25) NOT NULL,
    birthdate DATE NOT NULL,
    ssn VARCHAR(12) NOT NULL,
    username VARCHAR(25) NOT NULL,
    email VARCHAR(50) NOT NULL,
    url VARCHAR(50) NOT NULL
);

Strings are composed of ASCII characters and are null-terminated. Dates are stored as three 32-bit integers in native byte order representing the day, month, and year.
There are two test databases: small.bin.gz, of size 40,960 bytes, containing 100 records, and large.bin.gz, of size 4 GiB, containing over 10 million records. These files are compressed with GNU GZip for download, and should be uncompressed before use.
Indexes will be created as DBM files using python libraries.

**Queries**

Each of the following queries are implemented as separate programs. 

**Query 1 - Table scan**
Read the file block-by-block, list the SSN, first name, and last name of all users under age 21.

**Query 2 - Uniqueness check**
The SSN is supposed to be a unique identifier, but it was not declared UNIQUE above. Read the file block-by-block, using a DBM database to check whether the SSN has been seen before. Report any duplicates.

**Query 3 - Secondary index**
Use a DBM database to create a secondary index on birthdate, then loop through all items in the index to find the location on disk of all users under age 21. Read only the relevant disk blocks in order to list the SSN, first name, and last name of all users under age 21.

**Query 4 - Clustered index**
Create a clustered index on birthdate by sorting the data file and creating sparse DBM index entries for each disk block. Use this index to repeat the previous query.
