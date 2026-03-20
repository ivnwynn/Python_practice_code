def calculator():
    num1=int(input("Enter your first number: "))
    num2=int(input("Enter your second number: "))

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        print(num1 + num2)
    elif choice == "2":
        print(num1 - num2)
    elif choice == "3":
        print(num1 * num2)
    elif choice == "4":
        print(num1 / num2)
    elif choice == "5":
        print("Exiting...")
    else: 
        print("Please try again")

calculator()

