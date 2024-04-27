# Break
# the break statment is used to stop a loop

while True:
    print ("Run forever")
    break
    print ("this code is not printed")

x= 0
while True:
    print ("In loop", x)
    x=x+1
    if x == 4:
        break

#Continue
# goes back to the top of the loop and skips what is below

x =0
for num in range(11):
    if num%2==1:
        continue
    x =x+num
print (x) ##this is the sum of all the even numbers
