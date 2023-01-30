names = ['john','bob','tushar','mayank']
print(names[1])
print(names[-2])
# slicing is clear, see notion
print(names[2:])
print(names)

names[0] = 'John' # Mutable
print(names)

# Ex-1
# Find largest number in list
num = int(input('Enter the number of values you want to input'))
mylist = []
for i in range(num):
    # mylist[i] = int(input()) error
    mylist.append(int(input()))

max = mylist[0]
for i in mylist:
    if max<i:
        max=i

print('max is',max)

# two dimensional list in python
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1]) # 2
matrix[0][1] = 20
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item,end=' ')
    print('\n')

for row in matrix: #better
    print(*row)

# List Methods
numbers = [5,2,1,7,4]
numbers.append(13)
numbers.insert(1,77)
numbers.remove(2)
print(numbers)
numbers[1:3]=[0,0,0,0]
print(numbers)
numbers.remove(0)
print(numbers) 

numbers.pop()
print(numbers)

print(numbers.index(0))
# print(numbers.index(50)) generates error
print(50 in numbers)

print(numbers.count(0))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers1 = numbers
#numbers1 = numbers.copy()
numbers1.append(100)
print(numbers1)
numbers.clear()
print(numbers)