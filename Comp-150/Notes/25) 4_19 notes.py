#tells if the string s is a palendrome with recursion

def pal(s):
    if len(s)<= 1:
        print("Is a palendrome")

    else:
        if s[0] == s[len(s)-1]:
            pal(s[1:len(s)-1])

        else:
            print("Not a palendrome")




s = "racecar"
pal(s)
