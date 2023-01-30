# s = "However, Ram has been in the news for all the wrong reasons too. Illiterate bigots have weaponized the slogan Jai Shri Ram for wanton acts of violence, crime and hatred, which are anathema to what Ram actually stands for. These lumpen elements do not know that Ram is maryada purushottam, the epitome of rectitude, the touchstone of impeccable behaviour, the role model of the perfect human being, and the very incarnation of saumya rasa, harmonious equilibrium."

# lst = s.split(" ")

# lst.sort(reverse=True)

# strng = ""
# for i in lst:
#     strng = strng + i + " "

# s3 = strng.rstrip()

# print(s3)

# s4 = str(lst)
# print(s4)
# print(s4[0])

# n = lst.count('Ram')
# print(n)

# # Q.5 Replace 'Ram' with 'Shree Ram' in above phrase

# s1=s.replace('Ram', 'Shree Ram')
# print(s1)

lst = [1,2,3,4,5,7,6]

# tmp = lst.sort()

# tmp = lst
# tmp.sort()

tmp = lst.copy()
tmp.sort()

if(lst == tmp):
    print("list is sorted")
else:
    print("Not sorted")