
def withdraw(balance, amount):

    #Create assertions
    assert balance >= 0, "Balance cannot be negative"
    assert amount > 0, "Amount must not be more than zero"
    assert amount <= balance, "Amount must be less than or equal to balance"

    new_balance = balance - amount
    return new_balance

#Asserting when balance < amount
print(withdraw(90, 100))

#Asserting when amount < 0
print(withdraw(90, -100))

#Asserting when balance < 0
print(withdraw(-90, 100))