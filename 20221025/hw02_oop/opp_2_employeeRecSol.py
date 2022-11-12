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

  # Constructor of the class Employee, assigns values to the name, the department and the age of the employee
  def __init__(self, name, department, age, vacation_days):
    self.name = name
    self.department = department
    self.age = age
    self.vacation_days = vacation_days

  # Set a new department of the employee
  def set_department(self, new_department):
    self.department = new_department

  # Return the information of the employee as a string representation
  def __str__(self):
    return ("###Employee Summary###\n"
            f"Name: {self.name}\n"
            f"Age: {str(self.age)}\n"
            f"Current department: {self.department}\n")

  # Reduce the number of vacation days left
  def reduce_vacation_days(self, days):
    self.vacation_days -= days


# Main Code
if __name__ == "__main__":
  print("Employee Information:")
  employee1 = Employee("Harry Potter", "research", 35, 30)
  employee1.set_department("marketing")
  print(employee1.name + " now works in " + employee1.department)
  employee1.department
  employee2 = Employee("Hermine Granger", "marketing", 27, 30)
  employee2.reduce_vacation_days(10)
  print(employee2.name + " only has " + str(employee2.vacation_days) + " vacation days left.")
  employee3 = Employee("Ron Weasley", "research", 53, 30)
  employee4 = Employee("Voldemort", "research", 77, 30)

  # Create dictionary with departments and employees
  departements_dict = {
    "research": [employee3, employee4],
    "marketing": [employee1, employee1]
  }

  # print each department and each employee
  for dep in departements_dict.keys():
    for empl in departements_dict[dep]:
      print(dep + ":" + empl.name)
