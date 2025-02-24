
# Create a program that takes two strings and calculates if they are anagrams of each other.
# Also calculate the Hamming distance between the strings.
# A hamming distance is a measure of how different two strings are from each other.
# egg and peg have a Hamming distance of 2.
# You compare the strings character by character and increase Hamming distance by 1 if they are different and zero if the same.
# mead and read have a Hamming distance of 1 since the 1st characters are the only ones different.

string1 = input("\nEnter String 1: ")
string2 = input("Enter String 2: ")

distance = 0

if sorted(string1) == sorted(string2):
    print("The strings are anagrams.")
else:
    print("The strings are NOT anagrams.")

if len(string1) != len(string2):
    print("Hamming distance is not defined for strings of different lengths.")
else:
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    print(f"Hamming distance is {distance}")
