# Write a list comprehension which doubles the positive numbers 
# in a list and halves the negative numbers.

c = [1, 2, -3, -4, 5, -6, 7]

result = [n*2 if n > 0 else n*0.5 for n in c]
print(c, result)

