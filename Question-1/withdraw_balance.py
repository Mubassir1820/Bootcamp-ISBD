# A banking application allows users to withdraw money. The function withdraw(balance,
# amount) should check if the withdrawal amount is greater than the balance. If yes, it should
# raise an exception "Insufficient funds", otherwise return the new balance.


def withdraw(balance: int, amount: int):
    if amount > balance:
        raise Exception("Insufficient funds")
    new_balance = balance - amount
    return f'Remaining balance: {new_balance}'