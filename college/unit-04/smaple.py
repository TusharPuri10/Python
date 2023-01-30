# . and \ Regex
import re
txt = "Hey i am Tushar Puri, software engineer, iamtusharpuri@gmail.com 12x12x2022 12.12.2022 12122022"
result = re.search("@.", txt)
print(result.group())

result = re.search(".", txt)
print(result.group())

result = re.search("\.", txt)
print(result.group())

result = re.search("@.+", txt) # iamtusharpuri@" will give error for this
print(result.group())

result = re.search("@.*", txt)
print(result.group())

# result = re.search("@\d", txt)
# print(result.group())

result = re.search("@\d*", txt)
print(result.group()) # isme chal rha hai * means 0 or more , @ ke aage kuch nhi hoga toh bhi chal jaega

# result = re.search("@\d+", txt)
# print(result.group()) # isme nhi chal rha hai + means 1 or more

result = re.search("[0-9]{2}.[0-9]{2}.[0-9]{4}",txt)
print(result.group())

result = re.search("[0-9]{2}\.[0-9]{2}\.[0-9]{4}",txt)
print(result.group())

# extract particular words of a given string
result = re.split("\s",txt)[0]
print(result)

# extract all the words of a given string
print(re.split("\s",txt))
print(txt.split())

# split a stringg with multiple delimiters
print(re.split("\s|,|\,",txt))

# return all the words of a given string starts with vowel
result = re.findall("\\b[aeiouAEIOU]\S*",txt)
print(result)

result = re.findall("\\b[aeiouAEIOU]\S+",txt) # single ko chod dega
print(result)

txt = "k12"
print(re.findall("\d",txt))
print(re.findall("8\d",txt))
print(re.findall("9\D",txt))
print(re.findall("\A1",txt))
print(re.findall("[a-z]",txt))
print(re.findall("[^a-z]",txt))
print(re.findall("[0-9]",txt))
print(re.findall("[0-9]{2,4}",txt))
print(re.findall("[0-9]{2,5}",txt))
print(re.findall("k1",txt))
print(re.findall("k?1",txt)) # k optional hai
print(re.findall("a?",txt))
print(re.findall("k?",txt))
# print(re.findall("a?a",txt))
print(re.findall("k?.",txt)) # k optional hai

