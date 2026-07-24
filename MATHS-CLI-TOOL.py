print("----CLI TOOL----")
def factorial(n):
    '''takes in your number n and calculates the total number of ways you can arrange them in specific group of items'''
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci(n):
    '''The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
       return fibonacci(n - 1) + fibonacci(n - 2)   
    
def square(n):
    '''take in a number n and returns the square of n'''  
    return n**2  

def countdown(n):
    '''Recursively counts down from n to 0 and prints a blast-off message'''
    if n<= 0:
        print("blast off!!")
        return
    else:
        print(f"{n}")
        countdown(n-1)    

print("_" * 40)        
print("_" * 40)
print()

print("           MATHS CLI TOOL")
print("_" * 40)
print("_" * 40)

while True:
    print("\n select your option")
    print("1) factorial")
    print("2) fibonacci")
    print("3) square")
    print("4) countdown")
    print("5) exit")

    choice = int(input("enter your option: "))

    if choice == 1:
        print(f"INFO: {factorial.__doc__}")
        n = int(input("enter your choice of number: "))
        print(f"result = {factorial(n)}")
    
    elif choice == 2:
        print(f"INFO: {fibonacci.__doc__}")
        num = int(input("enter your choice of num: "))
        print(f"result = {fibonacci(num)}")

    elif choice == 3:
        print(f"INFO: {square.__doc__}")
        num = int(input("enter number: "))
        result = (f"{square(num)}")

    elif choice == 4:
        print(f"INFO: {countdown.__doc__}")
        num = int(input("enter number: "))
        result = (f"{countdown(num)}")

    elif choice == 5:
        print("GOODBYE!")
        exit
    else:
        print("ivalid! enter a int")    
       
