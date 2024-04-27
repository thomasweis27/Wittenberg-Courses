"""
Dictionaries:
    words and definitions become keys and values
     in pyton values can be the same, not keys

{key1:value1, key2:value2, key3:value3....}
"""


myDict = {"veriable":"something that stores a value", 
          "function":"code that does a procedure",
          "constant":"a fixed value"}

print(myDict)
#good for one structure with two sets of information - (1 set is good for list)

m = "function"
print(m, ": definition is:", myDict[m])

print()
for k in myDict:
    print(k, myDict[k])


print()
#test to see if ke is in dict
if "definition" in myDict:
    print("this key is in the dict")

else:
    print("key is NOT in dict")

myDict["Thomas Weis"] = 5
myDict["Thomas Weis"] = myDict["Thomas Weis"] + 1
print(myDict["Thomas Weis"])

#also good for a program that counts the number of characters in a string
#    add new letters to dict
#    add one to numbers already in dict


