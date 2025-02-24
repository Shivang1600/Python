# Write a small script to replace the first letter of a string with its uppercase equivalent.
# The rest of the string must be untouched.

word = input("\nEnter a word: ")

if len(word) >= 1:
    new_word = word[0].upper() + word[1:]
    print(new_word)
else:
    print("Empty String!")