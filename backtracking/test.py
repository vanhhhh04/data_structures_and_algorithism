from copy import copy
from copy import deepcopy

student_info = ("Linda", 18, ["Math", "Physics", "History"])

student_profile = deepcopy(student_info)

print(id(student_info))
print(id(student_profile))