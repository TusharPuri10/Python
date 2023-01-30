def add(a,b):
    '''This function adds two variables a and b
    and returns the sum of a and b
    '''
    return a+b

def sub(a,b):
    '''This function subtracts two variables a and b
    and returns the subtraction of a and b
    '''
    return a-b

print("Hello world 1")

def main():
    '''This function is testing all the functionalities
    '''
    if add(1,2) == 3:
        print("Add functionality is working fine")
    if sub(3,2) == 1:
        print("Sub functionality is working fine")

print(__name__)

if __name__ == "__main__":#__name__ == "main": check karta hai ki ham apni file ke andar hi hai na
    # print("Hello world 2")#__name__ variable store name of file in which code is written but if we are running the same file then it will return __main__ else it returns name of the file
    main()#import karne pe __name__ variable store name of file in which code is written, here M1_OtherFunctions and __main__ is string
    ''' is file ko jab koi import karege toh wo file ko objective function use karna hoga na ki functionality check karna'''

print("Hello world 3")