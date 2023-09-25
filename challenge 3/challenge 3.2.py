class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"{self.name} (Roll No: {self.roll_number}, CGPA: {self.cgpa})"

def sort_students(student_list):
    # Sort the list of students based on their CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
students = [
    Student("Alice", "A001", 3.8),
    Student("Bob", "B002", 3.6),
    Student("Charlie", "C003", 3.9),
    Student("David", "D004", 3.7),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(student)
