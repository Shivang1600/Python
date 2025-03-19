
# Write a function that will take a list of numbers and return
# the maximum value of that list.
# Do not use the max function.

def f_max_num(my_list):
    max_num = my_list[0]
    for n in my_list:
        if n > max_num:
            max_num = n
        else:
            continue
    return max_num

new_list = [23, 45, 12, 67, 34, -89, 2]

max_value = f_max_num(new_list)
print(max_value)