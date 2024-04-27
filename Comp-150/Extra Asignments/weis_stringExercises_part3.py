#
# Name: Thomas Weis
# File: weis_stringExercises_part3.py
# Date: 03/10/2021
#
# Desc: replaces repeated letters in a given string
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis


def main():
    string = input("Please enter a string: ")
    x = len(string)

    #for every letter except that of the place i is
    #  replace it with a '$'
    
    for i in range(x):
        for k in range(x):
            if string[i] == string[k] and i != k:
                string = string[:k] + "$" + string[k+1:]
                
    print (string)

    
main()
