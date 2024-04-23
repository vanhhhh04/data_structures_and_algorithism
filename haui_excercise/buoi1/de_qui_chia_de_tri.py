# Bài 1: Tìm số fibonaci
# Yêu cầu:
# - Viết định nghĩa đệ quy tìm số fibonaci thứ n (n ≥ 1) trong dãy số fibonaci
# - Thiết kế giải thuật đệ quy theo định nghĩa trên.
# - Cài đặt chương trình ứng dụng thực hiện:
# o Tìm và hiển thị số fibonaci thứ n.
# o Tìm và hiển thị dãy n số fibonaci.
# 1 1 2 3 5 8 13 21
def fibonaci(a):
    if a == 0 or a == 1 :
        return 1
    elif a <0 :
        return 0
    else :
        return fibonaci(a-1) + fibonaci(a-2)
a = 4
lst = [fibonaci(i) for i in range(0,a)]
# print(lst)
def fibonacii(a):
    x,y = 1,1
    for i in range(1,a-1):
        x,y = y,x+y
    return y
# print(fibonacii(4))

# Bài 2: Tháp Hà Nội
# Yêu cầu:
# - Mô tả quá trình chuyển đĩa với số lượng đĩa n = 3.
# - Thiết kế giải thuật đệ quy giải quyết bài toán.
# - Cài đặt chương trình ứng dụng.
# - Đưa ra nhận xét khi số lượng đĩa tăng lên.
def move(a,c):
    print("move one dish from ",a," to ", c)
def tower_of_hanoi(n,a,b,c):
    if n == 1 :
        print("move one dish from ",a,' to ',c)
    else :
        tower_of_hanoi(n-1,a,c,b)
        move(a,c)
        tower_of_hanoi(n-1,b,a,c)
n =3
a = "a"
b = "b"
c = "c"
# tower_of_hanoi(n,a,b,c)

# Bài 3: Tìm ước số chung lớn nhất
# Yêu cầu:
# - Viết định nghĩa đệ quy tìm ước số chung lớn nhất theo thuật toán Euclid.
# - Thiết kế giải thuật đệ quy theo định nghĩa trên.
# - Cài đặt chương trình ứng dụng giải thuật
def ucln(a, b):
    if a >= b :
        if a % b == 0 :
            return b
        else :
            return ucln(b,a%b)
    else :
        if b % a == 0 :
            return a
        else :
            return ucln(a,b%a)

# Bài 4: Tìm giá trị lớn nhất
# Yêu cầu:
# - Mô tả quá trình tìm giá trị lớn nhất trên dãy số theo chiến lược chia để trị.
# - Thiết kế giải thuật tìm giá trị lớn nhất trên dãy số theo chiến lược chia để trị.
# - Cài đặt chương trình ứng dụng.
def max_value(a, left, right):
    if left == right:
        return a[left]
    else:
        mid = (left + right) // 2  # Use integer division to get the midpoint
        max_left = max_value(a, left, mid)
        max_right = max_value(a, mid + 1, right)

        return max(max_left, max_right)

a = [4,6,3,2,3,5,7,8,9,3,1]
print(max_value(a,0,len(a)-1))

# Bài 5: Tính a^n
# - Mô tả cách tính 2^9
# theo chiến lược chia để trị.
# - Thiết kế giải thuật tính an
# theo chiến lược chia để trị.
# - Cài đặt chương trình ứng dụng.
d = 0
def power(a,n):
    global d
    if n == 1 :
        return a
    elif n % 2 == 0 :
        x = power(a, n//2)
        d += 1
        return x * x
    else :
        x = power(a, (n-1)//2)
        d += 2
        return x * x *a

a = 2
n = 4

# print(power(2,9))
# print(d)

# Bài 6: Đếm số trong dãy
# - Mô tả cách đếm số lần xuất hiện của một số x trong dãy a có n số theo chiến
# lược chia để trị.
# - Viết định nghĩa đệ quy theo mô tả trên.
# - Thiết kế giải thuật đếm theo chiến lược chia để trị.
# - Cài đặt chương trình ứng dụng
# bài toán đếm số chữ số của 1 số vd 123 (3 chữ số)
def dem_chu_so(a):
    if a < 10 :
        return 1
    else :
        return 1 + dem_chu_so(a//10)
# print(dem_chu_so(4568))

# Bài 2: In ngược xâu ký tự
def in_nguoc(a):
    if len(a) == 0 :
        return
    else :
        print(a[-1],end='')
        in_nguoc(a[:-1])
# a = "hello"
# in_nguoc(a)


# Bài 3: Tìm từ trong từ điển (các từ trong từ điển sắp xếp theo thứ tự bảng chữ cái).
# - Mô tả cách tìm theo chiến lược chia để trị.
# - Thiết kế giải thuật tìm kiếm.
# - Cài đặt chương trình ứng dụng
dictionary = ["apple", "banana", "cherry", "grape", "orange", "pear"]
word_to_find = "cherry"
# found = binary_search(sorted(dictionary), word_to_find)

def search_words(a,word,left,right):
    if left > right :
        return False
    else :
        middle = (left+right)//2
        if a[middle] == word :
            return middle
        elif a[middle] > word :
            return search_words(a,word,left,middle-1)
        elif a[middle] < word :
            return search_words(a,word,middle+1,right)
dictionary = ["apple", "banana", "cherry", "grape", "orange", "pear"]
word_to_find = "cherry"
found = search_words(sorted(dictionary), word_to_find,0,len(dictionary))
print(found)

# Bài 4: Tính tổng
# - Tìm cách tính tổng của một dãy có n số theo chiến lược chia để trị.
# - Định nghĩa cách tính, thiết kế giải thuật và cài đặt ứng dụng.
def sum_dive(a):
    if len(a) == 1 :
        return a[0]
    else :
        middle = len(a) // 2
        left_sum = sum_dive(a[middle:])
        right_sum = sum_dive(a[:middle])
        return left_sum + right_sum
a=[1,2,3,4,5]
print(sum_dive(a))

# Bài 5: Sắp xếp dãy số
# - Tìm cách sắp xếp một dãy số theo chiều tăng dần bằng chiến lược chia để
# trị.
# - Thiết kế giải thuật và cài đặt giải thuật
a = [3,5,6,2,12,8]
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else :
        middle = len(arr)//2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left,right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Copy các phần tử còn lại của left và right vào result
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Ví dụ sử dụng chương trình
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Dãy số sau khi sắp xếp:", sorted_arr)
