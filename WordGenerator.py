import random

word_bank = [
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

class WordGenerator:
    def __init__(self):
        self.random_word = random.choice(word_bank)

    def add_word(self, new_word):
        word_bank.append(new_word)
        return True
    
    def remove_word(self, word):
        if word in word_bank:
            word_bank.remove(word)
            return True
        return False

    def get_random_word(self):
        return self.random_word