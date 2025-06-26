students = []
subjects_set = set()

print("Welcome to the Student Data Organizer!")

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        
        student_id = input("Student ID: ")
        name = input("Name: ")
        age = int(input("Age: "))  
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ").split(",")
        
        
        student = {
            "id_dob": (student_id, dob),
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }
        students.append(student)  
        subjects_set.update(subjects)  
        print("Student added successfully!")

    elif choice == "2":
        
        if not students:
            print("No student records found.")
        else:
            print("\n--- All Student Records ---")
            for i in students:
                student_id, dob = i["id_dob"]
                name = i["name"]
                age = i["age"]
                grade = i["grade"]
                subjects = ', '.join(i["subjects"])
                print(f"Student ID: {student_id} | Name: {name} | Age: {age} | Grade: {grade} | DOB: {dob}")
                print(f"Subjects: {subjects}")
                
    elif choice == "3":
        
        student_id = input("Enter Student ID to update: ")
        found = False
        for i in students:
            if i["id_dob"][0] == student_id:
                found = True
                field = input("Enter field to update (age/subjects): ").lower()
                if field == "age":
                    i["age"] = int(input("Enter new age: "))
                    print("Age updated!")
                elif field == "subjects":
                    new_subjects = input("Enter new subjects (comma-separated): ").split(",")
                    i["subjects"] = [sub for sub in new_subjects]
                    subjects_set.update(i["subjects"])
                    print("Subjects updated!")
                else:
                    print("Invalid field.")
        if not found:
            print("Student ID not found!")

    elif choice == "4":
        
        student_id = input("Enter Student ID to delete: ")
        for i in range(len(students)):
            if students[i]["id_dob"][0] == student_id:
                del students[i]
                print("Student deleted!")
                break
        else:
            print("Student ID not found!")

    elif choice == "5":
        
        if subjects_set:
            print("Subjects Offered:", ", ".join(sorted(subjects_set)))
        else:
            print("No subjects recorded yet.")

    elif choice == "6":
        print("Thank you for visiting student data organizer.")
        break

    else:
        print("Invalid choice, please Try again.")