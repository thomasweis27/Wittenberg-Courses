# Lists
# the item is given from how far the item is from the first item

# Zero-Based Indexing
#    the first item take spot (index) 0
#    the second item takes spot (index) 1
#    the third item takes index three

#listName = [item0, item1, item2, item3]   <- can put whatever you want inside

tsList = ["Thomas", "Is", "Making", "a", "List"]
print (tsList)
"""
print(tsList[1]) #<-pick something out of the list
print(tsList[2:5]) #<- gets part of list (numbers up to but not including 5)
print(tsList [:4]) #<-goes from beginning to spot 4
print(tsList [2:])

lengthOfList = len(tsList)
print("The length of the list is", lengthOfList)
"""

numbers0To9 = list(range(10))
print (numbers0To9)

for item in tsList:                 #item in for statment and in used below
    print("word in list is", item)

