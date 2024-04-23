# Write a Python program to find the indices at which the numbers in the list drop.
# NOTE: You can detect multiple drops just by checking if nums[i] < nums[i-1]
# Input:
# [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
# Output:
# [1, 4, 6, 8, 10, 11, 15, 16, 18]
# Input:
# [6, 5, 4, 3, 2, 1]
# Output:
# [1, 2, 3, 4, 5]
# Input:
# [1, 19, 5, 15, 5, 25, 5]
# Output:
# [0, 2, 4, 6]
def check_indices(lst):
    tmp = []
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            tmp.append(i+1)
    return tmp
lst = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
print(check_indices(lst))