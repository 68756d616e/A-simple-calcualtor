# A simple calculator

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

print("Welcome to A simple calculator")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

while True:
    choice = input("PLease choose options 1 - 4: ")
    
    if choice in ('1', '2', '3', '4'):       
        no1 = float(input("Please enter the first number: "))
        no2 = float(input("Please enter the second number: "))

        if choice == '1':
            print(no1, "+", no2, "=", add(no1, no2))        
        elif choice == '2':
            print(no1, "-", no2, '=', subtract(no1, no2))
        elif choice == '3':
            print(no1, "*", no2, '=', multiply(no1, no2))
        elif choice == '4':
            print(no1, "/", no2, '=', divide(no1, no2))

        calculate_again = input("Would you like to calculate again? yes or no?: ")
        if calculate_again == "no":
            break
    
    else:
        print("Incorrect input")
