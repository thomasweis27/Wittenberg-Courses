# the math lirary provides useful math functions in the code

import math # need this at the top of the file

someNumber = 10.24
newNumber = math.sqrt(someNumber)
print (newNumber)

#the floor function will round a decimal to the nearest integer
# ex) 9.8 rounds down to 9

newNumber = math.floor(someNumber)
print (newNumber)
print (math.floor(-4.5))

#ceiling function (ceil) you round up, oppisite of the floor function
print (math.ceil (9.1))
print (math.ceil (-11.34))
print (math.ceil (2.00))

#truncate (trunc) will just chop off the decimal of any number
print (math.trunc(3.56457658747456456))
print (math.trunc (-4.5))
print()

#euler's number (e = 2.718..., yeah that number)
# lib can calc  e^(some number) (for just the number e just use e^1)
print("e is approx equal to", math.exp(1))#e to the power of one
print (math.exp(-4.28)) #e^-4.28

# good for compounded interest rate
principal = 50000 #($)
interestRate = .02 #(2%)
numberOfYears = 10
amount  = principal*math.exp(interestRate*numberOfYears)
print()
print("The amount after 10 years is $", amount)
print ("We have gained $", amount-50000)
print()

# in to get pi print math.pi
print(math.pi)

#finding the radious of a circle
radius = int(input("what is the radius? "))
area = math.pi*radius**2
print (area)

#note about irrational numbers; best to use an approximation instead of going on forever

#exponentiation (pow) (standard rules of powers apply)
print (math.pow(4, 2))   # prints first number to the power of second (4^2)
print (math.pow(5, -0.5))

