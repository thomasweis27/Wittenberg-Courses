"""
Basics of Software Design
1. Get the requirements of what the code/software needs to do
    a. Do we understand the requirements and do they make sense?
2. Design a solution (not coding yet)
    a. Find the overview/overall big picture for the design...
    b. What sort of veriables and objects do you need?
    c. What finctions do we need?
    d. How is this all tied together?
3. Implement the design

"""
#Requetbaall Example
#Simulate a requetball game played by two players
#   Each rally is begun from player hitting ball until the other misses
#   Wins with 15 points and has two more than other player
#   one player is the server from the start
#   if the server misses the other player then serves
#   if the other player misses then the other player gets the point
#Needs to enter players skill leveles from 1 -100 (worse to best)
#for each rally, print who won and the current points and serve
#print who won the game

"""
What do we need to keep track of?
    points
    who the server is
    how many rallies
    any user inputs

overall design:
    print out title
    asks for player names
    asks for skill levels
    begin playing raquetball
        play a rallie
        add a point or change server
    when finished, display who won
"""

#Play a rally
#    need a loop that runs until someone misses
#    need to know who missed
#    implement a function that returns who missed
#    input: players skill levels
#playing a series of rallies
#    need a while loop
#    loop ends when someone wins
#    inside the loop:
#       play the rally
#       update the server or points
#How do we define when someone misses?
#   create a function that returns if someone his of misses
#   input - skill
#   output True/False if player hits and misses
#
#       Generate numbers from 1-100
#       if the number is greater than the skill level then the player misses
#
import random

def playerHitsBall(skill):
    x  = random.randrange(100)
    if x > skill:
        return False
    else:
        return True

def rally(player1Skill, player2Skill, server):
    while True:
        if server is 1:
            wins = playerHitsBall(player1Skill)
            print ("     One plays")
            if wins == False:
                return 1
            else:
                server = 2
        else:
            wins = playerHitsBall(player2Skill)
            print ("     Two plays")
            if wins == False:
                return 2
            else:
                server = 1

def main():
    print("Title")
    name1 = input("What is player one's name? ")
    skill1 = int(input("What is this players skill level? (1-100) "))
    name2 = input("What is player two's name? ")
    skill2 = int(input("What is this players skill level? (1-100) "))
    points1 = 0
    points2 = 0
    server = 1
    #   number of rallies
    while points1 != 15 and points2 != 15:
        if server == 1:
            print ("The server is player",  name1)
        else:
            print ("     The server is player", name2)
        loser = rally(skill1, skill2, server)
        print ("Player", loser, "lost the match.")
        if loser == 1 and loser !=server:
            points2 = points2 + 1
        elif loser == 1 and loser == server:
            server = 2
        elif loser == 2 and loser !=server:
            points1 = points1 + 1
        else:
            server = 1
        print (points1, name1,"      ", points2, name2)
    
    #play a series of rallies
    #play until someone wins

    #print who won and the score
main()



