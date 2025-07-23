#Start with a list

students = []

#Make an add function

def add_student():
    name = input("Name: ")
    student_id = input("ID: ")
    grade = input("Grade: ")

    student = {
        "name": name,
        "id": student_id,
        "grade": grade
    }

    students.append(student)
    print("Student added!")


#Save to file

def save_students():
    file = open("students.txt", "w")
    for s in students:
        line = f"{s['name']},{s['id']},{s['grade']}\n"
        file.write(line)
    file.close()
    print("Students saved to file.")


#Load from file

def load_students():
    try:
        file = open("students.txt", "r")
        for line in file:
            name, student_id, grade = line.strip().split(",")
            student = {
                "name": name,
                "id": student_id,
                "grade": grade
            }
            students.append(student)
        file.close()
        print("Students loaded.")
    except FileNotFoundError:
        print("No file found. Starting fresh.")


# List students

def list_students():
    for s in students:
        print(f"Name: {s['name']}, ID: {s['id']}, Grade: {s['grade']}")


#Add Update

def update_student():
    student_id = input("Enter ID of student to update: ")

    for s in students:
        if s["id"] == student_id:
            print(f"Found: {s['name']} with grade {s['grade']}")
            new_grade = input("Enter new grade: ")
            s["grade"] = new_grade
            print("Grade updated!")
            return

    print("Student not found.")


#Add Delete

def delete_student():
    student_id = input("Enter ID of student to delete: ")

    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            print("Student deleted!")
            return

    print("Student not found.")


#Main loop

def main():
    load_students()

    while True:
        print("\n1. Add student")
        print("2. List students")
        print("3. Save")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            save_students()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()    
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

main()


# ✅ Combine lists + dicts → to store structured data.
# ✅ Read/Write to a file → simulate a database.
# ✅ CRUD → Add, Read, Update (change grade?), Delete (optional — try it!)

# This is real CRUD:

# Create → add_student()

# Read → list_students()

# Update → update_student()

# Delete → delete_student()

# Save → save_students() keeps your file up to date.

# 🔑 CRUD is just about finding the right item → change it or remove it.

# ✅ Loops + conditions = control the flow.

# ✅ remove() deletes from list.

# ✅ Changing dict values updates the info.