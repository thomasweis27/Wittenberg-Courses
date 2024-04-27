class Dog:
    def __init__(self, name, size, weight, color, age):
        self.name = name
        self.size = size
        self.weight = weight
        self.color = color
        self.age = age

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def setSize(self, newSize):
        self.size = newSize

    def getWeight(self):
        return self.weight

    def getColor(self):
        return self.weight

    def getAge(self):
        return self.age

    def setAge(self, newWeight):
        self.weight = NewWeight

    #things a dog can do

    def bark(self):
        print("{} says bark!".format(self.name))

    def eat(self, foodItem):
        print("{} ate {}!".format(self.name, foodItem))
        self.weight = self.weight + 1

    def sleep(self):
        self.weight = self.weight - 1

    def wagTail(self):
        print ("{} seems happy.".format(self.name))

    #'two string method'
    #retuns string that repersents an object
    def __str__(self):
        return "{}".format(self.name)



def main():
    dog1 = Dog("Mollie", "Small", 30, "Black and White", 2)

    dog1.eat("a banana")

    #only works bc of the 2 string method
    print(dog1)
    print(dog1.getWeight)
    dog1.sleep()
    print(dog1.getWeight)
    

main()

        
