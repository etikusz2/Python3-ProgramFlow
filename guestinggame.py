import random

highest = 10
answer = random.randint(1, highest)

print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("You got it first time")

while guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it!")
