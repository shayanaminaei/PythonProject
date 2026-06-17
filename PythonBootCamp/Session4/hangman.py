from secrets import choice
banner = """
██   ██  █████  ███    ██  ██████      ███    ███  █████  ███    ██ 
██   ██ ██   ██ ████   ██ ██           ████  ████ ██   ██ ████   ██ 
███████ ███████ ██ ██  ██ ██   ███     ██ ████ ██ ███████ ██ ██  ██ 
██   ██ ██   ██ ██  ██ ██ ██    ██     ██  ██  ██ ██   ██ ██  ██ ██ 
██   ██ ██   ██ ██   ████  ██████      ██      ██ ██   ██ ██   ████ 
                                                                    
                                                                    
"""
print(banner)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========''']


word_list = ["ardvark","baboon","camel"]
chosen_word = choice( word_list )
# print( chosen_word )
lives = 6

#chosen word test, if you want fill free to remove it
print(f"Psst, the word is: {chosen_word}")
display = []
chosen_word_length = len(chosen_word)
for i in range(chosen_word_length):
    display +="_"
print(display)
end_of_game = False


while not end_of_game:
    guess = input ( "Guess a letter: " ).lower ()

    for position in range(chosen_word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if  guess not in display:
        lives -=1
        if lives == 0:
            end_of_game = True
            print("you lose...")


    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win :)")


    print(stages[lives])