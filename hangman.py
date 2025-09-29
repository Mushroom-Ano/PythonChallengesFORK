import random
livesCounter = 10
wordbank = [
    "python", "variable", "function", "object", "compile",
    "hangman", "wizard", "jungle", "puzzle", "rocket",
    "galaxy", "nebula", "planet", "asteroid", "comet",
    "castle", "sword", "dragon", "knight", "quest",
    "forest", "ocean", "desert", "island", "mountain",
    "banana", "guitar", "piano", "violin", "trumpet",
    "zebra", "penguin", "giraffe", "dolphin", "kangaroo",
    "mystery", "adventure", "treasure", "pyramid", "labyrinth",
    "shadow", "phantom", "ghost", "skeleton", "zombie",
    "energy", "gravity", "fractal", "quantum", "neutron",
    "coffee", "chocolate", "sandwich", "pancake", "cookie",
    "smile", "friendship", "happiness", "freedom", "courage"
]
chosenWord = random.choice(wordbank)
guessletters = []
for i in range(len(chosenWord)):
    guessletters.append("_")
print(chosenWord)
print(guessletters)

while livesCounter > 0:
    userinput = input("Enter your letter \n")
    if len(userinput) !=1:
        print("Your input must be one letter!")
        continue
    for i in range(len(chosenWord)):
        if userinput == chosenWord[i]:
            guessletters[i] = userinput
    if userinput not in chosenWord:
        livesCounter -= 1
    print(guessletters)
    print("You have " + str(livesCounter) + " lives left")
    if "_" not in guessletters:
        print("You win!")
        break
if livesCounter == 0:
    print("You lost! Haha, the word was " + chosenWord)
