def primeCalculator(n):
    i = 1
    while i <= n:
        if i > 1 and i != n and n % i == 0:
            print("divisible by " + str(i))
            return "composite"
        i += 1
    return "prime"

def factorization(n):
    factorizationList = []
    if primeCalculator(n) == "prime":
        factorizationList.append(n)
    else:
       print("hi") 


factorization(6)