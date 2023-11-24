# COMP3005-A4
Implementation of students database for COMP 3005 class. For assignment 4, question 1.

Youtube Video of Demonstration: https://youtu.be/h9SwDw3qUcA

This repository is small, only consisting of a Python file with the application contents and a text file with the queries used to create the students table within my Student database in the pgAdmin 4 DBMS. 


To setup and run the code:

Start by running the queries found in queries-pgadmin file in pgAdmin. 

Proceed to go to VSCode Editor and download the PostgreSQL extension by Microsoft. 

Then open up the application-students.py file in VSCode.

Edit the parameters in the connect variable (lines 5-12) and then test each functionality. This is done on lines 57-74. More information of this Python file will be discussed below.

NOTE: You may need to install the library being used in the code, in that case, just write the following in your terminal: pip install psycopg2


In the application-students.py file you will find 4 functions:

getAllStudents() - which prints out all the students in the students table

addStudent(first_name, last_name, email, enrollment_date) - which inserts a new student to the table given various params (and does NOT allow for duplicate emails)

updateStudentEmail(student_id, new_email) - given a student id, changes that student's email

deleteStudent(student_id) - given a student id, deletes the whole record of that student from the database.


To test the application:

To test the deleteStudent function, uncomment lines 71-74 (which is already done in my code)

To test the getAllStudents function, uncomment lines 57-59

To test the addStudent function, uncomment lines 61-64

To test the updateStudentEmail function, uncomment lines 66-69
