if __name__ == "__main__":
    print "Parser ING"

import os
import csv
import re
from datetime import datetime
from Transaction import Transaction


def floatFromAmount(str):
    return re.findall("\d+\.\d+", str)[0]

def parseFile(fileAndPath):
    transactions = []

    with open(fileAndPath) as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:

            if row["Date"]:
                date = datetime.strptime(row["Date"], '%d %B %Y')
                amount = 0
                debit = row["Debit"]
                credit = row["Credit"]
                if debit:
                    debit = floatFromAmount(debit)
                    amount = -1 * float(debit)
                elif credit:
                    credit = floatFromAmount(credit)
                    amount = float(credit)
                else:
                    continue

                details = row["Transaction Details"]

                transaction = Transaction(date, amount, details)
                transactions.append(transaction)



    return transactions
