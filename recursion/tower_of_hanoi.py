def move(a,b):
    print('Move ',a,' to ', b)

# def tower_of_hanoi(n, x, y, z):
#     if n == 1 :
#         move(x,z)
#     else :
#         tower_of_hanoi(n-1, x, z, y)
#         move(x,z)
#         tower_of_hanoi(n-1, y, x, z)

# n = 3
# tower_of_hanoi(n,1,2,3)

# stack = [tower_of_hanoi(3,1,2,3)-->tower_of_hanoi(2,1,3,2)-->move(1,3)-->tower_of_hanoi(2,2,1,3)]
# khai trien
# tower_of_hanoi(2,1,3,2)=[tower_of_hanoi(1,1,2,3)-->move(1,2)-->tower_of_hanoi(1,3,1,2)]
# move(1,3)
# tower_of_hanoi(2,2,1,3)=[tower_of_hanoi(1,2,3,1)-->move(2,3)-->tower_of_hanoi(1,1,2,3)]




def move(a,b):
    print('move one dish from',a,'to',b)


def tower_of_hanoi(n,x,y,z):
    if n == 1 :
        move(x,z)
    else :
        tower_of_hanoi(n-1,x,z,y)
        move(x,z)
        tower_of_hanoi(n-1,y,z,x)


n=3

tower_of_hanoi(3,1,2,3)

