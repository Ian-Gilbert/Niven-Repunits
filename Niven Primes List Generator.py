from sympy.ntheory import factorint, n_order, primerange

r = 100000

file = open("Niven Primes List.txt", "r")


def writeln(x):
    file.write(str(x) + "\n")


def check_primes(e_p, factors):
    for q in factors:
        try:
            e_q = n_order(10, q)
        except ValueError:
            return False
        if e_p % e_q != 0:
            return False
    return True


primes = file.readlines()
primes = [int(i) for i in primes]
print(primes)
start = max(primes) + 2
end = start + r

newprimes = []

for p in primerange(start, end):
    e_p = n_order(10, p)
    if checkPrimes(e_p, factorint(e_p).keys()):
        newprimes.append(p)

print("")
print(newprimes)
 
file.close()
