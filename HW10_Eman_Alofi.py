from collections import defaultdict
from prettytable import PrettyTable
from HW08_Eman_Alofi import file_reading_gen


class Repository:
    """This class holds all the files need to be readed"""

    def __init__(self, cwd):
        self.cwd = cwd
        self.studentdict = {}
        self.instructordict = {}
        self.majordict = {}
        self.student(self.cwd)
        self.instructor(self.cwd)
        self.gradesprocessing(self.cwd)
        self.majors(self.cwd)

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

            for  instructorid, instructorname, instructordept in file_reading_gen(instructor_file, 3, sep='|', header=True)
                self.instructordict[instructorid] = Instructor(instructorid, instructorname, instructordept)

    def gradesprocessing(self, path):
        """To read grades files """
        try:
            gradesprocessing_file = open(path, 'r')
        except FileNotFoundError:
            print('There is an error with opening the file to analyze')

        else:
            for studentid, studentcourse, studentgrade, instructorid in file_reading_gen(gradesprocessing_file, 3, sep='|', header=True)
                if studentid in self.studentdict:
                    self.studentdict[studentid].add_coursegrade(studentcourse, studentgrade)
                else:
                    print('Not finding the student')
                if instructorid in self.instructordict:
                    self.instructordict[instructorid].add_coursestudent(studentcourse)
                else:
                    print('Not finding the Instructor')

    def major(self, path):
        """To read majors' file"""
        try:
            major_file = open(path, 'r')
        except FileNotFoundError:
            print('There is an error with opening the file to analyze')

        else:
               for  major, flag, course in file_reading_gen(major_file, 3, sep='\t', header=True)
                     if major not in self.majordict:
                        self.majordict[major] = Major(major)
                else:
                    self.majordict[major].add_course(course, flag)

    def ptablestudent(self):
        """Print all students prettytable"""
        pt = PrettyTable(field_names=['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', '"Remaining electives'])
        for student in self.studentdict.values():
            pt.add_row(student.studentdetails())
        print(pt)

    def ptableinstructor(self):
        """Print all instructors prettytable"""
        pt = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])
        for instructor in self.instructordict.values():
            pt.add_row(instructor.instructordetails())
        print(pt)

    def petablemajor(self):
        """Print all majors prettytable"""
        pt = PrettyTable(field_names=['major_name', 'Required_courses ', 'Elective_courses'])
        for major in self.majordict.values():
            pt.add_row(major.majordetails())
        print(pt)



class Student:

    def __init__(self, studentid, studentname, studentmajor):
        self.studentid = studentid
        self.studentname = studentname
        self.studentmajor = studentmajor
        self.coursegrades = {}
        m = Major(self, self.dept)

    def add_coursegrade(self, course, grade):
        """To add course grade """
        self.coursegrades[course] = grade


    def studentdetails(self):
        """To return students deitals info """
        return [self.studentid, self.studentname, self.student_major, m.completed_courses(self),
                m.remaning_cources(self),m.elective_cources(self)]


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
        self.completed_courses = set()
        self.remaning_courses = set()
        self.remaning_elective_courses = set()
        s = Student(self, studentid, studentname, studentmajor)

    def add_course(self, course, type_course):
        """To add either Requried  or Elective course"""
        if type_course == "R":
            self.required.add(course)
        elif type_course == "E":
            self.electives.add(course)

    def completed_courses(self):
        """To add the completed cources by students"""
        for course, grade in s.coursegrades.items():
            if grade in {'A', 'A-', 'B', 'B-', 'C', 'C-'}:
                self.completed_courses.add(course)

    def remaning_cources(self):
        """To check the reamaninig cource of the students"""
        return self.completed_courses - self.required

    def elective_cources(self):
        """To check the reamaninig elective courses """
        if self.completed_courses.intersection(self.electives):
            return None
        else:
            return self.electives

   def major_details(self):
       """return all major details"""
       return [self.dept, sorted(self.required), sorted(self.electives)]


def main():
    cwd = "/Users/ealofi3/Desktop/test"
    repos = Repository(cwd)
    repos.ptablestudent()
    repos.ptableinstructor()
    repos.petablemajor()


if __name__ == '__main__':
    main()

