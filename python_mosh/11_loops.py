i = 1
while i<=5:
    print('*' * i)
    i+=1

# for loop are used to iterate items of a collection such as string list tuple etc.
for item in 'Python':
    print(item)

for item in ['tushar','vishwas','mayank']:
    print(item)

for item in range(10):# 0-9
    print(item)

print('')
for item in range(5,10):# 5-9
    print(item)

print('')
for item in range(2,10,2):# 2 4 6 8
    print(item)

# Nested loops
for x in range(4):#0-3
    for y in range (3):#0-2
        print(f'{x} - {y}')#formatted string

# challenge
mylist = [5,2,5,2,2,2]
# for i in range(len(mylist)):
#         print('@'*mylist[i])
for i in mylist:
    print('@'*i)