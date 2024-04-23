# input
# a = [1,5,6,3,2,3,5] n = 7
# s = 10
# output
# return the numbers of index which we have to get in the array

def tinhtong(a,n,s):
    sort_descending(a)
    i = 0
    p = 0
    while (i < n and p < s):
        p += a[i]
        i += 1
    if p > s :
        return i
    else :
        return -1
def sort_descending(a):
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] < a[j] :
                a[i],a[j] = a[j],a[i]



a = [4, 5, 1, 3, 2]
n = len(a)
s = 10
print(tinhtong(a, n, s))

