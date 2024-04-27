#continuing strings functions
#    note: cant change strings - only make new ones
#    if you capatalize or something you must (str1 = str1 + edits_made)
#          for the changes to actually stay

str1 = "abcd"
str2 = "efgh"

str3 = str1 + " " + str2
print (str3)
print(str3.capitalize())         #.capitalize()

str1 = str1.upper()              #.upper()
print (str1)

str1 = str1.lower()              #.lower()
print (str1)

print("42".isdigit())            #.isdigit()
print("4.2".isdigit())
        #tells user if the string only has numbers 
        #   0-9 (decimals not included)

str3 = str3.split()              #.split()
print(str3) #splits string into spaces
            #if you put something in the perenthasees
            #    then it will split based on that item
example = "q,w,e,r,t,y,u,i,o,p"
print(example.split(','))


# CAN NOT:
#   subtract letters out of strings
#   multiply a string times another string
print(str1 * 3) #this is fine because not two strings
#   cant replace letters the same way as in a list

new = str1[:1]+'hello'+ str1[3:]
print (new) #how to replace letters

