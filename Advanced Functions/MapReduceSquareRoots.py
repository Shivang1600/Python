# Write a map-reduce function to calculate the square 
# root of the sum of squares of a list of integers.


# import math

from functools import reduce

# def SrSSI(mylist):
#     mysum = 0
#     for n in mylist:
#         mysum += n*n

#     return math.sqrt(mysum)

mylist = [3, 4, 5]
result = reduce(lambda n1,n2: (n1**2 + n2**2)**0.5,mylist)
print(result)
