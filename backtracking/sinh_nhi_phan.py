


# https://o2.edu.vn/thuat-toan-sinh-cac-day-nhi-phan-co-do-dai-n/

def fine_print(x):
    tmp = ''
    for i in x:
        tmp += str(i)
    return tmp


def bin_gen(i):
    for j in range(0, 2):
        x[i] = j
        if i == n-1:
            print(fine_print(x))
        else:
            bin_gen(i+1)




n = 3
x = ['0','0','0']
# print(x)
# print_nc(x)
sinh_nc(0)





