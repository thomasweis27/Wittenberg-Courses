#calculate factorial without a loop

def fact(n):
    x = 1
    if n != 0:
        x = fact(n-1)

    else:
        n=1
        
    n = n*x

    return n



def main():
    x = fact(0)
    print (x)

main()

