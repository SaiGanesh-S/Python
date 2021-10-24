# Requirement
'''The first century spans from the year 1 up to and including the year 100, the second century
- from the year 101 up to and including the year 200, etc.'''

# sample TestCases
# 1705 - -> 18
# 1900 - -> 19
# 1601 - -> 17
# 2000 - -> 20

# user input
import math as m
user_input = 1601

# using math

print(m.ceil((user_input/100)), '-> Century')

# without using math
print((user_input + 99) // 100, '-> Century')
