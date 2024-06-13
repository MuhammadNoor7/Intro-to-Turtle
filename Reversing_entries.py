# Function to input student data
def input_student_data():
    students = []
    for i in range(10):
        print(f"Enter data for student {i + 1}:")
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        age = int(input("Age: "))
        degreeProgram = input("Degree Program: ")
        student = {
            "firstName": firstName,
            "lastName": lastName,
            "age": age,
            "degreeProgram": degreeProgram
        }
        students.append(student)
    return students


# Function to display student data in reverse order
def display_reverse(students):
    print("\nStudent data in reverse order:")
    for i in range(1, len(students) + 1):
        student = students[-i]
        print(f"Student {len(students) - i + 1}:")
        print(f"  First Name: {student['firstName']}")
        print(f"  Last Name: {student['lastName']}")
        print(f"  Age: {student['age']}")
        print(f"  Degree Program: {student['degreeProgram']}")



# Main program
students = input_student_data()
display_reverse(students)
