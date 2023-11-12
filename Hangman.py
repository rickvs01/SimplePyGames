################################ Hangman Game #####################################
##Import Packages

from random_word import RandomWords
from os import system, name
#from replit import clear

#### Define Global Variables ####
r = RandomWords()
already_provided = []
display_tracker = []
display_tracker_cnt = 0
end_of_game = False
lives = 6
stage = -1
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')

#### Game Starts ####

print("******************************* Welcome to Hangman! *******************************")
print(logo)
print(stages[0])

#This choses a random word in English for the game
word = r.get_random_word()

#Create the intital letter display tracker
for letter in word:
    display_tracker += "_"
    display_tracker_cnt += 1
print(f'There are {display_tracker_cnt} letters in the word.\n {display_tracker}')

#Continue Game until it is solved:
while not end_of_game:
#Test each letter

    user_input = input("Pick a Letter: ").lower()
    print("\n" * 100)
    #clear()
    round_luck = 0
    if user_input not in already_provided:

        for position in range(len(word)):
            letter = word[position]

            if letter == user_input:
                display_tracker[position] = letter
                round_luck = 1

        if round_luck == 1:
            print(logo)
            print(f"Good choice! {user_input} is in the word")

        else:
            print(logo)
            print(f"Sorry, {user_input} is not in the word.")
            lives -= 1
            stage -= 1
        already_provided += user_input

        if "_" not in display_tracker:
            end_of_game = True
            print("You Win the game!!")

        if lives == 0:
            end_of_game = True
            print("You lose the game!")
            print(f'Psst... the answer was {word}')
        print(stages[stage])
        print(display_tracker)
    else:
        print(logo)
        print(stages[stage])
        print(display_tracker)
        print(f"Sorry, you have already tested {user_input}. Try another letter")




