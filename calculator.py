def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def display_menu():
    print("\n" + "="*30)
    print("      🧮 Simple Calculator")
    print("="*30)
    print("1️⃣  Add")
    print("2️⃣  Subtract")
    print("3️⃣  Multiply")
    print("4️⃣  Divide")
    print("5️⃣  Exit")

while True:
    display_menu()
    
    choice = input("\n🔹 Enter your choice (1/2/3/4/5): ")
    
    if choice == '5':
        print("📌 Exiting calculator. Thank you! 😊")
        break

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("\n🔢 Enter first number: "))
            num2 = float(input("🔢 Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numeric values.")
            continue

        print("\n📝 Result: ", end="")
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} × {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} ÷ {num2} = {divide(num1, num2)}")
    else:
        print("❌ Invalid choice! Please select a valid option.")

    input("\n🔄 Press Enter to continue...")
