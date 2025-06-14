print ("Welcome to the bill Splliter")

dec = True
while dec:
    a = float(input("Enter total bill amount: "))
    print(" ")

    if a <= 0 :
        print("invalid amount , please enter right amount")
        continue

    b = int(input("Enter number of people: "))

    if b <= 0 : 
        print("invalid amount , please enter right amount")
        continue

    c = int(input("Enter tip percentage (0,5,10,15,20): ")) 

    if c <= 0 :
        print("invalid amount , please enter right amount")

    tip_amount = (c / 100 * a)*a 
    total_amount = a + b
    per_person = a / b

    print(f"tip amount: " , tip_amount)
    print(f"total bill(with tip): " , total_amount)
    print(f"Each person shoud pay: " , per_person)

    dec = False
    print(input("Whould you like to calculate another bill? (yes/no): "))
    print("...")




