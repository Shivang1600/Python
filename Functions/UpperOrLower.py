
# Create a function that will count the number of uppercase and
# lowercase characters in a string.

def find(my_str):
    upper = 0
    lower = 0
    for i in my_str:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper, lower

upper, lower = find("ShiVAng")

print(f"There are {upper} uppercase letters and {lower} lowercase letters.")
