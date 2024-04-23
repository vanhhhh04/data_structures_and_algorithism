# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]


# s = "hello"

# print("The original string is : ", end="")
# print(s)

# print("The reversed string(using recursion) is : ", end="")
# print(reverse(s))

# routes = [
#     ("Mumbai", "Paris"),
#     ("Mumbai", "Dubai"),
#     ("Paris", "New York"),
#     ("Paris", "New York"),
#     ("Dubai", "New York"),
#     ("New York", "Toronto")
# ]
# tup = []
# for i,j in routes :
#     # print(type(i))
#     tup.append(i)
# tup = tuple(tup)
# dicts1 = dict.fromkeys(tup)
# list1 = list(dicts1.keys())
# print(list1)
# print(routes)
# dicts = {}
# for k in range(0,len(list1)):
#     listn = []
#     for i,j in routes :
#         if i == list1[k]:
#             listn.append(j)

#     dicts[list1[k]] = listn

# print(dicts)


# def closure():
#     a = 'hello'
#     def inside():
#         nonlocal a
#         a = 'hello again'
#         print(a)
#     inside()
#     print(a)
# closure()
import math
kc = 5


def distance():
    print(kc)
distance()



# 10. Write a Python program that iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz".
# For numbers that are multiples of three and five, print "FizzBuzz".

for i in range(1,51):
    if i % 3 ==0 and i % 5 == 0 :
        print("fizzbuzz")
    elif i % 3 ==0 :
        print("fezz")
    elif i%5==0  :
        print("buzz")
    else :
        print(i)
def test(nums):
    # Check if the count of 19 in 'nums' is equal to 2 and the count of 5 is greater than or equal to 3
    a = nums.count('a')
    return a
nums = ['a']
print(test(nums))
# 4. We are making n stone piles! The first pile has n stones.
# If n is even, then all piles have an even number of stones.
# If n is odd, all piles have an odd number of stones.
# Each pile must more stones than the previous pile but as few as possible.
# Write a Python program to find the number of stones in each pile.
a = 5
j = 2
lst = []
for i in range(0,5):
    lst.append(a+i*2)
print(lst)









