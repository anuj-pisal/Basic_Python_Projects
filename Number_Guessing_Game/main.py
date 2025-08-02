import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

print("\n==== Number Guessing Game ====\n")
print("Guess A number in between 1 and 100")

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("\nYou guessed it right!")
    else:
        if(userGuess>randNumber):
            print("\nYou guessed it wrong! Enter a smaller number")
        else:
            print("\nYou guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
