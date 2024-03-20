# Project Title: Student-Advisor Relationship Management System
## Overview
- This Python script demonstrates the creation of a simple student-advisor relationship management system using SQLite3 database. It creates tables for advisors, students, and their relationships, and populates them with sample data. Additionally, it performs a query to show the number of students each advisor has.

# Requirements
- Python 3.x
- SQLite3

# Installation

- Clone the repository or download the script.
- Make sure you have Python installed on your system.
- Run the script using the command python your_script_name.py.

# Usage

The script connects to an SQLite database named sqlite3.db or creates a new one if it doesn't exist.
It creates three tables: Advisor, Student, and Student_Advisor.
Sample data is inserted into the tables for demonstration purposes.
A query is executed to display the number of students each advisor has.
The script commits changes to the database and closes the connection.

Sample Output

Copy code:

```LiteSQL
AdvisorID  AdvisorName  NumberOfStudents
3          Raj Shetty   2
4          Sam Reeds    2
1          John Paul    3
2          Anthony Roy  3
5          Arthur Clintwood  0
```

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
