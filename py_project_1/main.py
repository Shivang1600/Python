# print("Prabhjot")
# print('o-----')
# print(' ||||')
# print('*' * 10)
# price = 10
# rating = 4.9
# name = 'Jatin'
# is_published = True
# print(price)
# name = input('what is your name? ')
# print('Hi ' + name)
# birth_year = input('birth year: ')
# print(type(birth_year))
# age = 2021 - int(birth_year)
# print(age)
# print(type(age))
# weight_lbs = input('weight (lbs): ')
# weight_kg = float(weight_lbs) * 0.45
# print(weight_kg)
# course = '''
# Hi John,
#
# Here is our first email to you.
#
# Thank you,
# The support Team
# '''
# print(course)
# course = 'Python for Beginners'
# another = course[:]
# print(another)
# name = 'Jennifer'
# print(name[1:-1])
# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(msg)
# course = 'Python for Beginners'
# print('python' in course)
# print(10 % 3)
# x = 10
# x -= 3
# print(x)
# x = (10 + 3) * 2 ** 2
# print(x)
# x = 2.9
# print(abs(-2.9))
# import math
# print(math.floor(2.9))
# is_hot = False
# is_cold = False
# if is_hot:
#     print("it 's a hot day")
#     print("drink plenty of water")
# elif is_cold:
#     print("it s a cold day")
#     print("wear warm clothes")
# else:
#     print("it s a lovely day")
# print("enjoy your day")



# ............ 26th Feb 2021 ............ #

# .......... Mini-Project to convert weight from kg to lbs or visa-versa ..........#

# weight = int(input("Enter the weight: "))
# unit = input("(L)bs or (K)gs: ")
# if(unit.upper() == "L"):
#     converter = weight * 0.454
#     print(f"Your weight is {converter} KGS")
#
# elif(unit.upper() == "K"):
#     converter = weight / 0.454
#     print(f"Your weight is {converter} LBS")

# ...................................... Done .....................................#

# .......... While loop ..........#

# count = 1
# while count <= 5:
#     print("*" * count)
#     count = count + 1

# .............. Done ..............#

# .......... Mini-Project to implement a guessing game ..........#

# secret_number = 9
# attempts = 3
# guess_count = 0
#
# while(guess_count < attempts):
#     guess = int(input(f"Guess {guess_count + 1} : "))
#     guess_count += 1
#     if(guess == secret_number):
#         print("You win...!")
#         break
#
# else:
#     print("You failed...!")

#Note: inside the while loop we have provision to provide else loop

# ...................................... Done .....................................#

# .......... Hands On Exercise ..........#

# name = input("Enter a name: ")
# if(len(name) < 3):
#     print("Name must be at least 3 characters long.")
# elif(len(name) > 50):
#     print("Name cannot exceed 50 characters.")
# else:
#     print("Name looks good")

# .............. Done ..............#