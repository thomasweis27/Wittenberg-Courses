#Selection Sort
#   basic idea - take smallest and swap it with that is at position 0

alist = [3, 7, 2, 1, 5, 4]


for i in range(0, len(alist)):
    smallestNumber = alist[i]
    smallestPosition = i
    for j in range(i, len(alist)):
        if alist[j] < smallestNumber:
            smallestNumber = alist[j]
            smallestPosition = j

    tmp = alist[i]
    alist[i] = smallestNumber
    alist[smallestPosition] = tmp

print(alist)

    

        

