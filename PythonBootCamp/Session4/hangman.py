# step 1
from random import random
from secrets import choice

word_list = ["ardvark","baboon","camel"]
# random selection of world list
chosen_word = choice( word_list )
# print( chosen_word )
chosen_word_length = len(chosen_word)
# print(chosen_word_length)
#print("-"*chosen_word_length)
print(f"Psst, the word is: {chosen_word}")
display = []
for i in range(chosen_word_length):
    display +="_"
print(display)
end_of_game = False
while not end_of_game:
    guest = input ( "Guess a letter: " ).lower ()

    for position in range(chosen_word_length):
        letter = chosen_word[position]
        if letter == guest:
            display[position] = letter


    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win.")