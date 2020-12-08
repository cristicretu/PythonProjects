# min number of guesses = log2(Upper_bound - lower_bound + 1)
import random
import math

lower = int(input("Lower bound: "))
upper = int(input("Upper bound: "))

x = random.randint(lower, upper)
guessNr = math.log(upper - lower + 1, 2)

print(guessNr)

count = 0

while count < guessNr:
    count += 1
    
    guess = int(input("Guess: "))
    if x == guess:  
       print("Good job")
       break
    elif x > guess:
       print("Too low")
    elif x < guess:
       print("Too high")


if count >= guessNr:
    print("The number was "+ x + " good luck next time")