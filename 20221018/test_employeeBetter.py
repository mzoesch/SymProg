# Tests should always be isolated

import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('John', 'Smith', 50000)
        self.emp_2 = Employee('Sue', 'Schafer', 60000)

    def tearDown(self):
        print('tearDown')

    @classmethod
    def setUpClass(cls):
        print('setUpClass')  # Creating DB for example

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')  # Popping DB for example

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'John.Smith@company.com')
        self.assertEqual(self.emp_2.email, 'Sue.Schafer@company.com')

        self.emp_1.first = 'Jim'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'Jim.Smith@company.com')
        self.assertEqual(self.emp_2.email, 'Jane.Schafer@company.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'John Smith')
        self.assertEqual(self.emp_2.fullname, 'Sue Schafer')

        self.emp_1.first = 'Jim'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'Jim Smith')
        self.assertEqual(self.emp_2.fullname, 'Jane Schafer')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    # Mocking
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Smith/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Schafer/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
