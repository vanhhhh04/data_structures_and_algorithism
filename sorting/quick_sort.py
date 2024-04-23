

def swap(a,b,arr):
    arr[a] , arr[b] = arr[b], arr[a]

def partition(elements,start,end):
    pivot_index = 0
    pivot = elements[pivot_index]

    while start < end :
        while start < len(elements) and elements[start] <= pivot :
            start += 1
        while elements[end] >= pivot :
            end -= 1
        if start < end :
            swap(start,end,elements)

    swap(pivot_index,end,elements)
    return end
def quicksort(elements,start,end):
    if start<end :
        qi = partition(elements,start,end)
        quicksort(elements,start,qi-1)
        quicksort(elements,qi+1,end)


elements = [11,9,29,7,15,28]
partition(elements,0,len(elements)-1)
quicksort(elements,0,len(elements)-1)
print(elements)