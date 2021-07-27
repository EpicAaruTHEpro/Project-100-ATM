class Atm() :
    def __init__(self, name, cardNum, pin, withdrawl, balance):
        self.name = name
        self.cardNum = cardNum
        self.pin= pin
        self.withdrawl = withdrawl
        self.balance = balance

    def cashWithdrawl(self, withdrawl) :
        print("You have withdrawn", withdrawl)

    def balanceEnquiry(self, balance):
        print("You currently have", balance)

# Making the accounts for the atm
Jeff = Atm("Jeff", 159043, 567210, 9750, 193278)
Jamie = Atm("Jamie", 574389, 318712, 700, 52340)

# Printing values
print(Jeff.cardNum)
print(Jamie.cardNum)
Jeff.cashWithdrawl(Jeff.withdrawl)
Jamie.balanceEnquiry(Jamie.balance)

