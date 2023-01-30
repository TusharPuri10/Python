# Working of open() function
'''
# Here file is a file object not a simple variabl
file = open(filename with path,mode)
'''
# 1. Manual approach to get the file path
path = 'C:\\Users\\hp\\OneDrive\\Desktop\\Workspace\\python_workspace\\unit-03\\abc.txt'
path = path + '/'

file=open(path + 'abc.txt','r')
for i in file:
    print(i)
    