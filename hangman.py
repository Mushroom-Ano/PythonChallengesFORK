from WordGenerator import WordGenerator
lives_counter = 10

word_gen = WordGenerator()
chosen_word = word_gen.get_random_word()

guess_letters = []
for i in range(len(chosen_word)):
    guess_letters.append("_")
print(chosen_word)
print(guess_letters)

while lives_counter > 0:
    print("you have " + str(lives_counter) + " lives left")
    user_input = input("enter your letter \n")
    user_input = user_input.lower()
    if len(user_input) == len(chosen_word):
        if(user_input == chosen_word):
            print("you win!")
            break
        else:
            print("incorrect guess!")
            lives_counter-=1
    elif len(user_input) !=1:
        print("your input must be one letter, or the exact length of the word!")
        continue
    else:
        for i in range(len(chosen_word)):
            if user_input == chosen_word[i]:
                guess_letters[i] = user_input
        if user_input not in chosen_word:
            lives_counter -= 1
        print(guess_letters)
        if "_" not in guess_letters:
            print("you win!")
            break
    print()
if lives_counter == 0:
    print("you lost! haha, the word was " + chosen_word)


