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
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        display_inventory()
    elif choice == "2":
        category = input("Enter category (Sword, Shield, or Potion): ")
        display_category(category.capitalize())  # capitalize input for consistency
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")