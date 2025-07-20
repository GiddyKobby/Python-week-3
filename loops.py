#for loops (repeat for each item)
#while loops (repeat while something is true)

#for loop with range()
Count from 1 to 5
for number in range(1, 6):
    print(number)


#Loop over a list
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print("I like", fruit)


#while loop
count = 0

while count < 5:
    print("Count is", count)
    count += 1

#try break (stop the loop)
while True:
    answer = input("Type 'exit' to stop: ")
    if answer == "exit":
        print("Bye!")
        break
    else:
        print("You typed:", answer)
