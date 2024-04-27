#Recursion

"""
Dont do this:

def f():
    f()    <- the program will crash

"""

# The idea is to break a problem into smaller subproblems
#      until the small proble is small enough to solve.


"""
Problem: Add areas of squares with side lengths 1 through n.
Subproblem: add areas of squares of side length 1 to n - 1
    > Add from 1 to n - 2
Bass: Add areas of squares with side lengths 1 to 5
"""

def sumOfSquares(n):
    if n == 1:
        return 1
    else:
        totalSum = sumOfSquares(n-1) + n*n
        return totalSum


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
    print(sumOfSquares(5))
    print(fact(5))
    
main()

