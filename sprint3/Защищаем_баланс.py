# Защищаем баланс 🔒
class Wallet:
    def __init__(self):
        self._balance=0
    @property
    def deposit(self,amount):
        if amount<=0:
            return False
        else:
            self._balance+=amount
            return True
    def spend(self,amount):
        if amount<=self._balance and amount>=0:
            self._balance-=amount
            return True
        else:
            return False

    def balance(self):
        return self._balance
wallet=Wallet()
print(wallet.deposit(200))
print(wallet.deposit(-200))
print(wallet.spend(100))
print(wallet.spend(150))
print(wallet.balance)