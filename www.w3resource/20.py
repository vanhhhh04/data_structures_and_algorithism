# 20. Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.
# Input:
# [1, 2, 3, 4, 5, 6]
# Output:
# Increasing.
# Input:
# [6, 5, 4, 3, 2, 1]
# Output:
# Decreasing.
# Input:
# [19, 19, 5, 5, 5, 5, 5]
# Output:
# Not a monotonic sequence!
def check_sequence(a):
    if all(a[i] < a[i+1] for i in range(0,len(a)-1)):
        print("increasing sequence")
    elif all(a[i] > a[i+1] for i in range(0,len(a)-1)):
        print('decreasing')
    else :
        print('not a monotonic sequence !')

