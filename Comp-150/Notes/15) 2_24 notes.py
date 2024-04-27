def addOne(number):
    number = number +1
    print ("Function", number)
    return number   #<- return is the output, no output, no return


number =5
number2 = addOne(number) #must have () at end in order to run

print ("origional", number)
print ("num +1 is", number2)

#more about lists

alist = [1, 2, 3, 'a', "b", "c"]
print (alist)

x = alist[3]
print (x)

#alist[index] = newValue

alist[5] = "cookie monster"
alist.append(42)
print (alist)

for item in alist:
    print("hi")

#concatainate

blist = [5, 6, 7, True]
clist = alist + blist
print (clist)

"""
listOfNums = []
for i in range(5):
    num = int(input("Enter number: "))
    listOfNums = listOfNums + [ num ]
print (listOfNums)
"""

#Copying a list

#This doesnt work:
#copiedList = origionalList
#any change done to origional list is reflected into the copied list
#both the origional and copied list refers to the same thing

olist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
clist = olist
olist[4] = 90000
print(olist)
print(clist) #only changed one but they both changed

#how to do it:
#copiedList = origionalList.copy()

item = 7

spot = len(olist)
index = -1
for i in range(spot):
    if olist[i] == item:
        index = i
        break

print ("the item", item, "is in spot ", i)

#find the loscation of something that is in there
idxOfA = alist.index('b')
print(idxOfA)

#removes ONLY THRE FIRST OCCURANCE of th item in perenthasies
alist.remove('cookie monster')
print (alist)

clist.clear()
print (clist)

n =7
nItemList = [item]*n
print(nItemList)


#this can be used for something lipe importing random numbers from 0-1000
import random
randomlist = [0]*100
for i in range(100):
    rN = random.randrange(1000)
    randomlist[i] = rN

print (randomlist)

