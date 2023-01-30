# note
'''
- A RegEx or Regular expression, is a sequence of characters that forms a search pattern.
- RegEx can be used to check if a string contains the specified search pattern.
- Python has a built-in package called "re", which can be used to work with regular expressions
'''

txt = "The rain in Spain"
x = txt.find("ai") #This is not a RegEx function but a string function
print(x)

x = txt.find("ai",7)
print(x)

#import the re module
import re

txt = "The rain in spain"
x = re.findall("ai",txt)# find all returns all the instances of the sub.
print(x)

x = re.findall("portugal",txt)
print(x)

# search for the first white space character or even a word in the string
txt = "The rain in spain, The rain in spain"
x = re.search("\s",txt)# \s denotes space
y = re.search("rain",txt)
print(x)
print(y)

print(y.span()) # y is now an object
print(y.group())
print(y.start())
print(y.end())

# split a statement, based on a single space
txt = "The rain in spain"
x = re.split("\s",txt) # this will return a list of words
print(x)

# control the number of occurrences by specifying the maxsplit part
txt = "The rain in spain"
x = re.split("\s",txt,2)
print(x)

# The split function replaces the matches with the text of your choice
txt = "The rain in spain"
x = re.sub("\s","_",txt)
print(x)

# control the number of replacements by specifying the count parameter
txt = "The rain in spain"
x = re.sub("\s","_",txt,2)
print(x)

# match object in regex
txt = "The rain in spain"
x = re.search("ai",txt) # this will return an object matched
print(x)
print(type(x))
print(x.start())    # will search from the start
print(x.span())     # return the span of the word/character
print(x.end())      # will search from the end
print(x.group())    # actual word/set. from the result

# Match object
'''
- A match object is an object containing information about the
    search and the result
- If there is no match, the value None will be returned
    instead of the match object.
'''

#Q1. Find username/host or domain name from the text provided

# 1. First approach (String function):
data = 'From akash.chauhan@gmail.com 12-12-2022 09:14:16'

sloc = data.find("@")
print(sloc)

eloc = data.find(" ",sloc)

print(data[sloc+1:eloc+1])

print(re.search("@.*",data).group().split()[0])

# Extract date from string
txt = "I have my report to the department on 12-12-2022, 12122022"
x = re.search("([0-9]{2}\-[0-9]{2}\-[0-9]{4})",txt)
print(x.group())

# return all the words of a string that starts with vowel
txt = "I have submitted my report to the department on 12-12-2022"

print(re.findall("\\b[aeiouAEIOU]\S*", txt))

print(re.split("\s|,|\.", txt))