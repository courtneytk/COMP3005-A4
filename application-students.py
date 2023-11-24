import psycopg2
from psycopg2 import sql

 
#Creating the connection to the database in pgadmin
connect = psycopg2.connect(
    database="Student",
    user='postgres',
    password='Courtney2002',
    host='localhost',
    port='5433'
)
 
#Creating a cursor object
cursor = connect.cursor()

#Getting all the students in the table
def getAllStudents():
    cursor.execute("SELECT * FROM students;")
    #Fetchall gets all the rows returned by SQL query
    students = cursor.fetchall()
    #Print for user to see info
    for student in students:
        print(student)
    return

#Adding a student to the database (note, doesn't allow duplicate students with the same emails)
def addStudent(first_name, last_name, email, enrollment_date):
    cursor.execute(sql.SQL("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ({}, {}, {}, {});").format(
            sql.Literal(first_name),
            sql.Literal(last_name),
            sql.Literal(email),
            sql.Literal(enrollment_date)
        ))
    #Commits changes to database
    connect.commit()

#Updating a given student's information
def updateStudentEmail(student_id, new_email):
    cursor.execute(sql.SQL("UPDATE students SET email = {} WHERE student_id = {};").format(
            sql.Literal(new_email),
            sql.Literal(student_id)
        ))
    #Commits changes to database
    connect.commit()

#Deleting a record of a student given an id
def deleteStudent(student_id):
    cursor.execute(sql.SQL("DELETE FROM students WHERE student_id = {};").format(
            sql.Literal(student_id)
        ))
    #Commits changes to database
    connect.commit()

#Printing results of CRUD operations in the terminal

# print("All Students:\n")
# getAllStudents()
# print("------------------------------\n")

# print("All Students with a new Addition:\n")
# addStudent("NEW", "ADDITION", "NEWADDITION3@example.com", "2023-11-23")
# getAllStudents()
# print("------------------------------\n")

# print("All Students with a new update to one Email:\n")
# updateStudentEmail(student_id=3, new_email="UPDATED@example.com")
# getAllStudents()
# print("------------------------------\n")

print("All Students and deletion of one student:\n")
deleteStudent(student_id=2)
getAllStudents()
print("------------------------------\n")
