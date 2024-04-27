# Name: Thomas Weis
# File: weis_lab8.py
# Date: 04/17/21
#
# Student Gpa Calculator
#
# I Received Help From: None Received
#
# I affirm that my work upholds the highest standards of honesty and
# academic integrity at Wittenberg and that I have neither given nor
# received unauthorized assistance.
#
# Thomas Weis


class Student:
    def __init__ (self , name , hours , qpoints):
        self.name =name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
        
    def getName(self):
        return self.name
    
    def getHours(self):
        return self.hours
    
    def getQPoints(self):
        return self.qpoints
    
    def gpa(self):
        return self.qpoints/self.hours

    def addGrade(self, gradePoint, credits):
        self.qpoints = (gradePoint * credits) + self.qpoints
        self.hours = self.hours + credits
        return self.qpoints, self.hours

    def addLetterGrade(self, gradeLetter, credits):
        if gradeLetter == "A+":
            g = 4.0
        elif gradeLetter == "A":
            g = 4.0
        elif gradeLetter == "A-":
            g = 3.7
        elif gradeLetter == "B+":
            g = 3.3
        elif gradeLetter == "B":
            g = 3.0
        elif gradeLetter == "B-":
            g = 2.7
        elif gradeLetter == "C+":
            g = 2.3
        elif gradeLetter == "C":
            g = 2.0
        elif gradeLetter == "C-":
            g = 1.7
        elif gradeLetter == "D+":
            g = 1.3
        elif gradeLetter == "D":
            g = 1.0
        else:
            g = 0.0


        self.qpoints = (g * credits) + self.qpoints
        self.hours = self.hours + credits
        return self.qpoints, self.hours
        


    

def main():
    print ("Student GPA Program")
    name = input("What is the Student's name? ")
    s1 = Student(name, 0, 0)
    while True:
        #start menu
        print("Select Option:")
        print("    1. Add Grade")
        print("    2. Add Letter Grade")
        print("    3. Current GPA")
        print("    4. Exit")
        selection = int(input("Choice: "))


        if selection == 1:
            x = float(input("What is your Grade Point? "))
            y = int(input("What is the # of Credits? "))
            s1.addGrade(x, y)
        elif selection == 2:
            x = input("What is your Grade Letter? ")
            y = int(input("What is the # of Credits? "))
            s1.addLetterGrade(x, y)
        elif selection == 3:
            print(s1.gpa())
        elif selection == 4:
            return False
        else:
            print("Not a valid option!")




    
main()
