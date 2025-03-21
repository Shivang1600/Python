# Consider the following tuple:

# Filter the tuple to retain only the strings that have valid numbers.

x = ('1', '2', 'hello', '23', 'python', 'abc123')

def check(element):
    if element.isnumeric():
        return True
    else:
        return False
    
y = list(filter(check, x))
print(y)

