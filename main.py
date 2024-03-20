# Import required libraries
import sqlite3

# Connect to SQLite database
# New file created if it doesn't already exist
conn = sqlite3.connect('sqlite3.db')

# Create cursor object
cursor = conn.cursor()

# Create and populate tables
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS Advisor( 
    AdvisorID INTEGER NOT NULL, 
    AdvisorName TEXT NOT NULL, 
    PRIMARY KEY(AdvisorID)
    )
''')

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS Student( 
    StudentID INTEGER NOT NULL, 
    StudentName TEXT NOT NULL, 
    AdvisorID INTEGER, 
    FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID), 
    PRIMARY KEY(StudentID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Student_Advisor( 
    AdvisorID INTEGER NOT NULL,
    StudentID INTEGER NOT NULL,
    FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
    FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
    PRIMARY KEY(AdvisorID, StudentID)
    )
''')

cursor.executescript('''
INSERT INTO  Advisor(AdvisorID, AdvisorName) VALUES 
(1,"John Paul"), 
(2,"Anthony Roy"), 
(3,"Raj Shetty"), 
(4,"Sam Reeds"), 
(5,"Arthur Clintwood"); 

INSERT INTO Student(StudentID, StudentName, AdvisorID) VALUES 
(501, "Geek1", 1), 
(502, "Geek2" ,1), 
(503, "Geek3", 3), 
(504, "Geek4", 2), 
(505, "Geek5", 4), 
(507, "Geek7", 2), 
(508, "Geek8", 3), 
(509, "Geek9", NULL), 
(510, "Geek10", 1); 

''')

# SQL query for the many-to-many connection

many_to_many_connection_result = '''
SELECT Advisor.AdvisorID, Advisor.AdvisorName, COUNT(Student.StudentID) AS number_of_students
FROM Advisor
INNER JOIN Student ON Advisor.AdvisorID = Student.AdvisorID
GROUP BY Advisor.AdvisorID, Advisor.AdvisorName
ORDER BY number_of_students ASC;
'''

cursor.execute(many_to_many_connection_result)

# Fetch and print the result
result = cursor.fetchall()
print("AdvisorID\tAdvisorName\tNumberOfStudents")
for row in result:
    print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}")

# Commit changes to database
conn.commit()

# Closing the connection
conn.close()
