#
# Name: Thomas Weis
# File: weis_lab10a.py
# Date: 04/29/21
#
# Desc: finds sums recursively
#
# I Received Help From: You and TA in Lab
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis


def main():
    tList0 = [1, 4, 3, 1/4]
    tList1 = [1, 4, 7, 13, 100.5]
    tList2 = [78, 18, 7, 16, 0, -6]
    print(recSum(tList0))
    print(recSum(tList1))
    print(recSum(tList2))

def recSum(aList):
    if len(aList) <= 0:
        return 0

    last = aList[(len(aList)-1)]
    aList.pop()
    Sum = last + recSum(aList)
    return Sum



main()
