# def insert_sorting(n):
#     for i in range(1,len(n)):
#         x, position = n[i], i-1
#         while(position >= 0 and x < n[position]):
#             n[position+1] = n[position]
#             position -= 1

#         n[position+1] = x




def insert_sort(n):
    for i in range(1,len(n)):
        x, position  = n[i],i-1
        while( position >=0 and x < n[position]):
            n[position+1] = n[position]
            position -=1

        n[position+1] = x


n = [9,8,6,4,3,2,1]
insert_sort(n)
print(n)
# print(n)
# b1 : i = 1 , x = 8 , position = 0 ,n[position] = 9
#  --> x < n[position]=9 va position >= 0
# n[1] = 9
# position = -1
# n[0] = 8

# n = [8,9,6,4,3,2,1]

# b2 : i = 2 , x = 6 , position = 1, n[position] = 9
# --> x < n[position] = 9 and position >= 0
# n[3] = 9 and position = 0
# --> i = 2, x = 6 < n[position] = 8 and position = 0 = 0
# n[2] = n[position] = 8 and position = -1









