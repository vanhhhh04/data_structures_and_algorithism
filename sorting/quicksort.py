# def partition(left,right,n):
#     i = left - 1
#     pivot = n[right]
#     for j in range(left,right):
#         if n[j] <= pivot :
#             i += 1
#             n[i] , n[j] = n[j],n[i]

#     i += 1
#     n[i], n[right] = n[right],n[i]
#     return i

# def quick_sort(left,right,n):
#     if left >= right :
#         return 0
#     else :
#         p = partition(left,right,n)
#         quick_sort(left, p-1,n)
#         quick_sort(p+1, right, n)


def partition(left,right,n):
    pivot = n[right]
    i = left - 1
    for j in range(left,right):
        if n[j] <= pivot :
            i += 1
            n[i], n[j] = n[j], n[i]

    i += 1
    n[right],n[i] = n[i],n[right]
    return i

def quick_sort(left,right,n):
    if left < right :
        p = partition(left,right,n)
        quick_sort(left,p-1,n)
        quick_sort(p+1,right,n)


n = [2,8,7,1,5,3,6,4]
left = 0
right = len(n)-1
quick_sort(left,right,n)
print(n)
