inventory = {
    "Sword": 5,
    "Shield": 3,
    "Potion": 10
}

def display_inventory():
    print("Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def display_category(category):
    if category in inventory:
        print(f"{category}s in Inventory: {inventory[category]}")
    else:
        print(f"No {category}s in the inventory.")


while True:
    print("\nMenu:")
    print("1. Display entire inventory")
    print("2. Display specific category")
    print("3. Add items to inventory")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        display_inventory()
    elif choice == "2":
        category = input("Enter category (Sword, Shield, Potion, or other): ")
        display_category(category.capitalize())
    elif choice == "3":
        new_category = input("Enter new category: ")
        new_quantity = int(input(f"Enter quantity of {new_category}: "))
        inventory[new_category.capitalize()] = new_quantity
        print(f"{new_quantity} {new_category}(s) added to inventory.")
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")