pin = int(input("Enter the ATM pin : "))
if pin == 1234:
    amount = int(input("Enter the amount : "))
    operation = input("Enter the operation (add, draw) : ")
    balance = 5000;
    if operation == "add":
        balance += amount;
        print("Deposit successful!")
    elif operation == "draw":
        if amount <= balance:
            balance -= amount;
            print("Withdraw successful!");
    print("Now your current balance is :",balance)
else:
    print("Invalid pin, chor!")
