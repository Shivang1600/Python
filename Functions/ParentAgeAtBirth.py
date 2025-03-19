# Write a function that takes 3 parameters the birth year of a man, woman and their child and 
# calculates the ages of the father and mother when the child was born.
# Perform some checking to see that the birth year of the father and mother are atleast 18 years 
# when the child was born but the age of the either parent cannot be greater than 60 when the child was born.
# Output the appropriate message when the ages are out of these bounds.

def parent_age(f_yob, m_yob, c_yob):
    f_age = c_yob - f_yob 
    m_age = c_yob - m_yob

    if f_age < 18 or m_age < 18:
        print("The parents were too young when they had their child.")
    elif f_age >= 60 or m_age >= 60:
        print("Age out of bound! Parents cannot have kids this late.")
    else:
        print(f"The father was {f_age} old and the mother was {m_age} old when they had the child.")

parent_age(1967, 1970, 1998)
