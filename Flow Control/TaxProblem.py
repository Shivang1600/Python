
# Tax Tables:
# A country has the following income tax structure:
# 0-10000 0%
# 10001-20000 5% above 10,000
# 20001-50000 10% above 20000 plus
# 50001-100000 15%
# 100001 and above 20%
# The tax structure is progressive i.e if a persons income is 25,000$,
# the first 10000 incurs 0% income tax, the next 9999$ a 5% tax and the remaining 4999$ at 10%.
# The total tax owed is then
# 10000*0+ (20000-10000) *.05+ (25000-20000)*.1
# = 1000$

income = input("\nEnter your income: $")
income = int(income)
tax = 0

if income <= 10000:
    print("You are poor! You do not owe any tax.")
elif income >= 10001 and income <= 20000:
    tax = (income - 10000) * 0.05
    print(f"You owe a tax of ${tax}")
elif income >= 20001 and income <= 50000:
    tax = ((20000 - 10000) * 0.05) + ((income - 20000) * 0.1)
    print(f"You owe a tax of ${tax}")
elif income >= 50001 and income <= 100000:
    tax = ((20000 - 10000) * 0.05) + ((50000 - 20000) * 0.1) + ((income - 50000) * 0.15) 
    print(f"You owe a tax of ${tax}")
elif income >= 100001:
    tax = ((20000 - 10000) * 0.05) + ((50000 - 20000) * 0.1) + ((100000 - 50000) * 0.15) + ((income - 100000) * 0.2)
    print(f"You owe a tax of ${tax}")