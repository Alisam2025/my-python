secret_number = 7 # This is the number the useer has to guess
guess = 0 # Initial condition to enter the while loop

# While loop for guessing
while guess  != secret_number:
    guess = int(input("Guess the secret number (between 1 and 100): ")) # this code will run until the user guesses the correct number

    if guess < secret_number:
        print("Too low. Try again.")
    if guess > secret_number:
         print("Too high. Try again.")
    else:
        print("Congratulations! You guessed it right.")
#menu driven program'
#countdown Timer
#ATM verification
