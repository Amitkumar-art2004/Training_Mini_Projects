cart = []   
categories = set()  
prices = {}
while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Calculate Total Bill")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        category = input("Enter item category: ")
        cart.append(item)
        prices[item] = price
        categories.add(category)
        print(item, "added to cart.")
    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            del prices[item]
            print(item, "removed from cart.")
        else:
            print("Item not found.")
    elif choice == 3:
        print("\nItems in Cart:", cart)
        print("Unique Categories:", categories)
        print("Item-Price Pairs:", prices)
    elif choice == 4:
        total = sum(prices.values())
        print("Total Bill = ₹", total)
    elif choice == 5:
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice!")
