
from collections import defaultdict
from prettytable import PrettyTable
from HW08_Eman_Alofi import file_reading_gen

class Repository:

    def __init__(self, cwd):
        self.cwd = cwd
        self.studentdict = {}
        self.instructordict = {}
        self.student(self.cwd)
        self.instructor(self.cwd)
        self.gradesprocessing(self.cwd)

    def student(self, path):
        """To read students' file"""
        try:
            student_file = open(path, "r")
        except FileNotFoundError:
            raise FileNotFoundError("File is not finiding ")
        else:

            for studentid, studentname, studentmajor in file_reading_gen(student_file, 3, sep=';', header=True):
                self.studentdict[studentid] = Student(studentid, studentname, studentmajor)


    def instructor(self, path):
        """To read Instrcutors' file"""

        try:
            instructor_file = open(path, "r")
        except FileNotFoundError:
            raise FileNotFoundError("File is not finiding ")
        else:

            for instructorid, instructorname, instructordept in file_reading_gen(instructor_file, 3, sep='|',
                                                                                 header=True)
                self.instructordict[instructorid] = Instructor(instructorid, instructorname, instructordept)

    def gradesprocessing(self, path):
        """To read grades files """
        try:
            gradesprocessing_file = open(path, 'r')
        except FileNotFoundError:
            print('There is an error with opening the file to analyze')

        else:
            for studentid, studentcourse, studentgrade, instructorid in file_reading_gen(gradesprocessing_file, 3,
                                                                                         sep='|', header=True)
                if studentid in self.studentdict:
                    self.studentdict[studentid].add_coursegrade(studentcourse, studentgrade)
                else:
                    print('Not finding the student')
                if instructorid in self.instructordict:
                    self.instructordict[instructorid].add_coursestudent(studentcourse)
                else:
                    print('Not finding the Instructor')
    def ptablestudent(self):
        """Print all students prettytable"""
        pt = PrettyTable(field_names=['CWID', 'Name', 'Completed Courses'])
        for student in self.studentdict.values():
            pt.add_row(student.studentdetails())
        print(pt)

    def ptableinstructor(self):
        """Print all instructors prettytable"""
        pt = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])
        for instructor in self.instructordict.values():
                pt.add_row(instructor.instructordetails())
        print(pt)


class Student:

    def __init__(self, student_id, student_name, student_major):
        self.student_id = student_id
        self.student_name = student_name
        self.student_major = student_major
        self.coursegrades = {}

    def add_coursegrade(self, course, grade):
        """To add the course grade """
        self.coursegrades[course] = grade

    def studentdetails(self):
        """to retrieve required students' info """
        return [self.studentid, self.studentname, sorted(self.coursegrades.keys())]


class Instructor:

    def __init__(self, instructor_id, instructor_name, instructor_dept):
        self.instructorid = instructor_id
        self.instructorname = instructor_name
        self.instructordept = instructor_dept
        self.coursestudents = defaultdict(int)

    def add_coursestudent(self, course):
        """to count number of students by a course that is taught by an instructor  """
        self.coursestudents[course] += 1

    def instructordetails(self):
      """to  retrieve required instructor  details """
        for course, studentnum in self.coursestudents.items():
            yield [self.instructorid, self.instructorname, self.instructordept, course, studentnum]



def main():
    cwd = "/Users/ealofi3/Desktop/test"
    repos = Repository(cwd)
    repos.ptablestudent()
    repos.ptableinstructor()


if __name__ == '__main__':
    main()

