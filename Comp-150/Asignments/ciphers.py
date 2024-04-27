def onlyLetters(text):
    strippedStr = ""
    
    for c in text:
        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
            strippedStr = strippedStr + c
            
    return strippedStr

def encryptShift(plaintext, shift):
    plaintext = onlyLetters(plaintext.upper())

    shift = ord(shift.upper()) - ord('A')
    
    ciphertext = ""
    
    for c in plaintext:
        ciphertext = ciphertext + chr(((ord(c) - ord('A') + shift) % 26) + ord('A'))
        
    return ciphertext


def decryptShift(ciphertext, shift):
    ciphertext = onlyLetters(ciphertext.upper())

    shift = ord(shift.upper()) - ord('A')
    
    plaintext = ""
    
    for c in ciphertext:
        plaintext = plaintext + chr(((ord(c) - ord('A') - shift) % 26) + ord('A'))
        
    return plaintext

def encryptSubstitution(plaintext, cipheralphabet):
    plaintext = onlyLetters(plaintext.upper())
    
    ciphertext = ""
    
    for c in plaintext:
        ciphertext = ciphertext + cipheralphabet[ord(c) - ord('A')]
        
    return ciphertext

def decryptSubstitution(ciphertext, cipheralphabet):
    ciphertext = onlyLetters(ciphertext.upper())
    
    plaintext = ""
    
    for c in ciphertext:
        plaintext = plaintext + chr(ord('A') + cipheralphabet.index(c))
        
    return plaintext

#NOT USED YET EITHER!!!!
def keyPhraseGen(key):
    
    key = onlyLetters(key.upper()) + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipheralphabet = ""
    
    for c in key:
        if not (c in cipheralphabet):
            cipheralphabet = cipheralphabet + c
            
    return cipheralphabet

def encryptKeyPhraseSub(plaintext, key):
    return encryptSubstitution(plaintext, keyPhraseGen(key))

def decryptKeyPhraseSub(ciphertext, key):
    return decryptSubstitution(ciphertext, keyPhraseGen(key))

def encryptRailfence(plaintext, levels):
    
    plaintext = onlyLetters(plaintext.upper())
    
    fence = []
    for _ in range(levels):
        fence.append([])
        
    inc = 1
    row = 0
    col = 0
    
    for c in plaintext:
        for i in range(levels):
            fence[i].append('')
        
        fence[row][col] = c
        if row == levels - 1:
            inc = -1
        elif row == 0:
            inc = 1
            
        row += inc
        col += 1
        
    # for r in fence:
    #     for c in r:
    #         print(f'{c:.<1s}',end='')
    #     print()

    for i in range(levels):
        fence[i] = ''.join(fence[i])
        
    ciphertext = ''.join(fence)
    
    return ciphertext
    
def decryptRailfence(ciphertext, levels):
    
    fence = []
    for _ in range(levels):
        fence.append([])
        
    inc = 1
    row = 0
    col = 0
    
    for i in range(len(ciphertext)):
        for j in range(levels):
            fence[j].append('')
        
        fence[row][col] = '.'
        
        if row == levels - 1:
            inc = -1
        elif row == 0:
            inc = 1
            
        row += inc
        col += 1
    
    row = 0
    col = 0
    
    for c in ciphertext:
        while fence[row][col] != '.':
            col += 1
            if col == len(ciphertext):
                col = 0
                row += 1
                
        fence[row][col] = c
        
    # for r in fence:
    #     for c in r:
    #         print(f'{c:.<1s}',end='')
    #     print()
    
    plaintext = ''
    
    inc = 1
    row = 0
    col = 0
    
    while len(plaintext) != len(ciphertext):
        plaintext += fence[row][col]
        
        if row == levels - 1:
            inc = -1
        elif row == 0:
            inc = 1
            
        row += inc
        col += 1
        
    
    return plaintext
