# Name: Thomas Weis
# File: weis_lab5a.py
# Date: 03/18/21
#
# Desc: Finds biggest number in list 
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis

def largest(aList):
    #is given first value in list and if >, that becomes greatest value
    biggest = aList[0]
    for i in range(len(aList)):
        if aList[i] > biggest:
            biggest = aList[i]
            #print (aList[i])
    return biggest

#Don't need to change anything here
def main():
    l1=[1,2,3,4,5,6,7]
    l2=[2,8,5,7,8,56,7,445,78,9678,-4234]
    print(largest(l1), " is the biggest element.")
    print(largest(l2), " is the biggest element.")
    
main()
