def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Enter choice (1/2/3/4/5): ")
    
    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break
    
    if choice in ('1', '2', '3', '4'):
        a = input("Enter either int or float:")
        if a in ('int'):
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        elif a in ('float'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        else:
            print("Invalid input. Please enter either int or float.")
            num1,num2 =0,0
            
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input. Please try again.")