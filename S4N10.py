class BankError(Exception):
    pass

class InvalidAmountError(BankError):
    pass

class InsufficientFundsError(BankError):
    pass

class AccountBlockedError(BankError):
    pass

def withdraw(balance, amount):
    if (amount <= 0):
        raise InvalidAmountError("Сумма снятия должна быть больше 0")
    if (amount > balance):
        raise InsufficientFundsError("На счете недостаточно средств")
    return balance - amount

try:
    print(withdraw(1000, 300))
    #print(withdraw(1000, 0))
    print(withdraw(1000, 1100))
except BankError as e:
    print(e)