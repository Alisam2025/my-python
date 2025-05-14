pin = "1234"
attempts = 0

while attempts < 3:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == pin:
        print("Access granted.")
        break
    else:
        print("Incorrect PIN.")
        attempts += 1
else:
    print("Too many incorrect attempts. Card blocked.")