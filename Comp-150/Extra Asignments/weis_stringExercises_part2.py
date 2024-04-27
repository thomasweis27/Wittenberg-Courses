#
# Name: Thomas Weis
# File: weis_stringExercises_part2.py
# Date: 03/10/2021
#
# Desc: finds the frequency of letters in a word
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

    new = "" 
    
    for i in range(x):
        count = 1
        for k in range(x):
            if string[i] == string[k] and i != k:
                count = count + 1
                #removes duplicate letters and counts how many times they occur
                string = string[:k] + " " + string[k+1:]

        #if the letter is not duplicated then put it in the new string
        if string[i] != " ":
            new = new + "'"+string[i]+"': " + str(count) + " "

        
    print ("{" + new + "}")

    
main()
