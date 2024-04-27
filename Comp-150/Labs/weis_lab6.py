# Name: Thomas Weis
# File: weis_lab6.py
# Date: 03/25/21
#
# This program simulates a 1 on 1 basketball game.
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis


import random

def madeShot(shootingPercentage):
    x  = random.randrange(100)
    if x > shootingPercentage:
        return False
    else:
        return True



#This function allows players to shoot back and forth until one of them makes a shot.
def scoreAPoint(player1ShootingPercentage, player2ShootingPercentage, ballControl):

    pointScored = False

    while not pointScored:
        if ballControl == 1:
            point = madeShot(player1ShootingPercentage)
            #print ("     One plays")
            if point == False:
                return 1
            else:
                ballControl = 2
        else:
            point = madeShot(player2ShootingPercentage)
            #print ("     Two plays")
            if point == False:
                return 2
            else:
                ballControl = 1




#This function runs an entire game to 15 scoring by 1.
def game():

    #Get player 1 info
    player1Name = input("Enter player 1 name: ")
    player1ShootingPercentage = int(input("Enter " + player1Name + "'s shooting percentage: "))
    player1Score = 0
    #get player 2 info
    player2Name = input("Enter player 1 name: ")
    player2ShootingPercentage = int(input("Enter " + player2Name + "'s shooting percentage: "))
    player2Score = 0
    print()

    #let player 1 have the ball first
    ballControl = 1


    #while no one has won yet
    while (player1Score < 15 and player2Score < 15):
        
        scorer = scoreAPoint(player1ShootingPercentage, player2ShootingPercentage, ballControl)

        #print (scorer)

        #if scorer is player 1
        if scorer == 2:
            print(player1Name, "scores!")
            player1Score = player1Score + 1

        #else if player 2 scores
        if scorer == 1:
            print(player2Name, "scores!")
            player2Score = player2Score + 1

    if player1Score == 15:
        print(), print ("The winner was", player1Name)
    else:
        print(), print ("{} wins!".format( player2Name))
    print ("Final Score: {}:{} - {}:{}".format(player1Name, player1Score, player2Name, player2Score))
    



def main():
    game()

main()
