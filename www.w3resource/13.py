# 13. Write a Python program to find strings in a given list starting with a given prefix.
# Input:
# [( ca,('cat', 'car', 'fear', 'center'))]
# Output:
# ['cat', 'car']
# Input:
# [(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
# Output:
# ['dog', 'donut']
a = [( 'ca',('cat', 'car', 'fear', 'center'))]
a = [('do',('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
lst = []
for i in a :
    length = len(i[0])
    for k in i[1] :
        if k[:length] == i[0] :
            lst.append(k)
print(lst)
def test(strs, prefix):
    # Use a list comprehension to filter strings in 'strs' that start with the given 'prefix'
    return [s for s in strs if s.startswith(prefix)]
