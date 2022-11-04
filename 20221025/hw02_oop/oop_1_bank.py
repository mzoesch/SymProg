import re

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

    def __init__(self, id: int, holder: str, balance: float = 0.) -> None:
        """

        Class acts as a simple bank account.\n
        Money can be deposited and withdrawn.\n
        The account holder can be changed.

        """

        self.id: int = id
        self.__holder: str = holder  # private attribute
        self._balance: float = balance
        return

    @property
    def holder(self):
        """ Acts as a getter for holder. A separate getter method is not needed. """

        return self.__holder

    @holder.setter
    def holder(self, value):
        """ Setter method for __holder. """

        if (not type(value) is str):
            print(  # Not raising error as in script, but printing error message,
                # so that the program can continue running without crashing.
                'Name of person must be of type string.'
            )
            return
        if not re.match('\w+( \w+)*', value.strip()):
            print(
                'Name of person must be a string of letters and spaces.'
            )
            return

        self.__holder = value

    # @holder.getter
    # def holder(self):
    #    """ Getter method for __holder. """
    #
    #    return self.__holder

    @property
    def balance(self):
        """ Acts as a getter for account balance. """

        return self._balance

    def deposit(self, amount):
        """ Deposit money into the account. Negative amounts are not allowed. """

        if amount <= 0.:
            print(
                'You can not deposit a negative amount or zero.'
            )
            return

        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        """ Withdraw money from the account. Negative amounts are not allowed. """

        if amount <= 0.:
            print(
                'You can not withdraw a negative amount or zero.'
            )
            return

        if self._balance <= -1_000.:
            print(
                'You have reached your maximum debt. You can not withdraw any more.'
            )
            return

        if self._balance - amount < -1_000.:
            r, self._balance = self._balance + 1_000., -1_000.
            print(
                f'You have reached your maximum debt (1000€). Could only withdraw: {r}€'
            )
            return r

        self._balance -= amount
        return amount

    def apply_interest(self, rate: float = 0.015) -> float:
        """ Apply interest rate of 1.5% (default) to current balance. """

        if self._balance <= 0.:
            print(
                'No interest on debts.'
            )
            return
        if rate <= 0.:
            print(
                'Interest rate has to be positive.'
            )
            return

        self._balance += self._balance * rate
        return self._balance

    def __str__(self) -> str:
        """ Return a string representation of the account. """

        return f'''
══════ Accout Info ══════
ID:         : {self.id}
Holder:     : {self.holder}
Balance:    : {self._balance}€
'''


def main(*args, **kwargs) -> None:
    """ Main application. """

    acc1 = Account(1, 'John Doe', 1_000.)
    acc2 = Account(2, 'Sue Schafer', 2_000.)
    acc3 = Account(3, 'Tim Schuster')
    print(acc1)
    print(acc2)
    print(f'{acc3}\n')

    acc1.deposit(1_000.)  # Does not throw
    acc2.deposit(-100.)  # Negative amount
    acc3.deposit(200.)  # Does not throw
    print(acc1)
    print(acc2)
    print(f'{acc3}\n')

    acc1.withdraw(500.)  # Does not throw
    acc1.withdraw(-50.)  # Negative amount
    acc2.withdraw(2_500.)  # Balance now negative
    acc3.withdraw(2_000.)  # Max debt
    print(acc1)
    print(acc2)
    print(f'{acc3}\n')

    acc1.apply_interest()
    acc2.deposit(1_000.)  # Deposit to get out of debt
    acc2.apply_interest()
    acc3.apply_interest()  # No interest on debts
    print(acc1)
    print(acc2)
    print(f'{acc3}\n')

    print(f'Account holder is {acc1.holder}')
    acc1.holder = "John Smith"
    print(f'Account holder is {acc1.holder}')

    return


if __name__ == '__main__':
    print('Welcome to the Python Bank.\n')
    main()
