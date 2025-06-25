# # CRUD in python

# # C :-  Create

# # R :-  Read

# # U :-  Update

# # D :-  Delete

# # CRUD, which stands for Create, Read, Update, and Delete, is a set of fundamental operations performed on data in databases and other data storage systems. It's a core concept in software development, web applications, and database management. Essentially, CRUD operations allow users to manage data by adding new entries, retrieving existing ones, modifying them, and removing them when no longer needed. 

# # Examples

users = [
    {"id":1 , "name":"Alice" , "age":25},
    {"id":2 , "name":"elisha" , "age":30}
]

while True:
    print("CRUD Operation in Python!!!" )
    print("1. Create user" )
    print("2. Read user" )
    print("3. Update user" )
    print("4. Delete user" )
    print("5. Exit" )
    
    choice = input("Enter your choice(1-5) : ")

    if choice == "1":

        try:
            user_id = int(input("Enter id : "))
            name = input("Enter Name : ")
            age = int(input("Enter age : "))

            users.append({"id":user_id , "name":name , "age":age})

            print("User Succeccfully added!!")

        except:
            print("Invalid Input!!")

    elif choice == "2":

        if not users:
            print("No User found.")

        else:
            print("User List: ")
            for user in users:
                print(user)
    
    elif choice == "3":

        try: 

            user_id = int(input("Enter Update user id : "))

            found = False
            
            for user in users:
                
                if user["id"] == user_id:
                    
                    field = input("Enter your field to update (name/age): ").lower()

                    if field in user:

                        if field == "age":
                            user["age"] = int(input("Enter new age : "))

                        else:
                            user["name"] = input("Enter new name: ")

                        print("User update successfully!!!")
                    
                    else:
                        print("Invalid field!!")

                    found = True

                    break

                if not found:

                    print("User not found!!")
        
        except:
            print("Invalid input!!")

    elif choice == "4":

        try:

            user_id = int(input("Enter ID to Delete User : "))

            for user in users:

                new_users = []

                if user["id"] != user_id:

                    new_users.append(user)

                    users = new_users

                    print("user delete successfilly!!!")

        except:

            print("Invalid input!!!")

    elif choice == "5":

        print("Program exit successfully!!")

    else:

        print("Invalid choice, please Enter number of 1 to 5.")