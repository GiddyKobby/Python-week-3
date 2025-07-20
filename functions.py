#Write a function,Give it input, Get output back, Call it multiple times

def say_hello():
    print("Hello, world!")

say_hello()
say_hello()
say_hello()

#function with input
def greet(name):
    print("Hello,", name)

greet("Gideon")
greet("Korbbby")

#Function that returns a result
def add_numbers(x, y):
    return x + y

result = add_numbers(5, 10)
print("5 + 10 =", result)

print("7 + 3 =", add_numbers(7, 3))


#Combine with input
def multiply(a, b):
    return a * b

x = int(input("First number: "))
y = int(input("Second number: "))

product = multiply(x, y)
print("The product is:", product)

