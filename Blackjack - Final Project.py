'''
Author: Chris Beaudoin
Date: 12/03/2024 - 12/05/2024
Purpose: Final Project - Game of Blackjack
'''

#Imports
import random
import time

#Defining Deck of Card Values:
cardValues = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 
              'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Queen': 10, 
              'King': 10, 'Jack': 10, 'Ace': 11}

#Defining The Deck of Cards Suits and Ranks.
cardSuits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
cardRanks = list(cardValues.keys())

#Creation of Card Deck, Combining the Ranks and Suits.
cardDeck = []
for suit in cardSuits:
    for rank in cardRanks:
        cardDeck.append((rank, suit))
cardDeck *= 2 #Duplicating the Deck to Have 2 Sets for the Game.

#Functions For Card Dealing, Hand Calc's, Card Display.
def dealCards(cardDeck):
    return cardDeck.pop(random.randint(0, len(cardDeck) - 1))

def calcHand(hand):
    value = sum(cardValues[card[0]] for card in hand)
    numAces = sum(1 for card in hand if card [0] == 'Ace') #Adjusts For Aces to Avoid Busting.
    while value > 21 and numAces:
        value -= 10
        numAces -= 1
    return value

def displayCards(hand, name):
    handName = f"{playerName}" if name == "Player" else "Dealer"
    if name == "Player":
        print(f"{handName}, your Dealt Hand is: ", ', '.join(f'{rank} of {suit}' for rank, suit in hand))
        print(f"{handName}, your Hand Total is: {calcHand(hand)}")
    else:
        print(f"{handName}'s Hand: ", ', '.join(f'{rank} of {suit}' for rank, suit in hand)) 
        print(f"{handName}'s Hand Totals: {calcHand(hand)}")
    time.sleep(1) #Time Sleep is Added for Realistic Game Play.

def checkForblackjack(hand):
    return calcHand(hand) == 21

def checkForbust(hand):
    return calcHand(hand) > 21

#Functions For Player/Dealer Turns
def playersTurn(cardDeck, playersHand):
    while True:
        displayCards(playersHand, "Player")        
        if checkForblackjack(playersHand):
            print(f"{playerName}, You've Got Blackjack! You Win!")
            return False
        elif checkForbust(playersHand):
            print(f"{playerName}, You Busted! The Dealer Wins!")
            time.sleep(1) #Time Sleep is Added for Realistic Game Play.
            return False
        while True:
            action = input(f"{playerName}, Would You Like to Hit or Stay? Please Type H or S: ").lower()            
            if action in ['h', 's']:
                break
            else:
                print("Invalid Input. Try Again!")                
        if action == 'h':
            playersHand.append(dealCards(cardDeck))
            time.sleep(1)
        else:
            break
    return True

def dealersTurn(cardDeck, dealersHand):
    displayCards(dealersHand, "Dealer")
    while calcHand(dealersHand) < 18:
        dealersHand.append(dealCards(cardDeck))
        displayCards(dealersHand, "Dealer")
        time.sleep(1) #Time Sleep is Added for Realistic Game Play.
    if checkForbust(dealersHand):
        print("The Dealer Has Busted! You Win!")
        time.sleep(1)
        return False
    return True

#Function To Determine The Winner
def whoWins(playersHand, dealersHand):
    playersValue = calcHand(playersHand)
    dealersValue = calcHand(dealersHand)
    print(f"{playerName}, Your Final Hand Total is: {playersValue} ")
    time.sleep(1) #Time Sleep is Added for Realistic Game Play.
    print(f"The Dealer's Final Hand Total is: {dealersValue} ")
    time.sleep(1)
    if playersValue > dealersValue:
        print(f"{playerName}, You Win!")
    elif playersValue < dealersValue:
        print("The Dealer Has Won!")
    else:
        print(" It's a Push! No Winner Declared.")
    time.sleep(1)

#The Main Function/Menu to Play the Game
def letsPlayblackjack():
    print("Welcome to My Game of Blackjack!")
    time.sleep(1)
    print("The Goal of Blackjack is: To Get a Hand that's Closer to 21 than the Dealer's Hand Without Going Over 21.")
    time.sleep(2)
    global playerName #Added Use of Real Name for Added Personalization in the Game.
    playerName = input("Enter Player's Name Here: ")
    print(f"Welcome, {playerName}! Let the Game Begin!")
    time.sleep(2) #Time Sleep is Added for Realistic Game Play.
    
    deckCopy = cardDeck[:]
    random.shuffle(deckCopy)
    
    playersHand = []
    dealersHand = []
    
    for _ in range(2):
        playersHand.append(dealCards(deckCopy))
        
    for _ in range(2):
        dealersHand.append(dealCards(deckCopy))    
    
    displayCards(dealersHand, "Dealer")
    
    if checkForblackjack(dealersHand):
        print("Dealer Has Blackjack! Game Over!")
            
    if playersTurn(deckCopy, playersHand):
        if dealersTurn(deckCopy, dealersHand):
            whoWins(playersHand, dealersHand)

def main():    
    while True:
        letsPlayblackjack()
        newGame = input("Play Another Hand? Enter Y or N: ").lower()
        time.sleep(1)
        if newGame == 'n':
            print("Thank You For Playing Blackjack!")
            break
        
main()
    


