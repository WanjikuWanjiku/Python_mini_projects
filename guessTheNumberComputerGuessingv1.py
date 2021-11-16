555
#Guess the number game
#Computer input version
#Initialize range of random numbers
#The user inputs a random number
#The computer guesses the number

#import random module
import random

#Define the range of random numbers
guess = random.randint(0,1000)

#Initialize number of attempts
#This will check how many attempts the computer makes to guess the random_number
attempts = 0

#Initialize random_number with the user's random number
random_number = int(input("Enter a random number between 0 and 1000: "))
#Check if user has entered a number within the range
while random_number < 0 or random_number>1000:
    random_number=int(input("Invalid Entry! Enter a number between 0 and 1000: "))

#What to do when guess is not correct
while guess != random_number:
    if guess < random_number:
        print("Too low. Try Again!")
        guess=random.randint((guess + 1),1000) #The computer guesses again with previous guess + 1 as lower limit
        attempts += 1
    elif guess > random_number:
        print("Too high. Try Again!")
        guess=random.randint(0,(guess-1))    #The computer guesses again with previous guess - 1 as upper limit
        attempts += 1

attempts += 1
#Print when the computer gets the guess right.
print(f"The computer guess, {guess}, is Correct after {attempts} attempts!")


