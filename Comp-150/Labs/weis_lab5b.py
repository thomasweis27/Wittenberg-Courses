# Name: Thomas Weis
# File: weis_lab5b.py
# Date: 03/18/21
#
# Desc: Creates and maintains a guest list for a resturant 
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis

def main():
    print("Guest List program running.")
    waitList=[]
    promptSelect=0
    while(promptSelect!=4):

        print("\n")
        print("Enter 1 to add  a party to the wait list.")
        print("Enter 2 to call the next party in line.")
        print("Enter 3 to remove a party from the list.")
        print("Enter 4 to close.")
        print("\n")
        
        promptSelect=int(input("Your selection: "))

        if promptSelect==1:
            x = input("Enter party name: ")
            waitList.append(x)
            #print (waitList)
            
        elif promptSelect==2:
            print (waitList[0], "is next.")
            waitList.remove(waitList[0])
            #print (waitList)


        elif promptSelect==3:
            x = input("Enter name to remove: ")
            removedPerson = waitList.index(x)
            waitList = waitList[:(removedPerson)] + waitList[(removedPerson+1):]
            #print (waitList)


        elif promptSelect==4:
            print("Have a nice day!")
main()

                         
