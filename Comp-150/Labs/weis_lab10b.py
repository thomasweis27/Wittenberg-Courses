#
# Name: Thomas Weis
# File: weis_lab10b.py
# Date: 04/29/21
#
# Desc: finds fib numbers recursively
#
# I Received Help From: You and TA in Lab
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis


def main():
    print(fib(4))
    print(fib(18))
    print(fib(7))
    print(fib(31))

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    answer = fib(n-1) + fib(n-2)
    return answer



main()
