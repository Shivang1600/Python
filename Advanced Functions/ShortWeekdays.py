
# Use a map function to convert the following list of weekday names to their short forms 
# i.e first three letters. Ensure that the first letter is capitalized.


weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def short(each_day):
    return each_day[0:3].capitalize()

print(list(map(short, weekdays)))
    
