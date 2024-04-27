# Name: Thomas Weis
# File: weis_lab5c.py
# Date: 03/18/21
#
# Desc: Creates and valadates usernames and passwords 
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis


#userData [[account, password], [account, password], etc.] 
def isCorrect(userData, user, password):
    for i in range(len(userData)):
        #find the username is in the list 
        if userData[i] == user:
            spot = userData.index(user)
            #the things after the username in the list is the password
            #checks to see if the password is correct to the username
            if userData[(spot+1)] == password:
                return True
            else:
                return False

        

def main():

    print("Account Verifier Running...")
    

    '''Loads passArr array with username password arrays.'''
    userData=[]


    '''Allows a user to select to create a new account or loginto an existing account.
        try entering print(userData) into the prompt below.'''
    userSelect=0
    while(userSelect!=1 and userSelect!=2):
        print("\nEnter 1 to login.")
        print("Enter 2 to create a new account.")
        print("Enter 3 to exit. \n")
        userSelect=int(input("Enter choice: "))

        '''Creates a new account.'''
        if(userSelect==2):
            x = input("Enter your username: ")
            y = input("Enter your password: ")
            userData.append(x)
            userData.append(y)
            #print(userData)

        elif(userSelect==1):
            
            '''This loop breaks when a username and password are correct. 
                We initialize user to i1 so that we can enter the loop and because -1
                isnt the index of an actual user.'''
            isAllowedEntry=False
            print("\nEnter login info.")
            while(not isAllowedEntry):
                
                username=input("Enter your username: ")
                password=input("Enter your password: ")
                print("\n")
                
                #Use your function to see
                isAllowedEntry=isCorrect(userData, username, password)

            print("Congrats, you're in!")

        elif(userSelect == 3):
            print("Goodbye")
            break

        userSelect = 0
main()
