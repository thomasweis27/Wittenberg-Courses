#
# Name: Thomas Weis
# File: weis_lab3d.py
# Date: 02/11/21
#
# Desc: Computes if numbers are abundant, perfect, or deficient
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis


n = int(input("Enter a number: "))
mySum = 0 

#finds all divisors and puts them in a row
print()
print ("Divisors:")
for i in range (1, n):
    if n%i == 0:
        print (i, end=", ")
        mySum = mySum + i

#determines and outputs the sum and clasifacation
print(), print()
print ("The sum the of proper divisors of",n , "is" , mySum)

if mySum > n:
    print (n, "is abundant")
elif mySum == n:
    print (n, "is perfect")
else:
    print (n, "is deficient")
