# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# Example:
balance = 3329; annualInterestRate = 0.2
# should result in 310

def correct(balance, InRa, PayRate, mon):
    orig_balance = balance
    while mon > 0:
        balance = balance - PayRate
        balance += balance * InRa
        mon -= 1
    if mon == 0 and balance > 0:
        return PayRate + 10
    else:
        PayRate -= 10
        return correct(orig_balance, annualInterestRate/12, PayRate, 12)

PayRate = (balance+balance*annualInterestRate)/12
PayRate = round(PayRate, -1)
PayRate = correct(balance, annualInterestRate/12, PayRate, 12)

print("Lowest Payment:", round(PayRate))