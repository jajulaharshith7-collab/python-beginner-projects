students = []

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def show_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print()

def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")