
# Write a program to look at all the numbers between 2 numbers
# and print out the ones that have only even numbers in their digits.
# start = 1000
# stop = 3000

start = int(input("\nEnter a starting number: "))
end = int(input("Enter an ending number: "))

even_digit_numbers = []  

for i in range(start, end + 1):  
    if all(int(digit) % 2 == 0 for digit in str(i)):  
        even_digit_numbers.append(i)

print("Numbers with only even digits:", even_digit_numbers)
