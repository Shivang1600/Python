# Consider the following tuple with a bunch of floating point numbers. 
# Write a map function which returns a list subject to the following conditions.
# If a number is less than -1, then we replace it with a zero. 
# If a number is greater than 1, then we replace it with a one. 
# If a number is between -1 and +1, we round it to 1 decimal point.

org = (-1.5, -0.756, 0.91, 5.6, -10.0, 12.2)


def each_num(num):
    if num > 1:
        num = 1
    elif num < -1:
        num = 0
    elif num >= -1 and num <= 1:
        num = round(num,1) 

    return num

result = list(map(each_num, org))
print(result)
