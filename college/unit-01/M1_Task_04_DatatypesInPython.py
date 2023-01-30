# Declaration of a variable is not requires in python
#M1_Task-01_VariablesInPython

'''
Declaration of a variable is not requires in python
Declaration of a variable is not requires in python
Declaration of a variable is not requires in python
'''

x = 5
y = "John"
print(x) 
print(y) 

# casting of a value
x = str(123)
y = int (3)
z = float (3)
print(x) 
print(y)
print(z)
# python string/character storage
# single quotee doublt quote

x = "john"
x = 'john'
x = 'b'
x = "b"
x = """Akash"""#doc string
x = 'Akash'

print(x)

# type of variable

'''
data types:
1 - Numeric:
        int 
        float
2 - Binary, Octal and Hexadecimal+
        n1 = 0b0101010 [0B for Binary{0,1}]
        n2 = 0o17      [0O for octal{0,1,2,3,4,5,6,7}]
        n3 = 0x12      [0X for Hexadecimal{0 - 9 , A,B,C,D,E,F}]
3 - Bool data type:
        a = 10
        b = 20
        if(a<b): print("Hello")
'''

n1 = 0B0101010
n2 = 0O17
n3 = 0X1c2

print(int(n1))
print(int(n2))
print(int(n3))

print(int('0101010',2))
print(int('17',8))
print(int('1c2',16))

# Bool data type
a = 10
b = 20
if(a<b): print("hello")
else: print("nope")