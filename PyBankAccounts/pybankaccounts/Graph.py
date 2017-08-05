# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print "Graph"

def plotAmount(xAxis, amount):

    plt.xlabel("Date")
    plt.ylabel("Funds")
    plt.plot(xAxis, amount, 'g-')
    plt.grid(True)

    plt.show()

def plot(xAxis, debitArray, creditArray):
    # plt.figure(1)
    # plt.subplot(211)
    plt.xlabel("Date")
    plt.ylabel("Funds")
    credit = plt.plot(xAxis, creditArray, 'g-', linewidth=2.0)
    plt.setp(credit, color='g', linewidth=2.0)

    debit = plt.plot(xAxis, debitArray, 'r-')
    plt.setp(debit, color='r', linewidth=1.0)


    plt.grid(True)
    plt.show()


# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
#
# plt.figure(1)
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()