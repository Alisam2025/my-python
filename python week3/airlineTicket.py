# Collect passenger input
passenger_age = int(input("Enter your age: "))
flight_duration = int(input("Enter flight duration (in hours): "))
distance = int(input("Enter the flight distance (in miles): "))
checked_in_bags = int(input("Enter the number of bags to be checked in: "))
flying_class = input("Enter the flying class: ").strip().title()

# Define fare conditions
if passenger_age >= 18 and flight_duration >= 10 and distance >= 2000:
    if checked_in_bags == 3 and flying_class == "First Class":
        print("Your total airfare is $7000.")
    elif checked_in_bags == 2 and flying_class == "second class":

        print("Your total airfare is $5000.")
    else:
        print("Your total fare should be less than $5000.")
else:
    print("You do not qualify for this fare tier.")