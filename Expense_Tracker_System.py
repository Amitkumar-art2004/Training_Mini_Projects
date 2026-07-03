def add_expense():
    try:
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        with open("expense.txt", "a") as file:
            file.write(f"{category},{amount}\n")
        print("Expense Added")
    except ValueError:
        print("Invalid Amount")

def show_summary():
    data = {}
    try:
        with open("expense.txt", "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                if category in data:
                    data[category] += float(amount)
                else:
                    data[category] = float(amount)
        print("\nSummary")
        for key, value in data.items():
            print(key, ":", value)
    except FileNotFoundError:
        print("Expense file not found")

add_expense()
show_summary()
