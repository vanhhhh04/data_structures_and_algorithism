def factorials(n):
    if n == 1   :
        return 1
    else :
        return n * factorials(n-1)

n = 4
print(factorials(n))




