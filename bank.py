class bankaccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit Amount P{amount}. New Balance: P{self.balance}")

        else:
            print("Deposit Amount should be greather than zero.")

my_account = bankaccount("bronnyJames", 1500)

my_account.deposit(4500)
