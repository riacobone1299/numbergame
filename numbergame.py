import random

def randomizer():
    print("Welcome to the Number Game!")
    print("I'm thinking of a number between 1 and 1000.")

    number = random.randint(1, 1000)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number: 
                print("Too low. Try again.")
            elif guess > number:
                print("too high. Try again.")
            else: 
                print(f"Nice job! You got the right number after {attempts} attempts.")
                break
        except ValueError:
            print("We dont understand. Please enter a number instead.")
randomizer()
            