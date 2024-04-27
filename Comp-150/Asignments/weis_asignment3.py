#
# Name: Thomas Weis
# File: weis_asignment3.py
# Date: 03/05/2021
#
# Desc:  Encodes and Decodes messages
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis



def generateKeyPhrase(key, length):
    origKey = key
    #makes the key longer until it is >= the phrase length
    while len(key) < length:
        key = key + origKey
    while len(key) != length:
    #if is is then an over phrase lengh, it will remove one letter at a time
        key = key[:(len(key)-1)]
    return key #Phrase

def viginereEncrypt(plaintext, key):
    plaintext = plaintext.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    #makes this happen for each letter of the keyPhrase
    for i in range(len(key)):
        alphabetKey = alphabet
        alphabetEncript = alphabet
        letterInString = 0
        #makes the first letter in the alphabet the last until
        #  the beginning letters of both are the same.
        while alphabetKey[0] != key[i]:
            alphabetKey = alphabetKey[1:] + alphabetKey[:1]
            
        #finds what number for each letter (a=0, b=1, c=2 and so on)
        while alphabetEncript[0] != plaintext[i]:
            alphabetEncript = alphabetEncript[1:] + alphabetEncript[:1]
            letterInString = letterInString +1

        #adds discovered letter to the string to form the coded message...
        y = alphabetKey[letterInString]
        ciphertext = ciphertext + y

    ciphertext = ciphertext.upper()
    return ciphertext




def viginereDecrypt(ciphertext, key):
    ciphertext = ciphertext.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plaintext = ""
    #makes this happen for each letter of the keyPhrase
    for i in range(len(key)):
        alphabetKey = alphabet
        alphabetDecript = alphabet
        letterInString = 0
        #makes the first letter in the alphabet the last until
        #  the beginning letters of both are the same.
        while alphabetKey[0] != key[i]:
            alphabetKey = alphabetKey[25:] + alphabetKey[:25]
        alphabetDecript = alphabetKey
        #finds what letter of the alphabet each letter is
        while alphabetDecript[0] != ciphertext[i]:
            alphabetDecript = alphabetDecript[1:] + alphabetDecript[:1]
            letterInString = letterInString +1

        #adds discovered letter to the string to form word/phrase
        y = alphabet[letterInString]
        plaintext = plaintext + y
    return plaintext




def onlyLetters(str1):
    # Returns string with only letters (given)
    str2 = ""
    for k in range(len(str1)):
        ch = str1[k]
        if (ch >= 'a' and ch <= 'z') or (ch>='A' and ch <= 'Z'):
            str2 = str2 + ch
    return str2



def main():
    #asks for info and then En/decripts
    print("Viginere Cipher Program"), print()
    ED = input("Enter (e)ncrypt or (d)ecrypt: ")
    if ED == "e":
        plaintext = input("Enter the plaintext: ")
        plaintext = onlyLetters(plaintext)
        key = input("Enter the key: ")
        print("The  encrypted ciphertext is: ")
        length = len(plaintext)
        keyPhrase = generateKeyPhrase(key, length)
        key = keyPhrase
        ciphertext = viginereEncrypt(plaintext, key)
        print (ciphertext)

        
    elif ED == "d":
        ciphertext = input("Enter the ciphertext: ")
        key = input("Enter the key: ")
        print("The decrypted plaintext is:")
        length = len(ciphertext)
        keyPhrase = generateKeyPhrase(key, length)
        key = keyPhrase
        plaintext = viginereDecrypt(ciphertext, key)
        print (plaintext)

    else:
        print("That is not a valid option.")




main()
