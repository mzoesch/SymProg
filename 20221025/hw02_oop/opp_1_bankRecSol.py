"""Exercise 1: (5 points)

a) Using the slides & the script, put together a file containing the
   complete Account class.  Each method must have a documentation
   string at the beginning which describes what the method is doing.
   (1 point)

b) Create a main application where you create a number of accounts.
   Play around with depositing / withdrawing money.  Change the
   account holder of an account using a setter method.  (1 point)

c) Change the withdraw function such that the minimum balance allowed
   is -1000.  (1 point)

d) Write a function apply_interest(self) which applies an interest
   rate of 1.5% to the current balance and call it on your objects.
   (1 point)

e) Implement the __str__ magic method and use it to print accounts.
   (1 point)
"""


class Account:
  """
   A class to represent a banking account.
   
   Attributes
   ----------
   number : int
      unique id for the account
   balance : int
      starting balance of the banking account
   holder: str
      person to whom the account belongs
   
   Methods
   -------
   withdraw(amount):
      Withdraw an amount of money from the banking account.
   deposit(amount):
      Deposit an amount in the banking account.
   set_account_holder(name):
      Change the name of the account holder.
   apply_interest():
      Apply the interest rate of 1.5% to the current balance.
   """

  # Constructor of the class Account, assings values to number and holder 
  def __init__(self, num, person):
    self.number = num
    self._holder = person
    self.balance = 0

  # Return the information of the given Account Instance"""
  def __str__(self):
    return ("###Account information###\n"
            f"Account ID: {str(self.number)}\n"
            f"Holder of the account: {str(self.holder)}\n"
            f"Current balance: {str(self.balance)}\n")

  @property
  def holder(self):
    return self._holder

  # Change the holder of the account to a new person"
  @holder.setter
  def holder(self, person):
    self._holder = person

  # old solution: explicit setter method
  # def set_holder(self, person):
  #   self.holder = person

  # Raise account balance by amount"
  def deposit(self, amount):
    print("Depositing " + str(amount) + "...")
    self.balance += amount

  # Lower account balance by the amount"
  def withdraw(self, amount):
    print("Withdrawing " + str(amount) + "...")
    if self.balance - amount < -1000:
      print("Your balance cannot be lower than -1000.")
    else:
      self.balance -= amount

  # Add interest to the balance
  def apply_interest(self):
    print("Applying interest of 1.5% ...")
    self.balance = self.balance * 1.015


if __name__ == "__main__":
  print("Welcome to the Python Bank!")
  katAcc = Account(1, "Katerina")
  anneAcc = Account(2, "Anne")
  katAcc.deposit(500)
  anneAcc.deposit(100000)
  print(katAcc)
  print(anneAcc)
  katAcc.withdraw(10000)
  anneAcc.withdraw(100)
  katAcc.apply_interest()
  print(katAcc)
  # anneAcc.set_holder("Mary")
  anneAcc.holder = "Mary"
  print(anneAcc)
