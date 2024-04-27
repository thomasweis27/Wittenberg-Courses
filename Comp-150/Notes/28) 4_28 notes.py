#Insertion Sort
#   we insert the item into the correct positon in a list
#   there is a sorted part of list(starts empty) and unsorted

alist = [3, 7, 2, 1, 5, 4]

def insertionSort(alist):
    i=1

    while i < len(alist):
        j = i #j is index element
        while j > 0 and alist[j] < alist[j-1]:
        #keep swapping until object in correct spot
            tmp = alist[j]
            alist = alist[j-1]
            alist[j-1] = tmp
            j = i - 1
        i = i + 1

print(insertionSort(alist))
