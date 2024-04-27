#
# Name: Thomas Weis
# File: weis_lab4a.py
# Date: 03/04/21
#
# Desc: Determines the furture value of an investment 
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis


print("Future Value Program\n")

def getInput():
    #gets all inputs and returns them to be used later
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter annual percentage rate: "))
    yr = eval(input("Enter number of years: "))
    return principal, apr, yr

def futureValue(principal, apr, yrs):
    #solves for the new principal
    for k in range(1,yrs+1):
        principal = principal *(1.0 + apr)
    return principal

def main():
    # get input
    principal, apr, yrs = getInput()

    # compute future value
    futureVal = futureValue(principal, apr, yrs)

    # print results
    print("\nThe value in",yrs,"years is $",int(futureVal*100+0.5)/100)
    print()

main()

