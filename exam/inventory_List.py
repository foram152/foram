print("\nWelcome to Inventory List Analyzer!")

item = {}
category = []

doc = True
while doc:

    name = input("\nEnter item name: ")
    cat = input("Enter category: ").lower()
    quantity = int(input("Enter quantity: "))

    item[name] = quantity

    category.append(cat)
    print(category)
    print(item)

    choice = input("\nDo you want to add more items? (y/n) : ").lower()
   
    if choice == "n":
        print("\n========== INVENTORY SUMMARY ==========\n")

        print("Total Different Items:", len(item))
        print("Total Quantity in Stock:", sum(item.values()))

        average = sum(item.values()) / len(item)
        print("Average Quantity per Item:", average)


        most = max(item)
        least = min(item)

        print("Most Stocked Item:", most, "", item[most], "units")
        print("Least Stocked Item:", least, "", item[least], "units")

        print("\n-------------------------------------------------")

        sorted_cats = sorted(category)
        print(f"\nUnique Categories in Inventory : {set(category)}")

        print("\n-------------------------------------------------")

        print("\nItems Sorted by Quantity:")
        sorted_items = sorted(item.items(), key=lambda x: x[1], reverse=True)
        for item, qty in sorted_items:
            print(item, "-", qty, "units")

        print("\n-------------------------------------------------")

        print("\nCategories in Alphabetical Order :")
        sorted_cat = sorted(category, key=lambda x: x.lower())
        for c in sorted_cat:
            print(c)

        print("\n========== END OF REPORT ==========\n")
        break