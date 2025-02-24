# Write code so that given a string with an odd number of characters and greater than 7 characters, return the middle 5 characters.
# Example: 'seventy' returns 'event', 'hello python!' returns 'o pyt'

string = input("\nEnter a string: ")

if len(string) % 2 == 1 and len(string) >= 7:
    new_string = string[round(len(string) / 2) -3:round(len(string) / 2) +2]
    print(new_string) 

else:
    print("Invalid String.")

