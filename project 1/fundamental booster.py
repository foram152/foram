def personal_data_collector():

    print("Welcome to the interactive personal data collecter!")
    print(" ")

    name = input("please enter your name: ")
    age = int(input("please enter your age: "))
    height = float(input("please enter your heght in meters: ")) 
    favNo = int(input("please enter your favourite number: "))
    print(" ")

    print("Thank you! hee is the information we collected: ")
    print(" ")

    print(f"Name:{name} (Type:{type(name)},memory address: {id(name)})")
    print(f"age:{age} (Type:{type(age)},memory address: {id(age)})")
    print(f"Name:{height} (Type:{type(height)},memory address: {id(height)})")
    print(f"Name:{favNo} (Type:{type(favNo)},memory address: {id(favNo)})")
    print(" ")

    birthYear = 2025 - age
    print(f"your birth year is approximately: {birthYear}(based on your age of {agef})")
    print(" ")

    print ("thank you for using the personal data collector. Goodbye!")

personal_data_collector()