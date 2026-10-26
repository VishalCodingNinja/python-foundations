class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Declined: {self.owner} has only {self.balance:.2f}")
            return False
        self.balance -= amount
        return True

    def describe(self):
        return f"{self.owner}: {self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=0.02):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        self.balance += self.balance * self.rate


ana = BankAccount("Ana", 100)
ana.deposit(50)
ana.withdraw(500)          # Declined: Ana has only 150.00
raj = SavingsAccount("Raj", 1000, rate=0.05)
raj.add_interest()
for account in [ana, raj]:
    print(account.describe())
