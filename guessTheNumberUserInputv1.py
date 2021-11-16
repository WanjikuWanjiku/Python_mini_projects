#Guess the number game
#User input version
#The user inputs the range of the random numbers
#The computer generates a random number
#The user guesses the number

#import module random for python to generate random numbers
import random

#initialize guess to 0
guess = 0

#Take user input for the range of the random number
lower_limit = int(input("Enter the lower limit number: "))
upper_limit= int(input("Enter the upper limit number: "))

#Request another number if upper_limit is lower than lower_limit
if upper_limit < lower_limit:
    upper_limit= int(input(f"Enter a number higher than {lower_limit}:"))

#Assign random_number a random integer in the rangelower_limit to upper_limit
random_number = random.randint(lower_limit,upper_limit)

#Evaluate what to do when guess is not equal to the random number
#The initial guess value is 0 so it is not equal to a range for random_number
while guess != random_number:
    #Take user's guess
    guess = int(input(f"Enter a number between {lower_limit} and {upper_limit}: "))

    #Loop when guess is not correct
    if guess < random_number:
        print("Sorry, your guess is too low. Try again!")
    elif guess > random_number:
        print("Sorry, your guess is too high. Try again!")

#Print when guess is correct
print(f"Hooray! Your guess, {guess}, is correct. Great job!")
