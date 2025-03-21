
# Using a list comprehension, convert a list of temperatures in Celsius to Fahrenheit.
# also add condition to output all positive temperatures.

c = [0, 100, -55, 25, 50, -40]

f = [e * 9/5 + 32 for e in c if e >= 0]
print(f, c)
