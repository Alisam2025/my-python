import random

print("💘 Welcome to the Dating Match Calculator 💘")

# Start the loop
while True:
    # Input names
    your_name = input("Enter your name: ")
    crush_name = input("Enter your crush's name: ")

    # Generate random match percentage
    match_percent = random.randint(50, 100)  # Keep it optimistic 😄
    print(f"{your_name} ❤️ {crush_name} = {match_percent}% match!")

    # Ask user if they want to try again
    again = input("Do you want to try again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for using the Dating Match Calculator! 💕")
        break

