# You are given two lists which have the same number of elements. 
# Print the elements inside a single for loop.

x = [1, 2, 3]

y = ['one', 'two', 'three']

for index, e in enumerate(x):
    print(e,y[index])