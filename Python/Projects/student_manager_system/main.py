from student import Student

def menu():
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

students = []

while True:
    menu()
    choice = input("Enter choice: ")

    try:
        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            students.append(Student(name, age))
            print("Student added!")

        elif choice == "2":
            for s in students:
                print(s)

        elif choice == "3":
            name = input("Enter name to delete: ")
            students = [s for s in students if s.name != name]
            print("Deleted!")

        elif choice == "4":
            break

        else:
            print("Invalid choice")

    except Exception as e:
        print("Error:", e)
