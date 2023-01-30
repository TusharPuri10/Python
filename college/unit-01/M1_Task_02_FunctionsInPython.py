# # M1_Task-02_FunctionsInPython.py

# def my_function(fname):
#     print(str(fname) + "reference")# , me space khud aata hai. + mai we have to include space automatically.

# my_function("happy")
# my_function("passwords")
# my_function(123)
# my_function(234)
# my_function(1.2)

# def my_function(fname,lname):
#     print(str(fname) + "  " + str(lname)) # int + string not possible therefore we must ensure that before adding anything to string it should be string
    
# my_function("happy","birthday")
# my_function("passwords","saved")
# my_function(123,456)
# my_function(234,"yolo")
# my_function(1.2,111)

# #arbitrary arguements, *args
# def my_function(*kids):
#     print(kids[2])# third element

# my_function("happy","birthday","to you")
# my_function("happy","anniversary","to you")
# #my_function("happy","birthday")# tuple index out of bound issue
# my_function("happy","yoga day","to you")

# #keyword arguments
# def my_function(child3, child2, child1):
#     print(child3 + " is youngest kid")

# my_function(child1 = "yogesh", child2 = "sujata", child3 = "nabbu")

# #default value of function parameter
# def my_function(country = "Norway"):
#     print("I am from " + country)

# my_function("sweden")
# my_function("brazil")
# my_function()
# my_function("india")

def my_function(food):
    print("food list:")
    for i in food:#for loop and here i is the element
        print(i)#food ke upar iterator object call karta hai and then pehla element uthata hai fir dusra

fruit = ["banana","apple",123,12.003]#list
my_function(fruit)

#Return values
def my_function(x):
    return 5*x

print(my_function(3))
print(my_function(5))
print(my_function(9.2))


# def mufunction():#used when you will write the code of this function in future but still you want to add the function
#     pass