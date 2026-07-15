from student import student as students,Student

while True:
    print("\n==============================")
    print("Student Management System")
    print("==============================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Display Topper")
    print("7. Exit")
    

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = int(input("Enter Roll Number: "))

        
        if any(s.rollNo == roll for s in students):
            print("Roll Number already exists!")
            continue

        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100.")
            continue

        s = Student(roll, name, marks)
        s.add_student()

    elif choice == 2:
        Student.view_student()

    elif choice == 3:
        roll = int(input("Enter Roll Number: "))
        Student.search_student(roll)

    elif choice == 4:
        roll = int(input("Enter Roll Number: "))
        marks = float(input("Enter New Marks: "))
        Student.update_marks(roll, marks)

    elif choice == 5:
        roll = int(input("Enter Roll Number: "))
        Student.delete_student(roll)

    elif choice == 6:
        Student.display_topper()

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
