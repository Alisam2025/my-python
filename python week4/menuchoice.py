choice = ""

while choice != "5":
    print("\nMenu:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. overdraft\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("Your balance is $1000.")
    elif choice == "2":
        print("Deposit successful.")
    elif choice == "3":
        print("Withdrawal successful.")
    elif choice == "4":
        print("Extra funds available for overdraft")
    elif choice == "5": 
        print("Exit")
    else:
        print("Invalid choice. Try again.")

# This code implements a simple ATM menu 
# using a while loop. The user can choose options 
# to check balance, deposit, withdraw, or exit the 
# program. The loop continues until the user chooses 
# to exit.


