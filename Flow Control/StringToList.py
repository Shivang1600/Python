
# Write a program to accept multiple comma separated numbers AS input from the user and 
# create a list of integers by extracting them out of the input.

user_input = input("\nEnter comma-separated numbers: ")

list_of_int = []

new_list = user_input.split(",")

for i in new_list:
    temp = int(i.strip())
    list_of_int.append(temp)
    print(type(temp))
    
print(f"User input {user_input} is of type {type(user_input)}")
print(f"New List {new_list} is of type {type(new_list)}")
print(f"List of INT {list_of_int} is of type {type(list_of_int)}")
