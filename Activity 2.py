import random
import time

def intro():
    print("May I ask you for your name?")
    global name
    name = input()
    print(f"Well, {name}, we are going to play a game. I am thinking of a number between 1 and 100.")
    time.sleep(0.5)

def pick():
    number = random.randint(1, 100)
    guessTaken = 0
    if number % 2 == 0:
        print("Hint: The number is even.")
    else:
        print("Hint: The number is odd.")

    print("Go ahead. Guess!")

    while guessTaken < 6:
        time.sleep(0.25)
        guess_input = input("Guess: ")

        try:
            guess = int(guess_input)

            if 1 <= guess <= 100:
                guessTaken += 1

                if guess < number:
                    print("Too low.")
                elif guess > number:
                    print("Too high.")
                else:
                    break  
                time.sleep(0.5)
                print("Try Again!")

            else:
                print("That number isn't in the range! (1–100)")
                time.sleep(0.25)

        except ValueError:
            print(f"Oops! \"{guess_input}\" isn't a valid number.")

    if guess == number:
        print(f"Good job, {name}! You guessed the number in {guessTaken} tries!")
    else:
        print(f"Sorry, {name}. The number I was thinking of was {number}.")

playagain = "yes"
while playagain.lower() in ["yes", "y"]:
    intro()
    pick()
    print("Do you want to play again?")
    playagain = input()