from sympy.ntheory import factorint, n_order, primerange
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

""" Variable Declaration """

r = 100000000 # range of numbers checked
num_repdigits = 0 # number of Niven repdigits found

badprimes = [] # primes that connot be factors of Niven repdigits
goodprimes = [2, 3, 37, 163, 757, 1999, 5477, 8803, 9397, 13627, 15649, 36187, 40879] # primes that can be factors of Niven repdigits
for i in primerange(0, 2000): # fill badprimes list
    if i not in goodprimes:
        badprimes.append(i)

""" Method Declaration """

def formatFactors(n, factors): # format the Niven repdigits and factors for printing
    returnMe = str(n) + " - "
    first_time = True
    for p, m in factors.items():
        if(not first_time):
            returnMe = returnMe + " * "
        returnMe = returnMe + str(p) + "^" + str(m)
        first_time = False
    return returnMe

def checkFactors(n): # remove numbers with badprimes factors; end early if primes are larger than number
    for p in badprimes:
        if(p > n):
            return True
        if(n % p == 0):
            return False
    return True

""" Begin Checking Numbers """

repdigits = []
cycleTimes_dict = {}

startTime = datetime.now()

for n in range(3, r, 6):
    cycleStart = datetime.now()
    if(checkFactors(n)):
        if(n % n_order(10, n) == 0):
            repdigits.append(n)
            num_repdigits += 1
    cycleEnd = datetime.now()
    cycleTimes_dict[n] = cycleEnd - cycleStart
            
endTime = datetime.now()

""" Display Results """

print("Total number of Niven repdigits: " + str(num_repdigits))

calcTime = endTime - startTime
print("Calculation time is: " + str(calcTime))

print("") 
#for n in repdigits:
#    print(formatFactors(n, factorint(n)))

"""Ploting the Cycle Times"""

#fig = plt.figure(figsize=(15,10))

x = []
y = []
for n in cycleTimes_dict.keys():
    x.append(n)
    y.append(cycleTimes_dict[n].total_seconds())

#plt.scatter(x, y, s=1)
#plt.ylim(0, max(y))
#plt.title("Cycle Times")
#plt.xlabel("Number Being Checked")
#plt.ylabel("Cycle Time")
#fig.savefig("cycleTimesPlot.png")