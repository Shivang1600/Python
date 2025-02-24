
# The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
# Example of characters that are not alphanumeric: (space)!#%&? etc.

x = 'abc123' 
y= 'abc 123'
z = '3.14'
a = x.isalnum()
b = y.isalnum() 
c = z.isalnum()

print(a,b,c)

