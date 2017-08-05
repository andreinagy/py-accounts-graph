# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import FileFinder as f
import Graph as g
import ParserING as parserIng
from Account import Account
from operator import attrgetter

if __name__ == "__main__":
    print("Python Bank Accounts CSV parser")

transactions = []

for file in f.findFilesInDirectory(f.cwd(), ".csv"):
    transactions += (parserIng.parseFile(file))


sortedTransactions = sorted(transactions, key=attrgetter('date'), reverse=False)

acc = Account(sortedTransactions)

dates = acc.getAllDates()
balances = acc.getAllBalances()

print(dates)
print(balances)

g.plotAmount(dates, balances)

# xAxis = [o.getDate() for o in sortedTransactions]
# amount = [o.amount for o in sortedTransactions]
#
# print(sortedTransactions)
# print(xAxis)
# print(amount)
#
# g.plotAmount(xAxis, amount)

