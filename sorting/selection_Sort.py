def selection_sort(l):
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]

l = [4,12,4,6,2,3]
selection_sort(l)
print(l)
