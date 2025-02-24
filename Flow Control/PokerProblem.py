
# In the game of poker, the player holds 2 cards in his hand and there are 5 cards on the table.
# You have a flush IF out of these 7 cards, 5 of them come from a single suit i.e spades, diamonds, hearts and clubs.
# Given two lists one for the table and one for the hand, write a snippet of code to determine if you have a flush or not.
# Each card is represented by a number (1,2 3, 10, J, Q, K) followed by an hyphen and then the 1 letter suit abbreviation.
# So J-H is Jack of Hearts and A-S is the ace of spades.

table = ["1-S", "6-C","9-D", "J-S","K-S"]
hand = ["1-H", "6-S"]
spades_cnt = 0
diamonds_cnt = 0
hearts_cnt = 0
clubs_cnt = 0



for i in table:
    # print(i[2])
    if i[2] == 'S':
        spades_cnt += 1
    elif i[2] == 'D':
        diamonds_cnt += 1
    elif i[2] == 'H':
        hearts_cnt += 1
    elif i[2] == 'C':
        clubs_cnt += 1
    else:
        print("Error in the List.")
        break

for j in hand:
    # print(j[2])
    if j[2] == 'S':
        spades_cnt += 1
    elif j[2] == 'D':
        diamonds_cnt += 1
    elif j[2] == 'H':
        hearts_cnt += 1
    elif j[2] == 'C':
        clubs_cnt += 1
    else:
        print("Error in the List.")
        break

if spades_cnt >= 5:
    print(f"You have a flush with {spades_cnt} Spades.")
elif diamonds_cnt >= 5:
    print(f"You have a flush with {diamonds_cnt} Diamonds.")
elif hearts_cnt >= 5:
    print(f"You have a flush with {hearts_cnt} Hearts.")
elif clubs_cnt >= 5:
    print(f"You have a flush with {clubs_cnt} Clubs.")
else:
    print(f"You do not have a flush.")
