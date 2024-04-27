# Name: Thomas Weis
# File: weis_lab07.py
# Date: 04/01/21
#
# Lists Sentence, Word, Letter, Character, Consonant, & Vowel Count of file
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis


def main():
    openfile = input("Enter file name: ")
    file = open(openfile, "r")
    address =(file.read())
    file.close()
    print()


#finds the number of sentences
    sen = 0

    for i in range (len(address)):
        if address[i] == ".":
            sen = sen + 1
    print ("Sentence Count =", sen)
        
#finds the number of words
    words = 0
    for i in range (len(address)):
        if address[i] == " " and address[i-1] != "-":
            words = words + 1
    print ("Word Count =", words)

#finds the number of characters
    print ("Character Count =", len(address))


#finds the number of Letters
    let = 0
    letList = ("")
    for i in range (len(address)):
        if address[i] >= "A" and address[i] <= "z":
            let = let + 1
            letList =letList + address[i]
    print ("Letter Count =", let)

    letList = letList.lower()
    #print (letList)


#finds the number of Vowels
    vow = 0
    for i in range (len(letList)):
        if letList[i] == "a" or letList[i] == "e" or letList[i] == "i" or letList[i] == "o" or letList[i] == "u":
            vow = vow + 1
    print ("Vowel Count =", vow)

#finds the number of consonants
    print ("Consonant Count =", (len(letList)- vow))


main()

