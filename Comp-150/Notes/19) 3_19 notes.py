#Reading a file

#fname = open(path_to_file, "r")
                    #r for reading, w for writing, a for appending

#paths:
#   relative path (from here to there)
#   absolute path (hardrive all the way down to the file)

"""
. is the current directory
/ needed to move into new folder/file
.. to move back a directory
"""

bfile = open("./1) test.py", "r")
print (bfile.readline())
print (bfile.readline())
print (bfile.readline())
bfile.close()
#always close a file after using it!


#readline = one string
#readlines = a list of strings


afile = open("/Users/thoma/Desktop/Comp 150/Notes/1) test.py", "r")
print (afile.readline())
filecontents  = afile.read()
afile.close
print(filecontents)

#code that counts the number of periods in a file
"""
count = 0
for c in filecontents:
    if c ==".":
        count = count +1

file.close()

"""

testFile = open("!test.txt", "w")
#file is created: if it already exists it will be replaced!
#the folder it is being created in must exist though
testFile.write("Hello")
testFile.write("\n")
testFile.write("This is a test ")
testFile.write("from doc ")
testFile.write(str(1))
testFile.write("9") # number must be string before putting it in
testFile.close()




