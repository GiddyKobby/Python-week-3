#Make a list

fruits = ["apple", "banana", "mango"]

print(fruits)


#Access items

print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])


#Add an item

fruits.append("orange")
print("After adding:", fruits)


#Remove an item

fruits.remove("banana")
print("After removing:", fruits)


#Loop through

for fruit in fruits:
    print("I like", fruit)


#Check length

print("Number of fruits:", len(fruits))


# ✅ [] → make a list
# ✅ append() → add
# ✅ remove() → delete
# ✅ [index] → access
# ✅ for item in list → loop through
# ✅ len() → count items