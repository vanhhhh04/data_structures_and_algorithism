def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp

def bubble_sort_by_key(array,key):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            a = array[j][key]
            b = array[j+1][key]
            if a > b :
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp



array = [1,4,7,9,5,6,3]
bubble_sort(array)
print(array)
# elements = [
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#     ]
# bubble_sort_by_key(elements,'transaction_amount')
# print(elements)
