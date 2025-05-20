balance = 1000.0
overdraft_limit = 200.0
choice = ""

while choice != "5":
    print("\nMenu:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Overdraft Info\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Your balance is ${balance:.2f}.")
    
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposit successful. New balance: ${balance:.2f}")
        else:
            print("Invalid deposit amount.")
    
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0:
            if amount <= balance + overdraft_limit:
                balance -= amount
                print(f"Withdrawal successful. New balance: ${balance:.2f}")
            else:
                print("Insufficient funds, including overdraft.")
        else:
            print("Invalid withdrawal amount.")
    
    elif choice == "4":
        print(f"Overdraft available: ${overdraft_limit:.2f}")
    
    elif choice == "5": 
        print("Exiting program.")
    
    else:
        print("Invalid choice. Try again.")
