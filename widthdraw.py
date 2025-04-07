class CashOut:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 100:
            self.balance -= amount
            print(f"Withdraw Amount P{amount} Your new balance is {self.balance}")

        else:
            print("withdraw should be amount to onehundred.")

my_account = CashOut("bronnyJames", 2000)

my_account.withdraw(110)