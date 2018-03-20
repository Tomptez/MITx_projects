#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#monthlyPaymentRate -  minimum monthly payment rate as a decimal

#example:
balance = 42; annualInterestRate = 0.2; monthlyPaymentRate = 0.04
# Expected remaining balance: 31.38

def month(balance, InRa, monPayRa, mon):
    if mon == 0:
        return balance
    balance = balance - monPayRa * balance
    balance += balance * InRa
    
    return month(balance, InRa, monPayRa, mon-1)

balance = month(balance, annualInterestRate/12, monthlyPaymentRate, 12)
print("Expected remaining balance:", round(balance, 2))