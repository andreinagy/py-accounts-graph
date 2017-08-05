

class Balance(object):

    def __init__(self, previousBalance, transaction):
        self.transaction = transaction
        self.balance = previousBalance + transaction.getAmount()

    def getBalance(self):
        return self.balance

    def getDate(self):
        return self.transaction.getDate()

    def getAmount(self):
        return  self.transaction.getAmount()

class Account(object):

    def __init__(self, transactions):

        balances = []
        previousBalance = 0
        for t in transactions:
            balance = Balance(previousBalance, t)
            # print("date " + str(balance.getDate()) + " previous balance " + str(previousBalance) + " transaction amount " + str(balance.getAmount()) + " current balance " + str(balance.getBalance()))
            previousBalance = balance.getBalance()

            balances.append(balance)

        self.balances = balances

    def getAllDates(self):
        dates = []
        for b in self.balances:
            dates.append(b.getDate())

        return dates

    def getAllBalances(self):
        balances = []
        for b in self.balances:
            balances.append(b.getBalance())

        return balances
