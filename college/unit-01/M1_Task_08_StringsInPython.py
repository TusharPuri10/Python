'George'
y = 10
# print(y + "dollar") this is giving error
print(str(y) + "Dollar")

'I \'m fine' # escape character  \' \ is a meta character works in code also used in regex
'press "Enter"'
'red' 'car'
print('red', 'car')
print('red', 'car',123)# space aaega
print('red'+'car'+ str(123))# + me space nhi aata
string="You're gay"
string[2::]
string[::2]
string[:4:]
string[-1:4:-1]
string[-4:-1]


#Repeating Strings
string='hello world'
print((string+'\n')*10)         #Prints hello world 10 times in new line

#finding length of string
s="Hey Tushar"
s=len(s)
print(s)

#Comparing Two Strings
s1='Hello'
s2='hello'
if s1==s2:
    print('Equals')
else:
    print('Not Equals')

if s1<=s2:
    print("s1 is smaller than or equal to s2")
else:
    print('s2 is smaller than s1')

s=' Sujata bijalwan '
print(s.rstrip())
print(s.lstrip())
print(s.strip())
print(s)

#Find a substring
str=input("Enter main string: ")
subStr=input("Enter Sub string: ")
n=str.find(subStr,0,len(str))
if n==-1:
    print('Substring not found')
else:
    print('Substring found at position',n)

#Strings are immutable in python
'''
    An immutable object is a object whose content can not be changed
    In python: strings, numbers and tuples are immutable
'''
s1='one'
s2='two'
s1=s2
print(s1)


#Replacing a Substring
str="your momma ugly asff"
s1="but she's a not milf"
s2="but heavy"
str1=str.replace(s1,s2)
print(str1)

#Split function
str="That is Beautiful"
str1=str.split(' ')

print(str1)
for i in str1:
    print(i)

# changing case of a string
str = "That is beautiful"
print(str.upper())

# Superscript and Subscript concept in Python
numbers_to_letters = str.maketrans("123", "ABC")
print("Question 1, point 2 and 4".translate(numbers_to_letters))

subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
print("C2H5OH".translate(subscript))

superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
print("PIr2".translate(superscript))

superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
print("PIr2".translate(superscript).replace('PI', 'π'))