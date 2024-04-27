#
# Name: Thomas Weis
# File: weis_asignment1.py
# Date: 02/05/2021
#
# Desc:  Calculates Cell Phone Cost for the Month 
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis

def main():
    #step one - asks for phone plan
    plan = input("Enter your wireless phone plan (A, B, or C): ")
    print ()


    #step two - asks for remainder of user info
    minutes = int(input("Enter the number of minutes you have used: "))
    messages = int(input("Enter the number of messages you have used: "))
    data = int(input("Enter the amount of data you have used (in MB): "))
    print(), print(), print()


    #step three - calculates minutes based on plan
    cost = float(0)

    if plan == "a":
        cost = minutes * .10 + messages*.10 + data * .01
    elif plan == "b":
        if minutes > 1000:
            minutes2 = minutes - 1000   #minutes2, messages2, and data2 is just convienient 
        else:                           #for knowing/storing amount gone over the plan
            minutes2 = 0
        if messages > 2000:
            messages2 = messages - 2000
        else:
            messages2 = 0
        if data > 5000:
            data2 = data - 5000
        else:
            data2 = 0
        cost  = 39.99 + minutes2 * .05 + messages2 * .05 + data2 * .01
    elif plan == "c":
        cost = 79.99
    else:
        print ("Not a valid plan.") #if something else entered


    #step 4

    #prints all info for plan a based on calculations above
    if plan == "a":     
        print ("Your total monthly cost: ${:.2f}" .format(cost))
        print ("  Minutes Used: " + str(minutes))
        print ("    Cost/Min: $0.10, Total Minute Cost: ${:.2f}" .format(minutes * .10))
        print ("  Message Used: "+ str(messages))
        print ("    Cost/Message: $0.10, Total Message Cost: ${:.2f}" .format(messages*.10))
        print ("  Data Used (MB): " + str(data))
        print ("    Cost/MB: $0.01, Total Data Cost: ${:.2f}" .format(data * .01))

    #prints all info for plan b based on calculations above
    elif plan == "b":   
        print ("Your total monthly cost: ${:.2f}" .format(cost)) 
        print()
        print ("Monthly Plan Cost: $39.99")
    
        print ("  Minutes Used: " + str(minutes))
        #series of if statements used to see if you went over the minutes in the user's plan
        if minutes >1000:  
            print("    Included Minutes Used: 1000, Additional Minutes Used: " + str(minutes2))
            print ("    Cost/Min: $0.05, Additional Minute Cost: ${:.2f}" .format(minutes2*.05))
        else:
            print("    Included Minutes Used: " + str(minutes) + ", Additional Minutes Used: 0")
            print ("    Cost/Min: $0.05, Additional Minute Cost: $0.00")

        print ("  Message Used: "+ str(messages))
        if messages > 2000:
            print("    Included Message Used: 1000, Additional Messages Used: " + str(messages2))
            print ("    Cost/Message: $0.05, Additional Message Cost: ${:.2f}" .format(messages2*.05))
        else:
            print("    Included Message Used: " + str(messages) + ", Additional Messages Used: 0")
            print ("    Cost/Message: $0.05, Additional Message Cost: $0.00")

        print ("  Data Used (MB): " + str(data))
        if data > 5000:
            print("    Included Data Used (MB): 5000, Additional Data Used (MB): " + str(data2))
            print("    Cost/MB: $0.01, Additional Data Cost: ${:.2f}".format(data2*.01))
        else:
            print("    Included Data Used: " + str(data) + ", Additional Data Used: 0")
            print ("    Cost/MB: $0.01, Additional Data Cost: $0.00")

    #plan c, nothing special as everything is same cost
    else:   
        print("Your total monthly cost: $79.99")
        print("  Monthly Plan Cost: $79.99")
        print("    Minutes Used: " + str(minutes))
        print("    Message Used: " + str(messages))
        print("    Data Used (MB): " + str(data))



main()
