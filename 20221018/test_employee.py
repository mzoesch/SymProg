import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('John', 'Smith', 50000)
        emp_2 = Employee('Sue', 'Schafer', 60000)

        self.assertEqual(emp_1.email, 'John.Smith@company.com')
        self.assertEqual(emp_2.email, 'Sue.Schafer@company.com')

        emp_1.first = 'Jim'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.email, 'Jim.Smith@company.com')
        self.assertEqual(emp_2.email, 'Jane.Schafer@company.com')

    def test_fullname(self):
        emp_1 = Employee('John', 'Smith', 50000)
        emp_2 = Employee('Sue', 'Schafer', 60000)

        self.assertEqual(emp_1.fullname, 'John Smith')
        self.assertEqual(emp_2.fullname, 'Sue Schafer')

        emp_1.first = 'Jim'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.fullname, 'Jim Smith')
        self.assertEqual(emp_2.fullname, 'Jane Schafer')

    def test_apply_raise(self):
        emp_1 = Employee('John', 'Smith', 50000)
        emp_2 = Employee('Sue', 'Schafer', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()
