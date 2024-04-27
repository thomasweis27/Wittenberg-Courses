# Loops

i=0
print (i)
i=1
print (i)
i=2
print (i)
i=3
print (i), print()

for i in range(4):   #list of numbers from 0 to number-1
    print (i)
    print ("Loop ideration", i)
    #code needed to repeat goes in here tabed over
print("Loop ended"), print()


#for i in range (start, end, number_counted_by)

for i in range (2, 7, 2):
    print (i)


print()
theSum = 0

for i in range (1, 10):
    theSum = theSum+i
print (theSum)


print(list(range(11))) #list range is good tool to see what range is genorated

print(list(range(10, -1, -1)))
print(), print(), print(), print()




totalValue = 0
for i in range(5):
    num = int(input("Please give number: "))
    totalValue = totalValue + num

print (totalValue)


    
