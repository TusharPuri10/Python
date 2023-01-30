# List
'''
Data Structures: List
- Basic List Operations
    - Creating a list
    - Inserting
    - Replacing
    - Removing an element
    - Searching
    - Sorting a list
- Methods of list objects
- Nested list
- Using lists as stacks and queues
- How efficient lists are when used as stack or queue
'''

# 1. What is list in python?
"""
- List is a python's in-built data structure
- List are mutable in nature, can be changed
- List can store different types of elements whereas arary can
 store only single type of elements [int arr[3] = {1,2,3}; ]
- [], square brackets are used to create a list
"""

# 1.1 Empty List Example
listSample = []
print(listSample)


# 2. Create a list
participants = ['john','leila','amit','cate',123,123.4,'A']
print(participants)

print(participants[1])

print(participants[-1])

print(participants[-2])

# 3. Updating a list element
participants[3] = 'Maria'
print(participants)

# 4. Delete an element form the list
del participants[2]
# del participants[1:3]
print(participants)

print(participants[2])

# 5. Add new elements into a list
participants.append("akash")
participants.append("123")
participants.append(123)
participants.append('A')
participants.append(123.4)
print(participants)

# 6. Replace Values in a list using indexing
l = ['Hardik','rohit','rahul','virat','pant']
l[0] = 'akash'
print(l)

# 7. List Slicing
"""
list[index]
list[start,stop]
list[start,stop,step]
stop element would be executed fromm the end result
"""

participants = ['suresh','john','maria','amit','sumit','cat',123]

print(participants)

print(participants[1:3])

print(participants[:2])

print(participants[4:])

print(participants[-2:])

print(participants[-2::-1])

# 8. Find index of an element of the list
maria_index = participants.index("maria")
print(maria_index)

# ValueError: 'Maria123' is not in list
# index = participants.index("Maria123")
# print(index)

# 9. Search an element in a list
x  = [1,2,3,4,5]
print(2 in x)#True
print(7 not in x)#True

participants = ['suresh','john','maria','amit','sumit','cat']

x = [1,2,3,4,5]
b = 7

if( b in x):
    a = x.index(b)
    print(a)
else:
    print("Element not found in the list")

# 10. sort a list
participants.sort()
print(participants)

numbers = [2,3,4,5,1]
numbers.sort()
print(numbers)

numbers.sort(reverse = True)
print(numbers)

# 11. Creating a list using range function
lst = range(1,9,2)
for i in lst:
    print(i)

# print(lst[0])

# 12. Concat two lists
lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = lst1 + lst2
print(lst3)# it will create a list of combined elements


# 13. Nested list as matrics [Nested list]
participants = ['suresh','john','maria','amit','sumit','cat',123]
Newcomers = ['Joshua','Britany']
#print(Newcomers)

print("__bigger_list__")
Bigger_List = [participants,Newcomers]

print(Bigger_List)
print(Bigger_List[0])
print(Bigger_List[1])

print(Bigger_List[0][4])
print(Bigger_List[1][1])

# print(Bigger_List[1][3])
Number = [1,2,3,4,5]
print(max(Number))
print(min(Number))

# 15. Extra Methods of list Object
n = [1,2,3,4,5]
print(len(n))
n.append(6)
n.append(6)
print(n)

print(n.count(0))

# Element based
n.remove(6)
print(n)

# Index based
n.pop()
n.pop(0)

n.reverse()
print(n)

n.clear() # Delete all the elements and would leave an empty list at the end
print(n)

# 16. List comprehension
""" List comprehension represents creation of new lists
from an iterable object like range, set, tuple and so on"""

s = []
for i in range(1,9):
    s.append(i)

print(s)

lst = range(1,9,2)
for i in lst:
    print(i)

# yet to explore: set, tuple, dictionary -> list

# 17. Using list as Stacks
# stack using list
""" LIFO ORDER"""
stack = ["Amar","Akbar","Anthony"]
stack.append("ram")
stack.append("Iqbal")
print(stack)

# Remove the last item
print(stack.pop())
print(stack)

# Remove the last item
print(stack.pop())
print(stack)

# 18. Using list as queue
# Initializing a queue



# How efficient lists are when used as stck or queue
# as Stack
"""
- The biggest issue is that it can run into speed issues as it grows/
- The items in the list are stored next to each other in memory.
- If the stack grows bigger than the block of memory that currentlu holds
, then python needs to do some memory allocations. This can lead to some
append() calls taking much longer than other ones.
"""

# As queue
"""
- However, lists are quite slow for this purpose
because inserting or deleting an element at the beginning requires
- Shifting all of the other elements by one, requiring O(n) time.
"""
