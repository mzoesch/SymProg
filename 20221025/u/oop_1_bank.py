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

    def __init__(self, account_holder: str, balance: float):
        """

        Class acts as a simple bank account.\n
        Money can be deposited and withdrawn.\n
        The account holder can be changed.

        """

        self.__account_holder: str = account_holder  # private attribute
        self._balance: float = balance
        return

    @property
    def account_holder(self):
        """ Acts as a getter for account_holder. A separate getter method is not needed. """

        return self.__account_holder

    @account_holder.setter
    def account_holder(self, value: str):
        """ Setter method for __account_holder. """

        self.__account_holder = value
        return

    # @account_holder.getter
    # def account_holder(self):
    #     """ Getter method for __account_holder. """

    #     return self.__account_holder

    def deposit(self, amount):
        """ Deposit money into the account. Negative amounts are not allowed. """

        if amount <= 0.:
            print('You cannot deposit negative amounts.')
            return

        self._balance += amount
        return

    def withdraw(self, amount):
        """ Withdraw money (max 1000€) from the account. Negative amounts are not allowed. """

        # Invalid amounts
        if amount <= 0:
            print('You cannot withdraw negative amounts.')
            return
        if amount > 1_000:
            print('You cannot withdraw more than 1,000€ from your account.')
            return

        # Balance below zero
        if self._balance <= -1_000:
            print('You have to mouch debts. You cannot withdraw any money anymore.')
            return
        if self._balance - amount < -1_000.:
            # _balance is always below zero or is zero
            r, self._balance = 1_000 - abs(self._balance), -1_000
            print('You can only have a max amount of debts (1,000€) at this bank.')
            print(f'Withdrawn {r}€ instead.')
            return r

        self._balance -= amount
        return amount

    def apply_interest(self, rate: float = 0.015):
        """ Apply interest rate of 1.5% (default) to current balance. """

        if self._balance <= 0:
            print('No interest on debts.')
            return
        if rate <= 0:
            print('Interest rate has to be positive.')
            return

        self._balance += self._balance * rate
        return self._balance

    def __str__(self):
        """ Return a string representation of the account. """

        return f'{self.account_holder} has {self._balance}€ in their account.'


def main():
    """ Main application. """

    account1 = Account('John Smith', 1_000.)
    account2 = Account('Sue Schafer', 2_000.)
    account3 = Account('Max Mustermann', 0.)

    print(account1)
    print(account2)
    print(f'{account3}\n')

    account1.withdraw(500.)  # Does not throw
    account1.withdraw(-50.)  # Negative amount
    account1.withdraw(2000.)  # To much withdrawn
    account2.withdraw(1000.)  # Max amount
    account3.withdraw(500.)  # Negative balance
    account3.withdraw(700.)  # Max debt
    print(account1)
    print(account2)
    print(f'{account3}\n')

    account1.apply_interest()
    account2.apply_interest()
    account3.apply_interest()  # No interest on debts
    print(account1)
    print(account2)
    print(f'{account3}\n')

    print(f'Account holder is {account1.account_holder}')
    account1.account_holder = "John Doe"
    print(f'Account holder is {account1.account_holder}')

    return


if __name__ == '__main__':
    print('Welcome to the Python Bank!\n')
    main()
