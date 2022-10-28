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
    """ Here has to be a documentation string that describes
    which data objects this class is designed for.
    You have to remove the pass statement and then write some
    code for the class. """

    """
    
    Class acts as a simple bank account.
    Money can be deposited and withdrawn.
    The account holder can be changed.

    """

    def __init__(self, account_holder: str, balance: float):
        """ Constructor of the class. """

        self.__account_holder: str = account_holder  # private attributes
        self.__balance: float = balance
        return

    def deposit(self, amount):
        """ Deposit money into the account. Negative amounts are not allowed. """

        if amount <= 0.:
            print("You cannot deposit negative amounts.")
            return

        self.__balance += amount
        return

    def withdraw(self, amount):
        """ Withdraw money (max 1000€) from the account. Negative amounts are not allowed. """

        if amount <= 0.:
            print("You cannot withdraw negative amounts.")
            return

        if amount > 1000.:
            print("You cannot withdraw more than 1000€ from your account.")
            return

        if self.__balance - amount < 0.:
            print("You cannot withdraw more money than you have in your account.")
            return

        self.__balance -= amount
        return amount

    def apply_interest(self):
        """ Apply interest rate of 1.5% to the current balance. """

        self.__balance += self.__balance * 1.015
        return

    @property
    def account_holder(self):
        """

        Acts as a getter for __account_holder.
        A seperate getter method is not needed.

        """

        return self.__account_holder

    @account_holder.setter
    def account_holder(self, value):
        """ Setter method for __account_holder. """

        self.__account_holder = value
        return

    # @account_holder.getter
    # def account_holder(self):
    #     """ Getter method for __account_holder. """

    #     return self.__account_holder

    def __str__(self):
        """ Return a string representation of the account. """

        return f'{self.__account_holder} has {self.__balance} in his account.'


def main():
    """ Main application. """

    account1 = Account("John Smith", 1000.)
    account2 = Account("Sue Schafer", 2000.)

    print(account1)
    print(f'{account2}\n')

    account1.deposit(500.)
    account2.deposit(-50.)

    print(account1)
    print(f'{account2}\n')

    account1.withdraw(500.)
    account2.withdraw(-50.)
    account1.withdraw(2000.)
    account1.withdraw(500.)
    account1.withdraw(1000.)

    print(account1)
    print(f'{account2}\n')

    account1.apply_interest()
    account2.apply_interest()

    print(account1)
    print(f'{account2}\n')

    print(f'Account holder is {account1.account_holder}')
    account1.account_holder = "John Doe"
    print(f'Account holder is {account1.account_holder}')
    print(account1)

    return


if __name__ == '__main__':
    print('Welcome to the Python Bank!\n')
    main()
