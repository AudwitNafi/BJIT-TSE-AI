class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        if amount>0:
            self.__balance += amount
    def getBalance(self):
        return self.__balance

account = BankAccount(100.0)
print(f"Current balance: {account.getBalance()}")
amount = float(input("Enter deposit amount: "))
account.deposit(amount)
print(f"New amount: {account.getBalance()}")