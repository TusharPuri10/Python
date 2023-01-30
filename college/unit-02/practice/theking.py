'''s="However, Ram has been in the news for all the wrong reasons too. Illiterate bigots have weaponized the slogan Jai Shri Ram for wanton acts of violence, crime and hatred, which are anathema to what Ram actually stands for. These lumpen elements do not know that Ram is maryada purushottam, the epitome of rectitude, the touchstone of impeccable behaviour, the role model of the perfect human being, and the very incarnation of saumya rasa, harmonious equilibrium."
print(s.replace("Ram","Shree Ram"))'''

'''s="However, Ram has been in the news for all the wrong reasons too. Illiterate bigots have weaponized the slogan Jai Shri Ram for wanton acts of violence, crime and hatred, which are anathema to what Ram actually stands for. These lumpen elements do not know that Ram is maryada purushottam, the epitome of rectitude, the touchstone of impeccable behaviour, the role model of the perfect human being, and the very incarnation of saumya rasa, harmonious equilibrium."
l=s.split()
l.sort(reverse=True)
for i in range(0,len(l)):
    print(l[i],end=' ')'''

'''s="However, Ram has been in the news for all the wrong reasons too. Illiterate bigots have weaponized the slogan Jai Shri Ram for wanton acts of violence, crime and hatred, which are anathema to what Ram actually stands for. These lumpen elements do not know that Ram is maryada purushottam, the epitome of rectitude, the touchstone of impeccable behaviour, the role model of the perfect human being, and the very incarnation of saumya rasa, harmonious equilibrium."
l=s.split()
l1=l.sort()
if(l1==l):
    print("Sorted")
else:
    print("Not Sorted")'''

'''l=[1,3,565,756,"rem","jwm","kjfgbj",45,78]
s=0
for i in range(0,len(l)):
    if(type(l[i])==int):
        s=s+l[i]
print(s)'''

'''s=["Kamal","Komal","Kajal","Kishore","kumjata","King of Section-A","Tumshar Bhamiya"]
for i in range(0,len(s)):
    if s[i][0]=='K' or s[i][0]=='k':
        print(s[i])'''

'''s=str.maketrans("0123456789","₀₁₂₃₄₅₆₇₈₉")
print("H2O".translate(s))'''

# score=int(input("Enter the score"))
# match score:
#     case score if score>=90:
#         print("a")
#     case _:
#         print("f")

s="However, Ram has been in the news for all the wrong reasons too. Illiterate bigots have weaponized the slogan Jai Shri Ram for wanton acts of violence, crime and hatred, which are anathema to what Ram actually stands for. These lumpen elements do not know that Ram is maryada purushottam, the epitome of rectitude, the touchstone of impeccable behaviour, the role model of the perfect human being, and the very incarnation of saumya rasa, harmonious equilibrium."
l=s.split()
l1=[]
l.sort()
l1.
print(l)
print(l1)
if(l1==l):
    print("Sorted")
else:
    print("Not Sorted")