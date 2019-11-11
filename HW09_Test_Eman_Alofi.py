import unittest

from HW09_Eman_Alofi import Repository,  Student, Instructor


class StudentsTest(unittest.TestCase):

    def test_studentdetails(self):
        """test cases for studentdetails() method"""
        student = Student('11461', 'Wright, U', 'SYEN')
        student.add_coursegrade('SYS 800', 'A')
        self.assertEqual(student.studentdetails(), ['11461', 'wright, U', ['SYS 800']])


class InstructorTest(unittest.TestCase):

    def test_instructordetails(self):
        """test cases for instructordetails() method"""
        instructor = Instructor('98765', 'Einstein, A', 'SFEN')
        instructor.add_coursestudent('SSW 540')
        self.assertEqual(instructor.instructordetails(), ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3])


class RepositoryTest(unittest.TestCase):

    def test_Repository(self):
        """test cases for Repository class methods"""

        cwd ="/Users/ealofi3/Desktop/test"
        repo = Repository(cwd)
        self.assertEqual(repo.student((cwd, 'students.txt')), None)
        self.assertEqual(repo.instructor((cwd, 'instructors.txt')), None)
        self.assertEqual(repo.gradesprocessing((cwd, 'grades.txt')), None)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
