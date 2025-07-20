#make a welcome function
def welcome():
    name = input("What is your name? ")
    print("Welcome,", name)

#make an add function
def add_numbers():
    x = int(input("First number: "))
    y = int(input("Second number: "))
    print("Their sum is:", x + y)

#make a loop function
def main():
    welcome()
    
    while True:
        print("\nWhat do you want to do?")
        print("1. Add two numbers")
        print("2. Exit")

        choice = input("Enter choice (1 or 2): ")

        if choice == "1":
            add_numbers()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()

