# Name: Thomas Weis
# File: weis_assignment5.py
# Date: 4/23/21
#
# Desc: Creating and maintaining a list of confrence atendees.
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis



class Guest():
    def __init__(self, name, company, state, email):
        self.name = name
        self.company = company
        self.state = state
        self.email = email

    def getName(self):
        return self.name

    def __str__(self):
        return "Attendee: {}, Email: {}".format(self.name, self.email)

    def getStats(self):
        return "Attendee: {}, Company: {}, State: {}, Email: {}".format(self.name, self.company, self.state, self.email)






def removeGuest(fileIn, name):
    #removes guest from the file by checking where the guest is in the file
    # first and then writing the file again with - - - - instead of the person. 
    file = open(fileIn, "r")
    fullDoc = ""
    currentLine = file.readline()
    while currentLine != "":
        if currentLine[:len(name)] == name:
            fullDoc = fullDoc + "- - - -\n"
        else:
            fullDoc = fullDoc + currentLine
        currentLine = file.readline()
    file.close()

    file = open(fileIn, "w")
    file.write(fullDoc)
    file.close
    
        




def addGuest(fileIn, newName, newCompany, newState, newEmail):
    #adds new guest to file based on inputs - is very similar to removing def above.
    file = open(fileIn, "r")
    used = False
    fullDoc = ""
    currentLine = file.readline()
    while currentLine != "":
        if currentLine[0] == "-":
            fullDoc = fullDoc + newName + " " + newCompany + " " + newState + " " + newEmail + "\n"
            used = True
        else:
            fullDoc = fullDoc + currentLine
        currentLine = file.readline()
    if used == False:
        fullDoc = fullDoc + newName + " " + newCompany + " " + newState + " " + newEmail + "\n"
    file.close()

    file = open(fileIn, "w")
    file.write(fullDoc)
    file.close






def importToClass(fileIn):
    #function to open file and make each part of the class
    file = open(fileIn, "r")
    guestList  = file.readline()
    peopleList = []
    x = 1
    guestListList = []
    while guestList != "":
        spaceList = []
        guestName = "guest" + str(x)  #use this to define each guest
        peopleList.append(guestName)
        for i in range (len(guestList)):
            if guestList[i] != " ":
                pass
            else:
                spaceList.append(i)
                #makes a list of whenever there is a space

        #at each space, make a new veriable to pass into to the Class
        a = guestList[0:spaceList[0]]
        b = guestList[spaceList[0]+1: spaceList[1]]
        c = guestList[spaceList[1]+1: spaceList[2]]
        d = guestList[spaceList[2]+1: ]


        #pass into class
        guestName = [a, b, c, d]
        guestListList = guestListList + guestName
        x = x + 1
        guestList = file.readline()
    file.close()
    #return peopleList
    return guestListList
    return False

def menu():
    #simple menu option
    print()
    print("What action would you like?")
    print("    1. Add an attendee.")
    print("    2. Delete an attendee.")
    print("    3. Display attendee information.")
    print("    4. List all attendee names and emails.")
    print("    0. Exit")


def menuChoice3(name, leaving, guest1, guest2, guest3, guest4):
    if name != leaving: #in case gotten rid of guest from list
        if guest1.getName() == name:
            print(guest1.getStats())
        elif guest2.getName() == name:
            print(guest2.getStats())
        elif guest3.getName() == name:
            print(guest3.getStats())
        elif guest4.getName() == name:
            print(guest4.getStats())
        else:
            print ("No attendee by that name")
    else:
        print ("No remaining attendee by that name")



def menuChoice4(leaving, guest1, guest2, guest3, guest4):
            if guest1.getName() != "-" and guest1.getName() != leaving:
                print(guest1)
            if guest2.getName() != "-" and guest2.getName() != leaving:
                print(guest2)
            if guest3.getName() != "-" and guest3.getName() != leaving:
                 print(guest3)
            if guest4.getName() != "-" and guest4.getName() != leaving:
                print(guest4)


    
def main():
    print("Welcome to the conference")
    fileIn = input("Enter the name of the file containing saved information: ")
    leaving  = ""
    
    #takes fileIn and pass the guests into the Guest class
    peopleList = importToClass(fileIn)

    numOfGuests =((len(peopleList))//4)

    guest1 = Guest(peopleList[0], peopleList[1], peopleList[2], peopleList[3])
    guest2 = Guest(peopleList[4], peopleList[5], peopleList[6], peopleList[7])
    guest3 = Guest(peopleList[8], peopleList[9], peopleList[10], peopleList[11])
    guest4 = Guest(peopleList[12], peopleList[13], peopleList[14], peopleList[15])


    
    while True:
        menu()
        choice = int(input("Your choice? "))





    #gives uses the input to get what the user wants
        if choice == 0:
            return False
        elif choice == 1:
            newName = input("Enter the attendee name: ")
            newCompany = input("Enter the attendee company: ")
            newState = input("Enter the attendee state: ")
            newEmail = input("Enter the attendee email: ")

            #function in menu Item one
            addGuest(fileIn, newName, newCompany, newState, newEmail)


            if guest1.getName() == "-":
                guest1 = Guest(newName, newCompany, newState, newEmail)
                leaving  = ""
            elif guest2.getName() == "-":
                guest2 = Guest(newName, newCompany, newState, newEmail)
                leaving  = ""
            elif guest3.getName() == "-":
                guest3 = Guest(newName, newCompany, newState, newEmail)
                leaving  = ""
            elif guest4.getName() == "-":
                guest4 = Guest(newName, newCompany, newState, newEmail)
                leaving  = ""
            else:
                guest5 = Guest(newName, newCompany, newState, newEmail)



        
        elif choice == 2:
            leaving = input("Enter the attendee name to remove: ")
            #function in menu Item 2
            removeGuest(fileIn, leaving)
            
        elif choice == 3:
            name = input("Enter the attendee name to display: ")
            #function for Menu Item 3
            menuChoice3(name, leaving, guest1, guest2, guest3, guest4)

        elif choice == 4:
            #function for Menu Item 4
            menuChoice4(leaving, guest1, guest2, guest3, guest4)
            
        else:
            print ("Not a valid option!")

main()
