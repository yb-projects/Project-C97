# PRO C97 - Number Guessing Game
import random
import time

print("Hello! Welcome to the Number Guessing Game!")

name = input("Enter your name to get started: ")
number_range = input(name + ", enter the maximum number from which you want to guess: ")
number = random.randint(1, int(number_range))
chances = 0

print("") # This is for leaving a blank space, so that it will not be closely packed.

print(".... LOADING ....")
print("Please wait for five seconds, our server is loading.")
print("")
time.sleep(5) # This function waits for 5 seconds.

print("You have 5 chances.")

while chances < 5:
    guess = int(input("Guess a number between 1 to " + number_range + ": "))

    if (guess < number):
        print("Your guess was close. Guess a higher number!")
        print(chances, " chances are over.")
        print("")
    elif (guess > number):
        print("Your guess was close. Guess a lower number!")
        print(chances, " chances are over.")
        print("")
    elif (guess == number):
        print("Congratulations, " + name + "! You won the game. 🏆")
        break
    chances = chances + 1

if not chances < 5:
    print("I'm sorry! You lose. All 5 chances were over.")
    print("The actual number was:", number)
