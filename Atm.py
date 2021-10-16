class Atm(object):
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber,
        self.pinNumber = pinNumber
    def CashWithdrawl(self):
        print("Cash Withdrawl")
    def BalanceEnquiry(self):
        print("Balance Enquiry")
#main
bank = Atm("1234","5678")
print(bank.cardNumber)
bank.CashWithdrawl()