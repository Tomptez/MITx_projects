# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# example:
balance = 320000; annualInterestRate = 0.2
# expect "Lowest Payment: 29157.1"

def calc_rate(balance, InRa, min, max, mon = 12):
    orig_balance = balance
    PayRate = (min + max) / 2
    while mon > 0:
        balance = balance - PayRate
        balance += balance * InRa
        mon -= 1
    if balance < 0 and balance > -2:
        return PayRate
    elif balance < -2:
        return calc_rate(orig_balance, InRa, min, PayRate)
    elif balance > 0:
        return calc_rate(orig_balance, InRa, PayRate, max)
    else:
        print("Error")

PayRate = calc_rate(balance, annualInterestRate/12, 0, balance)
print("Lowest Payment:", round(PayRate, 2))