import random

from WordGenerator import WordGenerator

livesCounter = 10

word_generator = WordGenerator()
chosenWord = word_generator.get_random_word()

guessletters = ["_" for i in range(len(chosenWord))]

# for i in range(len(chosenWord)):
#     guessletters.append("_")
print(chosenWord)
print(guessletters)

while livesCounter > 0:
    print("You have " + str(livesCounter) + " lives left")
    userinput = input("Enter your letter \n")
    userinput = userinput.lower()
    if len(userinput) == len(chosenWord):
        if(userinput == chosenWord):
            print("You win!")
            break
        else:
            print("Incorrect guess!")
            livesCounter-=1
    elif len(userinput) !=1:
        print("Your input must be one letter, or the exact length of the word!")
        continue
    else:
        for i in range(len(chosenWord)):
            if userinput == chosenWord[i]:
                guessletters[i] = userinput
        if userinput not in chosenWord:
            livesCounter -= 1
            if livesCounter == 3:
                print("Clue: " + chosenWord[0:1])
        print(guessletters)
        if "_" not in guessletters:
            print("\U0001f600 You win!")
            break
    print()
if livesCounter == 0:
    print("\U0001F923 You lost! Haha, the word was " + chosenWord)


