# Consider the following list which contains tuples. Each tuple has a number and a string as its elements.
# x = [(3,'Santino'), (1, 'Vito'), (4, 'Fredo'), (10,'Tessio'), (7,'Connie'), (9,'Clemenza'), (2, 'Michael')]
# Sort the list in ascending order of the number.

def bbl_sort(tup):
    for i in range(len(tup)):
        for j in range(len(tup) - i - 1):
            if tup[j][0] > tup[j + 1][0]:
                tup[j], tup[j+1] = tup[j+1], tup[j]
    
tup = [(3,'Santino'), (1, 'Vito'), (4, 'Fredo'), (10,'Tessio'), (7,'Connie'), (9,'Clemenza'), (2, 'Michael')]

bbl_sort(tup)

print(tup)