############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []







#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


import random


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# Define deck of cards
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    """Returns a random card from the deck with replacement"""
    return random.choice(cards)

def play_game():
#Create empty list to hold player and dealer cards
    print("\n"*1000)
    print(logo)
    player_cards = []
    dealer_cards = []

    #Initial card draw
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    #This function calculates the score
    def calculate_score(list):
        score = sum(list)
        if score == 21:
            score = 0
        if score > 21:
            for card in range(len(list)):
                if list[card] == 11:
                    list[card] = 1
                    score = sum(list)
        return score

    def compare( player_score, dealer_score):
        if player_score == dealer_score:
            return "Draw"
        elif player_score == 0:
            return "You win with a Blackjack!"
        elif dealer_score== 0:
            return "You lose, dealer has a Blackjack"
        elif player_score > 21:
            return "You went over, You lose"
        elif dealer_score > 21:
            return "Dealer went over, You win!"
        elif player_score > dealer_score:
            return "You win"
        else:
            return "You Lose"

    player_score= calculate_score(player_cards)
    dealer_score= calculate_score(dealer_cards)

    print(f"Your cards are: {player_cards}, current score is {player_score}")
    print(f"First dealer card is: {dealer_cards[0]}")


    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

    if player_score == 0 or player_score >21 or dealer_score == 0 or dealer_score >21:
        game_continues = False
    else:
        game_continues = True

    while game_continues:
        another_one = input("Would you like to draw another card? 'y' or 'n'")
        if another_one == 'y':
            player_cards.append(deal_card())
            player_score = calculate_score(player_cards)
            print(f"Your cards are: {player_cards}, current score is {player_score}")
            print(f"First dealer card is: {dealer_cards[0]}")
        while dealer_score < 17:
            dealer_cards.append(deal_card())
            dealer_score = calculate_score(dealer_cards)
        print(f"Your final cards are: {player_cards}, current score is {player_score}")
        print(f"dealer_cards = {dealer_cards}, and dealer score is {dealer_score}")
        game_continues = False

    print(compare(player_score,dealer_score))
while input("Do you want to play a hand of Blackjack? Type 'y' or 'n':")== "y":
    play_game()







#print(player_score)
#print(player_cards)
#print(dealer_score)
#print(dealer_cards)
