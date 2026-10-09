# Банковский счёт
class BankAccount:
    def __init__(self,owner):
        self.account=owner
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            return True
        else:
            return False
    def get_balance(self):
        return self.balance
first=BankAccount('Timur')
second=BankAccount('Anna')
first.deposit(200)
print(first.account)
print(second.get_balance())
print(first.withdraw(200))
print(first.get_balance())