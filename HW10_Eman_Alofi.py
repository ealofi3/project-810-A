from collections import defaultdict
from prettytable import PrettyTable
from HW08_Eman_Alofi import file_reading_gen
import os


class Repository:
    """ This class holds all the data for the repository """

    def __init__(self, cwd):
        self.cwd = cwd
        self.studentdict = {}
        self.instructordict = {}
        self.majordict = {}

        self.majors(os.path.join(self.cwd, "majors.txt"))
        self.student(os.path.join(self.cwd, "students.txt"))
        self.instructor(os.path.join(self.cwd, "instructors.txt"))
        self.gradesprocessing(os.path.join(self.cwd, "grades.txt"))

        self.ptablestudent()
        self.ptableinstructor()
        self.ptablemajor()

    def student(self, path):
        """ read student's file """
        try:
            for studentid, studentname, studentmajor in file_reading_gen(path, 3, sep=';', header=True):
                if studentmajor in self.majordict:
                    self.studentdict[studentid] = Student(studentid, studentname, studentmajor,
                                                          self.majordict[studentmajor])
                else:
                    print(f"WARNING: student {studentid} has an unknown major {studentmajor}")
        except FileNotFoundError as fnfe:
            print(fnfe)
        except ValueError as ve:
            print(ve)

    def instructor(self, path):
        """ read instructors """
        try:
            for instructorid, instructorname, instructordept in file_reading_gen(path, 3, sep='|', header=True):
                self.instructordict[instructorid] = Instructor(instructorid, instructorname, instructordept)
        except FileNotFoundError as fnfe:
            print(fnfe)
        except ValueError as ve:
            print(ve)

    def gradesprocessing(self, path):
        """To read grades files """
        try:
            for studentid, studentcourse, studentgrade, instructorid in file_reading_gen(path, 4, sep='|', header=True):
                if studentid in self.studentdict:
                    self.studentdict[studentid].add_coursegrade(studentcourse, studentgrade)
                else:
                    print('Not finding the student')
                if instructorid in self.instructordict:
                    self.instructordict[instructorid].add_coursestudent(studentcourse)
                else:
                    print('Not finding the Instructor')
        except FileNotFoundError as fnfe:
            print(fnfe)
        except ValueError as ve:
            print(ve)

    def majors(self, path):
        """To read majors' file"""
        try:
            for major, flag, course in file_reading_gen(path, 3, sep='\t', header=True):
                if major not in self.majordict:
                    self.majordict[major] = Major(major)

                self.majordict[major].add_course(course, flag)
        except FileNotFoundError as fnfe:
            print(fnfe)
        except ValueError as ve:
            print(ve)

    def ptablestudent(self):
        """Print all students prettytable"""
        pt = PrettyTable(
            field_names=['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', '"Remaining electives'])
        for student in self.studentdict.values():
            pt.add_row(student.studentdetails())
        print(pt)

    def ptableinstructor(self):
        """Print all instructors prettytable"""
        pt = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])
        for instructor in self.instructordict.values():
            for row in instructor.instructordetails():
                pt.add_row(row)
        print(pt)

    def ptablemajor(self):
        """Print all majors prettytable"""
        pt = PrettyTable(field_names=['major_name', 'Required_courses ', 'Elective_courses'])
        for major in self.majordict.values():
            pt.add_row(major.major_details())
        print(pt)


class Student:

    def __init__(self, studentid, studentname, studentmajor, major):
        self.studentid = studentid
        self.studentname = studentname
        self.studentmajor = studentmajor
        self.coursegrades = {}
        self.major = major

    def add_coursegrade(self, course, grade):
        """To add course grade """
        self.coursegrades[course] = grade

    def studentdetails(self):
        """To return students deitals info """
        completed = self.major.completed_courses(self.coursegrades)
        return [self.studentid, self.studentname, self.studentmajor, sorted(completed),
                sorted(self.major.remaining_courses(completed)), sorted(self.major.elective_courses(completed))]


class Instructor:

    def __init__(self, instructor_id, instructor_name, instructor_dept):
        self.instructorid = instructor_id
        self.instructorname = instructor_name
        self.instructordept = instructor_dept
        self.coursestudents = defaultdict(int)

    def add_coursestudent(self, course):
        """To add the number of cources """
        self.coursestudents[course] += 1

    def instructordetails(self):
        """To return instrcutors info """
        for course, studentnum in self.coursestudents.items():
            yield [self.instructorid, self.instructorname, self.instructordept, course, studentnum]


class Major:

    def __init__(self, dept):
        self.dept = dept
        self.required = set()
        self.electives = set()

    def add_course(self, course, type_course):
        """To add either Requried  or Elective course"""
        if type_course == "R":
            self.required.add(course)
        elif type_course == "E":
            self.electives.add(course)

    def completed_courses(self, courses_grades):
        """To add the completed cources by students"""
        return {course for course, grade in courses_grades.items() if grade in {'A', 'A-', 'B+', 'B', 'B-', 'C', 'C-'}}

    def remaining_courses(self, completed):
        """To check the reamaninig cource of the students"""
        return self.required - completed

    def elective_courses(self, completed):
        """To check the reamaninig elective courses """
        if completed.intersection(self.electives):
            return {}
        else:
            return self.electives

    def major_details(self):
        """return all major details"""
        return [self.dept, sorted(self.required), sorted(self.electives)]


def main():
    wdir10 ='/Users/ealofi3/Documents/good_data'
    wdir_bad_data = '/Users/ealofi3/Documents/bad_data'
    wdir_bad_fields = '/Users/ealofi3/Documents/bad_field'

    print("Good data")
    _ = Repository(wdir10)

    print("\nBad Data")
    print("--> should report student with unknown major, grade for unknown student, and grade for unknown instructor")
    _ = Repository(wdir_bad_data)

    print("\nBad Fields\n")
    print("should report bad student, grade, instructor feeds")
    _ = Repository(wdir_bad_fields)

    print("\nNon-existent Data Directory\n")
    _ = Repository("Not A Directory")
    
if __name__ == "__main__":
    main()


