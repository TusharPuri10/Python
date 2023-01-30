# Exception Handling
'''
# Exception, Error, Compilation Issues
1. Compilation Issues: ( programmar shi karta hai )
    - Syntax Issues, or Issues in the code
    catch by the python compiler
    pritn("kjskjfkd")
2. Exceptions: ( inki handling programmer kar sakta hai )
    - Issues in your code, catch by PVM [Python Virtual Machine]
    - Run time issues, Handle [PVM]
    a = 10
    b = 0
    print(a/b)
    - Handling  is possible by using try and except
    - Exception are always handled by the programmer
3. Errors:
    - Can not be handled by the programmer
    - Happen at run time
    - Even PVM can not catch them
    Memory full, Stack overflow, power failure etc.
    - System Design should be robust and efficient.
'''
try:
    # we have to write suspicious code in try block
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = a/b
    # file = open(path + "abc.txt",'w')
    # file.write('tushar is best')

except:
    # Handling of those exceptions
    print("b should not be zero")
    b = int(input("enter b: "))
    c = a/b
else:
    # if exception would not occur then execute this code
    print("Else block of code: ")
    print(c)

# finally:
    # this block of code will always run, if exception comes or not
    # f.close()
    # print("File is closed now")

# Rest of the code
print(c)