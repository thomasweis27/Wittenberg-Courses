#
# Name: Thomas Weis
# File: weis_asignment2.py
# Date: 03/08/2021
#
# Desc:  Calculates the return on investment in a stock fund
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis

#asks the user for a bunch of inputs and then returns 
#    stockNumber, initialBalance, initialAnnualRate, monthlyRateChangeYear1,
#    and monthlyRateChangeYear2 in a list for easy access. 
def getUserInput(infoList):
    stockNumber = input("Enter stock account number: ")
    initialBalance = int(input("Enter initial balance: "))
    initialAnnualRate = int(input("Enter initial annual % rate year 1: "))
    monthlyRateChangeYear1 = float(input("Enter monthly rate % change year 1: "))
    monthlyRateChangeYear2 = float(input("Enter monthly rate % change year 2: "))
    infoList = [stockNumber, initialBalance, initialAnnualRate, monthlyRateChangeYear1, monthlyRateChangeYear2]
    return infoList

#outputs the rate and balance increase of money per month of year one
def year1Output(initialBalance, initialAnnualRate, monthlyChangeYear1):
    rate = initialAnnualRate
    month = 0
    balance = initialBalance
    print("Year  Month  Rate  Balance")
    for i in range(12):
        month = month + 1
        balance =  balance*(rate/100/12) +balance
        #now that the math is done, the information is given


        #if statment is used to make proper spacing between months with 1 and
        # months with two digits.
        if month >=10:
            print ("  1    ", month,"   {:.1f}" .format(rate), "  ${:.2f}" .format(balance))
        else:
            print ("  1    ", month,"    {:.1f}" .format(rate), "  ${:.2f}" .format(balance))
        rate = rate + (monthlyChangeYear1)
        
    returnItems = [balance, rate]
    return returnItems

#outputs the rate and balance increase of money per month of year two
def year2Output(initialBalance, initialAnnualRate, monthlyChangeYear2):
    rate = initialAnnualRate
    month = 12
    balance = initialBalance
    #print("Year  Month  Rate  Balance")
    for i in range(12):
        month = month + 1
        balance = balance + balance*(rate/100/12)
        #now that the math is done, the information is given
        print ("  2    ", month,"   {:.1f}" .format(rate), "  ${:.2f}" .format(balance))
        rate = rate + (monthlyChangeYear2)

    returnItems = [balance, rate]
    return returnItems

#uses the definitions above to run the program
def main():
    infoList = []
    infoList = getUserInput(infoList)
    t = infoList[0]
    print(), print()
    print("Account: ", infoList[0])
    print(), print()
        # Compute end of month balances for year 1 and output
    r = year1Output(infoList[1], infoList[2], infoList[3])
        # Compute end of month balances for year 2 and output
    y = year2Output(r[0], r[1], infoList[4])


main()
