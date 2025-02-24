# A weight lifter bench presses every day and keeps track of the weights inside a list on a day to day basis.
# He wants to measure his progress and has what he calls a progress day. This is a day where he has lifted more weight on a particular day than the two days preceeding.
# For example [200, 205, 210, 206].
# The 3rd day would be considered a progress day because 210 is larger than 200 and 205 (the two preceding weights).
# However, the 4th day is not because while 206 is greater than 205, it is not greater than 210.
# Equality of weights does not count as a progress day. [180, 190, 190, 191]. The 3rd day is not a progress day while the 4th day is.



x = []

days  = input("How many days do you want to enter: ")
days = int(days)
days += 1
progress_days = 0
for i in range(1,days):
    x.append(input(f"\nEnter Day {i} Weight: "))
    
for j in range(len(x)-2):
    if x[j+1] > x[j] and x[j+2] > x[j+1]:
        print(f"The {j+2+1} day is the progress day.")
        progress_days += 1
        continue

print(f"Progress Days Count: {progress_days}")
