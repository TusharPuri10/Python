import math
def primeOrNot1(n):
    count = 0
    for i in range(2,n):# range(n) 1 - n-1  ,  range(2,n)  2 - n-1
        if n%i == 0:
            count = count + 1
    if count == 0:
        print("Prime Number")
    else:
        print("Not Prime Number")

def primeOrNot2(n):
    count = 0
    for i in range(2,int (n/2)):# range(n) 1 - n-1  ,  range(2,n)  2 - n-1
        if n%i == 0:
            count = count + 1
    if count == 0:
        print("Prime Number")
    else:
        print("Not Prime Number")

def primeOrNot3(n):
    count = 0
    y = int (math.sqrt(n))
    for i in range(2,y+1):# range(n) 1 - n-1  ,  range(2,n)  2 - n-1
        if n%i == 0:
            count = count + 1
    if count == 0:
        print("Prime Number")
    else:
        print("Not Prime Number")

def mysqrt(n):
    if n==1:
        return 1
    for i in range (int(n/2)):
        if(i*i > n):
            break
    return i-1

def primeOrNot4(n):
    count = 0
    y = int (mysqrt(n))
    for i in range(2,y+1):# range(n) 1 - n-1  ,  range(2,n)  2 - n-1
        if n%i == 0:
            count = count + 1
    if count == 0:
        print("Prime Number")
    else:
        print("Not Prime Number")

x = input("Enter the value of x: \n")
primeOrNot1(int(x))
primeOrNot2(int(x))
primeOrNot3(int(x))
primeOrNot4(int(x))
