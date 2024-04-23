# get only one postion
def binary_search(array,x, low,high):
    # if high >= low :
    mid = (high + low )// 2
    
    if array[mid] == x :
        return mid
    elif array[mid] > x :
        return binary_search(array,x,low,mid-1)
    else :
        return binary_search(array,x,mid+1,high)
# can get many position with one value of x
def binary_search_array(array,x,low,high):
    position = [binary_search(array,x,low,high)]
    po = position[0] -1
    while po >= low :
        if array[po] == x :
            position.append(po)
        po -= 1
    po = position[0] + 1
    while po <= high :
        if array[po] == x :
            position.append(po)
        po += 1
    return position
array = [1,2,3,4,5,6,7]
x = 8
low = 0
high = len(array)-1
print(binary_search(array,8,low,high))
# print(binary_search_array(array,5,low,high))
