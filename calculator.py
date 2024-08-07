# calculator 
print("----CALCULATOR----") 

print("Addition = 1") 
print("Subtraction = 2") 
print("Multiplication = 3") 
print("Division = 4") 

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

value = int(input("Choose a case to perform Operation : "))

def calculate(value , a , b):
    if value == 1:
        print(f"Answer according to case {value} is {a + b}")
    elif value == 2:
        print(f"Answer according to case {value} is {a - b}") 
    elif value == 3:
        print(f"Answer according to case {value} is {a * b}") 
    elif value == 4:
        if  b !=0:
         print(f"Answer according to case ",value,"is", a/b ) 
        else:
         print("Division by Zero not Possible")  
    else:
        print("Invalid case chosen")

calculate(value,a,b)

