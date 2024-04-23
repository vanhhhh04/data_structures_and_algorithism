# cac phan tu trong mang phai duoc sap xep
# O(logn)

def binary(left,right,n,x):
    if left > right :
        return False
    position = int((left + right) // 2)
    if n[position] == x :
        return position
    elif n[position] < x :
        return binary(position+1,right,n,x)
    elif n[position] > x :
        return binary(left,position-1,n,x)

def binary1(left,right,n,x):
    while left <= right:
        position = (left + right) // 2
        if n[position] == x :
            return position
        elif n[position] < x :
            left = position + 1
        else :
            right= position - 1
    # if left > right :







n = [1,2,3,4,5,6,7,8]
x = 3
left = 0
right = len(n) -1
# print(binary(left,right,n,x))
print(binary_seach1(left,right,n,x))

