class BankAccount:
    def __init__(self,owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"deposited {amount} to {self.owner}")
        assert (amount <= 0, "You didnt enter a positive value to deposit")

    def withdraw(self,amount):
        assert(amount <= 0, "You didnt enter a positive value to withdraw")
        if amount > self.balance:
            print("You don't have enough money to withdraw that amount")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount} to {self.owner}. Balance is now {self.balance} dollars.")


acct = BankAccount("Todd", 1000)
print(acct.withdraw(100))
print(acct.withdraw(1000))



