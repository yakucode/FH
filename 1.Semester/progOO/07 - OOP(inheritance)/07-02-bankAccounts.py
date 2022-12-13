import random


class Konto(object):
    __accountNumber = ""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.__accountNumber = random.randrange(100000000, 999999999)

    def __str__(self):
        return f"name = {self.name} - balance = {self.balance} - account number = {self.__accountNumber}"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class Festgeldkonto(Konto):

    def __init__(self, name, balance):
        super(Festgeldkonto, self).__init__(name, balance)

    def withdraw(self, amount):

        if self.balance >= amount:
            self.balance -= amount
        elif self.balance < amount:
            print("not enough funds")
        else:
            print("something went wrong in Festgeldkonto class withdraw method!")


class Girokonto(Konto):
    __dispo = 0

    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.__dispo = balance * 3

    def withdraw(self, amount):
        if amount <= (self.balance + self.__dispo):
            self.balance -= amount
        elif amount > (self.balance + self.__dispo):
            print("insufficient funds")
        else:
            print("something went wrong with Girokonto withdraw method")
