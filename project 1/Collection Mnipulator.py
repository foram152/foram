print("Welcome to the student data organizer!\n")

students = {}


while True:

    print("Select an option: ")
    print("1. Add student ")
    print("2. Display all students ")
    print("3. Update student Information ")
    print("4. Delete Student ")
    print("5. Display Subjects offered ")
    print("6. Exit ")

    choice = int(input("Enter your choice : "))

    if choice == 1:

        try:
            
            print("\nEnter student details:")
            std_id = int(input("student ID : "))
            name = input("Name : ")
            age = int(input("age : "))
            grade = input("Grade : ")
            dob = input("Date of Birth (YYYY-MM-DD) : ")
            subjects = input("Subjects (comma-separated) : ").split(',')
            
            print("student added successfully!\n")

            students[std_id] = {
                "name": name,
                "age": age,
                "grade": grade,
                "dob": dob,
                "subjects": subjects
            }

        except:
            print("no students found\n")

    elif choice == 2:
        
        if len(students) == 0:
            print("No user found.")

        else:
            print("--- Display All Students ---\n")
            for student, info in students.items():
                print(f"Student ID : {std_id} | Name : {info['name']} | Age : {info['age']} | Grade : {info['grade']} | Date of Birth : {info['dob']} | Subjects : {', '.join(info['subjects'])}")

    elif choice == 3:
        std_id = int(input("Enter Student ID to update: "))

        if std_id in students:

            print("Enter new details:")

            name = input(f"Name [{name}]: ") 
            age_input = input(f"Age [{age}]: ")
            grade = input(f"Grade [{grade}]: ") 

            print(f"DOB remains unchanged: {dob}")

            subjects_input = input(f"Subjects (comma-separated) [{', '.join(subjects)}]: ")

            students[std_id] = (f"Student ID : {std_id} | Name : {info['name']} | Age : {info['age']} | Grade : {info['grade']} | Date of Birth : {info['dob']} | Subjects : {', '.join(info['subjects'])}")

            print("Student record updated successfully (DOB not changed).\n")
        else:
            print("Student not found.")
            