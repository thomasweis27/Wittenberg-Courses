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

def sumOfDivisors(n):
    #finds all divisors and puts them in a row
    mySum = 0
    for k in range(1,n):
        if (n % k)==0:
            mySum = mySum + k
            #print(k)
    return mySum


def main():
    print ("Perfect Number Search")
    print()
    n = int(input("Enter an integer n (>1): "))
    print()

    #runs all the integers up to the inputted number and prints perfect ##s
    for i in range(2, n):
        mySum = sumOfDivisors(i)
        if mySum == i:
            print (i, "is perfect")


main()




