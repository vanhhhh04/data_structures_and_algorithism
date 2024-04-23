# 28. Write a Python program to select a string from a given list of strings with the most unique characters.
# Define a function named 'test' that takes a list of strings 'strs' as input
def test(strs):
    # Use the max function to find the string with the most unique characters
    # The key argument specifies a lambda function that calculates the length of the set of characters in each string
    return max(strs, key=lambda x: len(set(x)))
a = ['abcd','aabbccddee']
print(test(a))