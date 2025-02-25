
# Create a program that asks the user to guess words one character at a time.
# The program should choose a word from a list of words at random and ask the user to input their guesses one character at a time.
# If the character appears in the word, display all the locations where the character appears and continue till the entire word
# has been guessed correctly.
# Keep track of the total number of tries it took to fully guess the word.
import random

words = [
    "Apple", "Ball", "Cat", "Dog", "Elephant", "Fish", "Goat", "House", "Ice", "Jump",
    "Kite", "Lion", "Monkey", "Nest", "Orange", "Pencil", "Queen", "Rabbit", "Sun", "Tree",
    "Umbrella", "Violin", "Water", "Xylophone", "Yellow", "Zebra", "Happy", "Funny", "Strong", "Smile"
]

random_word = random.choice(words)
guess_word = "-" * len(random_word)

while guess_word != random_word:
    print(f"\n{guess_word}")
    guess_word_list = list(guess_word)
    guess_char = input("Guess a character: ")
    for i in range(len(random_word)):
        if guess_char == random_word[i]:
            guess_word_list[i] = random_word[i]
            guess_word = "".join(guess_word_list)
        else: 
            guess_word = "".join(guess_word_list)
            continue
    print("Wrong guess, try again!")
print(f"\nYou Win! The word is {guess_word}")



    