# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import FileFinder as f
import Graph as g
import ParserING as parserIng
from operator import attrgetter

if __name__ == "__main__":
    print("Python Bank Accounts CSV parser")

transactions = []

for file in f.findFilesInDirectory(f.cwd(), ".csv"):
    transactions += (parserIng.parseFile(file))


sortedTransactions = sorted(transactions, key=attrgetter('date'), reverse=True)

xAxis = [0, 1, 2, 3, 4]
debit = [1, 2, 1, 1, 1]
credit = [0, 0, 0, 1, 1]

g.plot(xAxis, debit, credit)

