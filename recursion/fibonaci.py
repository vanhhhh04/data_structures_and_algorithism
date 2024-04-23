1,1,2,3,5,8,13
def fibonaci(n):
    if n == 1 or n == 2  :
        return 1
    else :
        return fibonaci(n-1) + fibonaci(n-2)

print(fibonaci(7))


1,1,2,3,5,8,13,21
def fibo(n):
    if n==1 or n==2 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

n = 8
print(fibo(n))


# Initialize variables 'x' and 'y' with values 0 and 1, respectively
x, y = 0, 1

# Execute the while loop until the value of 'y' becomes greater than or equal to 50
while y < 50:
    # Print the current value of 'y'
    print(y)

    # Update the values of 'x' and 'y' using simultaneous assignment,
    # where 'x' becomes the previous value of 'y' and 'y' becomes the sum of 'x' and the previous value of 'y'
    x, y = y, x + y



















