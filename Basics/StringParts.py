# Write a small Python script to extract the first and last characters of a string and create a new string.
# For example, if the input string is axyz, the output should be az.

def first_and_last(s):
    if len(s)>=2:
        return s[0] + s[-1]
    else:
        return s
    
user_input = input("\nEnter a string: ")

result = first_and_last(user_input);

print(result)