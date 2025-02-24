# Given a string, take the 3rd character and add it to the end of the string 100 times.
# For example, 'python' should give 'pythontttttttttttttttttttttt...'

word = input("\nEnter a word: ")

# if len(word) >= 3:
#     ch = word[2]
#     n = 100
#     for x in range(n):
#         word += ch    

#     print(word.count(ch))
#     print(word)
# else:
#     print("String too short!")
word = word + word[2]*100
print(word)