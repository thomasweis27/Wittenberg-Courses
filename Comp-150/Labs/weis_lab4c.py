#
# Name: Thomas Weis
# File: weis_lab4c.py
# Date: 03/04/21
#
# Desc: Determines if an integer m is prime or not 
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis

def isPrime(m):
    #takes an input and returns if it is true of false
    count = 0
    for k in range(1,m):
        if m % k == 0:
            count = count + 1
    if count == 1:
        return True, count
    else:
        return False, count

def primesBetween(m):
    #sees if each number is prime and counts the numbers of primes between
    primesInbetween = 0
    for i in range (2, m):
        TF, count = isPrime(i)
        if TF == True:
            primesInbetween = primesInbetween +1
    return primesInbetween

def main():
    #takes the output of primesBetween() and displays outcome
    print ("Prime Number Counter"), print()
    m = int(input("Please enter a number: "))
    TF, count = isPrime(m)
    primesInbetween = primesBetween(m)
    if TF == True:
        primesInbetween = primesInbetween +1 #because we the number inputted could be prime
        
    print("There are {} primes less than or equal to {}".format(primesInbetween, m))

main()
