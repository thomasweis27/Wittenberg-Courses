# Name: Thomas Weis
# File: weis_assignment4.py
# Date: 4/9/21
#
# Desc: Menu system for encrypting/decrypting files.
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis

from ciphers import *

# create any additional functions you may need here

    
def main():
    print(f'Encryption/Decryption Program\n')

    while True:
    # Ask user if they want to encrypt, decrypt, or quit
        print("Choose one of the following: ")
        print("    (e)ncrypt \n    (d)ecrypt \n    (q)uit")
        edq = input("Choice: ")

        if edq == "q":
            return False

    #perform the appropriate action.
        print ("Enter number for cipher would you like to use?")
        print("1. Shift Cipher\n2. Substitution Cipher\n3. Keyphrase Cipher\n4. Railfence Cipher")
        cipher = int(input("Choice: "))

        if edq == "e":
            fileIn = input("What file would you like to encrypt? ")
        elif edq == "d":
            fileIn = input("What file would you like to decrypt? ")

    #opens the file that was input
        file = open(fileIn, "r")
        fileInsides  = file.read()
        file.close()

    #look at yellow hilight in thing
        #key = ""
        #while key >= "A" and address[i] <= "z":
        if cipher == 1:    
            key = input("Enter the key letter for the Shift Cipher: ")
        elif cipher == 2:
            key = input("Enter the alphabet for the Substitution Cipher (capital letters): ")
        elif cipher == 3:
            key = input("Enter the key for the Keyphrase Cipher: ")
        elif cipher == 4:
            key = int(input("Enter the levels for the Railfence Cipher: "))

        #fileOut = ("What file would you like to store the ciphertext? ")


    #makes the input usable to be cipher-ed
        readyInsides = onlyLetters(fileInsides)



    #sees how to store the output
        if edq == "e":
            fileOut = input("What file would you like to store the ciphertext? ")
        elif edq == "d":
            fileOut = input("What file would you like to store the plaintext? ")


    #encrypting and decripting begins here!
        if cipher == 1 and edq == "e":
            cryption  = encryptShift(readyInsides, key)
        elif cipher == 2 and edq == "e":
            cryption  = encryptSubstitution(readyInsides, key)
        elif cipher == 3 and edq == "e":
            cryption  = encryptKeyPhraseSub(readyInsides, key)
        elif cipher == 4 and edq == "e":
            cryption  = encryptRailfence(readyInsides, key)
        elif cipher == 1 and edq == "d":
            cryption  = decryptShift(readyInsides, key)
        elif cipher == 2 and edq == "d":
            cryption  = decryptSubstitution(readyInsides, key)
        elif cipher == 3 and edq == "d":
            cryption  = decryptKeyPhraseSub(readyInsides, key)
        elif cipher == 4 and edq == "d":
            cryption  = decryptRailfence(readyInsides, key)



    #makes new file with output
        file2 = open(fileOut, "w")
        file2.write(cryption)
        file2.close()




if __name__ == '__main__':
    main()
