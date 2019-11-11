import unittest

from HW10_Eman_Alofi import Repository,  Student, Instructor, Major


class StudentsTest(unittest.TestCase):

    def test_studentdetails(self):
        """test for studentdetails method"""
        student = Student('11461', 'Wright, U', 'SYEN')
        student.add_coursegrade('SYS 800', 'A')
        self.assertEqual(student.studentdetails(), ['11461', 'wright, U', ['SYS 800']])


class InstructorTest(unittest.TestCase):

    def test_instructordetails(self):
        """test for instrcutordetails method """
        instructor = Instructor('98765', 'Einstein, A', 'SFEN')
        instructor.add_coursestudent('SSW 540')
        self.assertEqual(instructor.instructordetails(), ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3])

class MajorTest(unittest.TestCase):

    def test_Majorrdetails(self):
        """test for major_details  method """
        major = Major('SFEN')
        major.add_course('SSW 540', 'R')
        major.add_course('SSW 564', 'R')
        major.add_course('SSW 555', 'R')
        major.add_course('SSW 567', 'R')
        major.add_course('CS 501', 'E')
        major.add_course('CS 513', 'E')
        major.add_course('CS 545', 'E')
        self.assertEqual(major.major_details(), ['SFEN',(('SSW 540', 'R'), (('SSW 564', 'R')), ('SSW 555', 'R'), ('SSW 567', 'R')),
                                                 (('CS 501', 'E'), ('CS 513', 'E'),('CS 545', 'E'))])


class RepositoryTest(unittest.TestCase):

    def test_Repository(self):
        """test cases for Repository class methods"""

        cwd ="/Users/ealofi3/Desktop/test"
        repo = Repository(cwd)
        self.assertEqual(repo.student((cwd, 'students.txt')), None)
        self.assertEqual(repo.instructor((cwd, 'instructors.txt')), None)
        self.assertEqual(repo.gradesprocessing((cwd, 'grades.txt')), None)
        self.assertEqual(repo.gradesprocessing((cwd, 'majors.txt')), None)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
