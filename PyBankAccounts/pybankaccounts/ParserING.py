if __name__ == "__main__":
    print "Parser ING"

import os
import csv
import re
from datetime import datetime
from Transaction import Transaction


def dateFromString(str):
    date = datetime.strptime(str, '%d %B %Y')
    print("--------------" + str + "   date : " + repr(date))
    return date

def floatFromAmount(str):
    nonDecimal = re.compile(r'[^\d.]+')
    st = nonDecimal.sub('', str)
    result = re.findall("\d+\.\d+", st)[0]
    fl = float(result)
    # print("--------"+ result + "   float: " + repr(fl))
    return fl

def parseFile(fileAndPath):
    transactions = []

    i = 0
    with open(fileAndPath) as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:

            if row["Date"]:
                date = dateFromString(row["Date"])
                amount = 0
                debit = row["Debit"]
                credit = row["Credit"]

                if debit:
                    debit = floatFromAmount(debit)
                    amount = -1 * debit
                elif credit:
                    credit = floatFromAmount(credit)
                    amount = credit
                else:
                    continue

                details = row["Transaction Details"]

                i += 1
                transaction = Transaction(i, date, amount, details)
                transactions.append(transaction)



    return transactions
