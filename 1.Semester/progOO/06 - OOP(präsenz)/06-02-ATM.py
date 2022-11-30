class ATM:
    def __init__(self):
        self.__balance = 0

    def deposit(self, money):
        self.__balance += money
        print(f"successfully deposited {money} $.")

    def withdraw(self, money):
        if self.__balance >= money:
            self.__balance -= money
            print(f"{self.__balance} $ withdrawn.")
        else:
            print(
                f"not enough funds: you have {self.__balance} $, but tried to withdraw {money} $")

    def getBalance(self):
        print(f"Current balance: {self.__balance}")


bankautomat_kiel = ATM()
bankautomat_kiel.getBalance()
bankautomat_kiel.deposit(120)
bankautomat_kiel.getBalance()
bankautomat_kiel.withdraw(90)
bankautomat_kiel.withdraw(50)
bankautomat_kiel.getBalance()
