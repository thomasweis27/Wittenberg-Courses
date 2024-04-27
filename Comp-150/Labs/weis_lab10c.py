#
# Name: Thomas Weis
# File: weis_lab10c.py
# Date: 04/29/21
#
# Desc: finds all possible paswords recursively
#
# I Received Help From: You and TA in Lab
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis


def main():
    #charSet is a list of characters that could
    #      appear in the password to be guessed
    charSet = ['a', 'b', 'c', 'd']
    length=int (input ("Enter the password length: "))
    print("The number of possiable passwords is", len(charSet)**length)
    passwordGuesser (charSet, length, "")

    

def passwordGuesser(charSet, length, currResult):
    #base case
    if len(currResult)==length:
        print(currResult)

    else:
        for i in charSet:
            passwordGuesser(charSet, length, currResult+i)
            

    


main()
