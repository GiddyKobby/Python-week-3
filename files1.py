#write to a file

# Open file in write mode ("w")
file = open("notes.txt", "w")

file.write("Hello! This is my first line.\n")
file.write("And this is the second line.\n")

file.close()

print("File written successfully.")


#Read from a file

file = open("notes.txt", "r")

content = file.read()

file.close()

print("File content:")
print(content)


#Append to a file

file = open("notes.txt", "a")  # 'a' means append

file.write("Adding a third line!\n")

file.close()

print("Line appended.")


# ✅ open()
# ✅ Modes: "w" write, "r" read, "a" append
# ✅ read() vs write()
# ✅ How files let you save real user data