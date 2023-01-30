def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b

def modul(a,b):
    return a%b

def exp(a,b):
    return a**b

def floorDiv(a,b):
    return a//b

def main():
    if add(1,2)==3:
        print("Add functionality is working fine")
    if sub(1,2)==-1:
        print("subtraction functionality is working fine")
    if multi(1,2)==2:
        print("multiplication functionality is working fine")
    if div(1,2)==0.5:
        print("division functionality is working fine")
    if modul(1,2)==1:
        print("modulus functionality is working fine")
    if exp(1,2)==1:
        print("exponential functionality is working fine")
    if floorDiv(1,2)==0:
        print("floor division functionality is working fine")
if __name__ == "__main__":
    main()
print("Calculator Done")