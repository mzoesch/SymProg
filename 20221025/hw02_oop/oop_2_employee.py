"""Exercise 2: (5 points)

a) Write the complete code for the Employee class (including
   constructor, __str__, ...). (2 points)

b) Create a main application, create a few employee objects and show
   how you can manipulate them using the methods. (1 point)

c) Create a department dictionary (dictionary of strings to lists/sets
   of employees) with at least two departments (e.g. "accounting",
   "sales", ...) with each at least two employees. Print for each
   employee in the dictionary "<department> <employee name>".
   (2 points)

"""


class Employee:

    def __init__(self, name: str, salary: float) -> None:
        self.name: str = name
        self.salary: float = salary
        return

    def apply_raise_amount(self, raise_amount: float):
        self.salary += raise_amount
        return

    def apply_raise_precentage(self, raise_precentage: float = 0.05):
        self.salary += self.salary * raise_precentage
        return

    def __str__(self):
        return f'{self.name} has a salary of {self.salary}'

    def __repr__(self):
        return self.name


def main(*args, **kwargs) -> None:
    """ Main application. """

    employee1 = Employee('John', 1000.)
    employee2 = Employee('Jane', 2000.)
    employee3 = Employee('Jack', 3000.)
    employee4 = Employee('Jill', 4000.)
    employee5 = Employee('Jone', 5000.)
    employee6 = Employee('Jona', 6000.)
    print(employee1)
    print(employee2)
    print(employee3)
    print(employee4)
    print(employee5)
    print(f'{employee6}\n')

    employee1.apply_raise_amount(100.)
    employee2.apply_raise_precentage(0.1)
    employee3.apply_raise_precentage()
    employee4.apply_raise_amount(500.)
    employee5.apply_raise_amount(150.)
    employee6.apply_raise_precentage()
    print(employee1)
    print(employee2)
    print(employee3)
    print(employee4)
    print(employee5)
    print(f'{employee6}\n')

    departments = {
        'accounting':   {employee1, employee2, employee3},
        'sales':        {employee4, employee5, employee6}
    }
    for department, employees in departments.items():
        for employee in employees:
            print(f'{department} {repr(employee)}')

    return


if __name__ == '__main__':
    print('Employee application.\n')
    main()
