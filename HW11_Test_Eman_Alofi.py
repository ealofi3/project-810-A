import unittest

import sqlite3
db_file = '/Users/ealofi3/Documents/Database_SSW810/test_startup.db'

class RepositoryTest(unittest.TestCase):

    def read_student_table(self):
        """To test students' file from database """
        try:
            db = sqlite3.connect(db_file)
            cursor = db.cursor()
            student_query = """select CWID, Name, Major from Students"""
            for row in cursor.execute(student_query):
                print(row)
            print("Connected to SQLITE3")
            cursor.close()
        except sqlite3.Error as error:
            print(f" {error}")

        finally:
            if (db):
                db.close()
                print("The database connection is close ")



    def test_db_instructors(self):
        """To test  Instructors' file from database """
        try:
            db = sqlite3.connect(db_file)
            cursor = db.cursor()
            student_query = """select CWID, Name, Dept from Instructors"""
            for row in cursor.execute(student_query):
                print(row)
            print("Connected to SQLITE3")
            cursor.close()
        except sqlite3.Error as error:
            print(f"{error}")

        finally:
            if (db):
                db.close()
                print("The database connection is close ")


    def test_grades(self):

        """To test Grades' file from database """
        try:
            db = sqlite3.connect(db_file)
            cursor = db.cursor()
            student_query = """select StudentCWID, Course, Grade, InstructorCWID from Grades"""
            for row in cursor.execute(student_query):
                print(row)
            print("Connected to SQLITE3")
            cursor.close()
        except sqlite3.Error as error:
            print(f"{error}")

        finally:
            if (db):
                db.close()
                print("The database connection is close ")

    def test_major(self):

        """To test majors' file from database """
        try:
            db = sqlite3.connect(db_file)
            cursor = db.cursor()
            student_query = """select Major, Required/Elective, Course from Majors"""
            for row in cursor.execute(student_query):
                print(row)
            print("Connected to SQLITE3")
            cursor.close()
        except sqlite3.Error as error:
            print(f" {error}")

        finally:
            if (db):
                db.close()
                print("The database connection is close ")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
