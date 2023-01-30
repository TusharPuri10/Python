import math
# importing math module which contains bunch of reusable functions
# now math is an object like a string and we can use it's methods using dot operator
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
# augmented assignment operator += ...
# no ++ -- in python
x = 10
x = x + 3
x += 3
print(x)
#operator precedence basic maths concept
# paranthesis > exp > mul/div > add/sub
x = 10 + 3 * 2
print(x) # 16

x = 2.9
print(round(x)) # 3 
print(x) # 2.9

y = -1.8
print(abs(y)) # 1.8
print(y) # -1.8

print(math.ceil(2.4))
print(math.floor(2.4))
# https://docs.python.org/3/library/math.html all python functions in math module