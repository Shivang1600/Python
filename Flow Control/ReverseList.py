# Reverse the list x = [1,2,3,4] using a for loop. Dont use reverse or [::-1] notation.

# x = [1,2,3,4]
# y = []
# # x.reverse()
# for temp in range(len(x)):
#     y.append(x.pop()) 

# print(y)


x = [1, 2, 3, 'python', 4, 'hello']
index = -1
newx = [None] * len(x)
for e in x:
    newx[index] = e 
    index -= 1

x = newx
print(x)