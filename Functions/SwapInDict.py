# Write a function that swaps the keys and values of a dictionary.
# Assume that the values are immutable.

def swap_dict(my_dict):
    new_dict = {}
    for k,v in my_dict.items():
        new_dict[v] = k
    
    return new_dict

sample_dict = {
    'apple': 1,
    'banana': 2,
    'cherry': 3,
    'date': 4,
    'elderberry': 5
}

swapped_dict = swap_dict(sample_dict)
print(swapped_dict)