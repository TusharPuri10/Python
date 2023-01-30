is_boy = True
is_girl = False

if (is_boy == True and is_girl == True) or (is_boy == False and is_girl == False):
    print("Trans")
elif is_boy == True:
    print("boy")
else:
    print("girl")

if (is_boy and is_girl) or (not is_boy and not is_girl):
    print("Trans")
elif is_boy:
    print("boy")
else:
    print("girl")

# comparison operators are == > >= <= <