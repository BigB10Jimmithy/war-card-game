from card import *
from tools import *

class Player(object):

    def __init__(self, name, number, colour):
        self.name = name
        #I believe number is the number of the arrow inside the card
        #indicating the number is in relation to position of the arrow
        self.number = number
        self.colour = colour
        self.cards = []
        #creates the hands in the deck
        #see if you can have these in their own cards
        arrows1 = 3
        self.cards.append(Card(arrows1, number, 1, colour))
        arrows2 = 2 #randint(2, 4)
        self.cards.append(Card(arrows2, number, 2, colour))
        arrows3 = 6 #randint(3, 6)
        self.cards.append(Card(arrows3, number, 3, colour))
        self.cards.append(Card(4, number, 4, colour))
        arrows5 = 7 #18 - (4 + arrows1 + arrows2 + arrows3)
        self.cards.append(Card(arrows5, number, 5, colour))

################################################################
        self.score = 0
        self.round = 0

    def handReset(self):
        self.cards = []
        arrows1 = randint(1, 2)
        self.cards.append(Card(arrows1, self.number, 1, self.colour))
        arrows2 = randint(2, 4)
        self.cards.append(Card(arrows2, self.number, 2, self.colour))
        arrows3 = randint(3, 6)
        self.cards.append(Card(arrows3, self.number, 3, self.colour))
        self.cards.append(Card(4, self.number, 4, self.colour))
        arrows5 = 18 - (4 + arrows1 + arrows2 + arrows3)
        self.cards.append(Card(arrows5, self.number, 5, self.colour))
        
    #looking to get the function changed to act as a deletion
    #def colourChange(self):
     #   number = int(raw_input("1 = red, 2 = blue, 3 = green, 4 = black"))
      #  self.colour = allColours(number)

    #function to all card that is selected
    #attribute clickedCard is refered to in card file
    def cardPick(self, x, y):
        for card in self.cards:
            #changed clickedCard to isClickedOn
            #I might want to change this callable attribute to something else if possible
            #it's used in the original source, find out where it's from
            if card.CardIsClickedOn(x,y):
                if card.clickedCard: #clickedCard = isSelected
                    card.clickedCard = not card.clickedCard
                    playersCard = None #playersCard = cardSelected
                else:
                    for cardtochange in self.cards: #check cardtochange
                        cardtochange.clickedCard = False
                    card.clickedCard = True
                    playersCard = card
        for card in self.cards:
            if card.clickedCard:
                return True
        return False

    #function allows selected cards onto the game map
    def getCard(self,number):
        if number > 5 or number < 1: #if number greater than 5 or less than one then
            print ("number is wrong") #print statement, this seems redunant as the program can go beyond 5
        else:
            for x in range(len(self.cards)): #for x that is in range of the legnth of cards attribute
                if self.cards[x].number == number: #if the card x is in range of number variable then
                     return self.cards.pop(x) #return data but remove x from the array
            print ("The player " + str(self.player) + " doesn't have the card number " + str(number) + " on his/her hand.") #never seen this happen in game, removable?
    #function to add a card to the grid
    #also allows for conditions if the card is placed outside of the list
    def addCard(self,card):
        self.cards.append(card)

    #function that allows user to click on card in hand
    def getSelectedCard(self):
        for card in self.cards:
            if card.clickedCard: #change
                return card
        return None
