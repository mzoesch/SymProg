class Account:

    def __init__(self, name, id, balance):
        self.name = name
        self._id = id  # Semi private
        self.__id = id  # Private
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def printInfo(self):
        print(f'{self.name} has {self.balance} in their account')

    def __str__(self):
        return f'{self.name} has {self.balance} in their account.\nThe public  account id is {self._id}\nThe private account id is {self.__id}\n'

    def setID(self, id):
        self.__id = id

    def getID(self):
        return self.__id


if __name__ == '__main__':
    a = Account('John', 12345678, 100)
    print(a)
    a.deposit(100)
    a._id = 87654321
    print(a)
    a.withdraw(50)
    a.setID(11112222)
    a.__id = 2  # This will not change the private id, but also not throw
    print(a)
