#simple conditions
age = 17

if age >= 18:
    print("You are an adult.")
else:
    print("You are a child.")

#try with a user input
age = int(input("What is your age? "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a child.")

#adding elif (else if)
score = int(input("What is your score? "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

#combine conditions
number = int(input("Give me a number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")

