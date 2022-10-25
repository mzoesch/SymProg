class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


if __name__ == '__main__':
    a = Account('John', 100)
    print(a.name)
    print(a.balance)
    a.deposit(50)
    print(a.balance)
    a.balance = 10
    print(a.balance)
