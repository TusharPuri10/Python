course = 'Python for Beginners'
print(len(course)) # general purpose function, used in list also
print(course.upper()) #these functions are methods(oops)(specific to string object)
print(course) # strings are immutable
print(course.title())
print(course.lower())

print(course.find('P')) # 0 # case sensitive #find returns index
print(course.find('o')) # 4
print(course.find('O')) # -1 as O not exist
print(course.find('Beginners')) # 11
print(course.replace('Beginners','Absolute Beginners'))
print(course.replace('beginners','Absolute Beginners'))
print(course.replace('n','m'))
print('Python' in course) # boolean expression # in returns boolean value # True
print('python' in course) # False