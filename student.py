student = []

class Student:
    def __init__(self, rollNo, name, marks):
        self.rollNo = rollNo
        self.name = name
        self.marks = marks
        self.calculate_grade()

    # Calculate grade
    def calculate_grade(self):
        if self.marks >= 90:
            self.grade = "A+"
        elif self.marks >= 80:
            self.grade = "A"
        elif self.marks >= 70:
            self.grade = "B"
        elif self.marks >= 60:
            self.grade = "C"
        elif self.marks >= 40:
            self.grade = "D"
        else:
            self.grade = "Fail"

    # Add student
    def add_student(self):
        # Check unique roll number
        for s in student:
            if s.rollNo == self.rollNo:
                print("Roll Number already exists!")
                return

        student.append(self)
        print("Student added successfully!")

    # Display one student
    def display(self):
        print("--------------------------------")
        print("Roll No :", self.rollNo)
        print("Name    :", self.name)
        print("Marks   :", self.marks)
        print("Grade   :", self.grade)
        print("--------------------------------")

    # View all students
    @staticmethod
    def view_student():
        if not student:
            print("No students found.")
            return

        for s in student:
            s.display()

    # Search by roll number
    @staticmethod
    def search_student(rollNo):
        for s in student:
            if s.rollNo == rollNo:
                s.display()
                return
        print("Student not found.")

    # Update marks
    @staticmethod
    def update_marks(rollNo, new_marks):
        if new_marks < 0 or new_marks > 100:
            print("Marks should be between 0 and 100.")
            return

        for s in student:
            if s.rollNo == rollNo:
                s.marks = new_marks
                s.calculate_grade()
                print("Marks updated successfully!")
                return

        print("Student not found.")

    # Delete student
    @staticmethod
    def delete_student(rollNo):
        for s in student:
            if s.rollNo == rollNo:
                student.remove(s)
                print("Student deleted successfully!")
                return

        print("Student not found.")

    # Display topper
    @staticmethod
    def display_topper():
        if not student:
            print("No students available.")
            return

        topper = max(student, key=lambda x: x.marks)
        print("\nTopper Details:")
        topper.display()