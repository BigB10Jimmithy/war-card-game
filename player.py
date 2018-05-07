from card import *
from tools import *
import random
import copy

class Player(object):

    def __init__(self, name, number, colour):
        self.name = name
        self.CardsOrder = random.sample(range(1,7),5)
        #I believe number is the number of the arrow inside the card
        #indicating the number is in relation to position of the arrow
        self.number = number
        self.colour = colour
        self.handReset()
        
        #creates the hands in the deck
        #see if you can have these in their own cards
        self.score = 0
        self.round = 0
##################################################################################

    #this function creates a hand of 5 cards for each player and shuffles from
    #a set of cards, so to make sure that palyer's don't have the same hand.
    def handReset(self):
        #create a array for the cards
        cards = []
        self.cards = []
        number = self.number
        colour = self.colour
        #creates the hands in the deck
        #see if you can have these in their own cards
        #arrowCountList is the array containing the range of numbers it can equal
        arrowCountList = [1,2,3,4,5,6,7]#randint 2 to 7
        selectionList = random.sample(range(5),5)

        #for loop to append the cards with arrows?
        for i in range(1,7):#i in range of 1 to 5 gives the arrows in card placement 1 to 5
            cards.append(Card(arrowCountList[i-1], number, i,colour))
        ind = 0

        for i in range(5):
            #print(i,selectionList[ind])
            card1 = cards[i]#card 1 represents player 1's set of cards
            card2 = cards[selectionList[ind]]
            temp = copy.deepcopy(card1) 
            card1.arrows = card2.arrows  
            card2.arrows = temp.arrows
            print(i,cards[i].arrows)
            ind +=1
            self.cards.append(cards[i])

            #i.number = selectionList[ind]
            #ind +=1
            #print(i.number,i.arrows)
        '''arrows1 = 3
        self.cards.append(Card(arrows1, number, 1, colour))
        arrows2 = 2 #randint(2, 4)
        self.cards.append(Card(arrows2, number, 2, colour))
        arrows3 = 6 #randint(3, 6)
        self.cards.append(Card(arrows3, number, 3, colour))
        self.cards.append(Card(4, number, 4, colour))
        arrows5 = 7 #18 - (4 + arrows1 + arrows2 + arrows3)
        self.cards.append(Card(arrows5, number, 5, colour))
        '''
        #print("one",self.cards)
        #self.cards = random.shuffle(self.cards)
		#print(self.cards)

    #function to all card that is selected
    #attribute clickedCard is refered to in card file
	
    def AIcardPick(self):
        print('AI card pick Method')
        choice = random.randrange(0,len(self.cards))
        card =  self.cards[choice]
        card.clickedCard = True
        playersCard = card
        return True
		
    def cardPick(self, x, y):
        for card in self.cards:
            #changed clickedCard to isClickedOn
            #I might want to change this callable attribute to something else if possible
            #it's used in the original source, find out where it's from
            if card.CardIsClickedOn(x,y):
                if card.clickedCard: #if card within the class of cards is clicked on then
                    card.clickedCard = not card.clickedCard
                    playersCard = None #playersCard is the card the player has selected in his hand
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
                    #deletes card from hand data
                     return self.cards.pop(x) #return data but remove x from the array
            print ("The player " + str(self.player) + " doesn't have the card number " + str(number) + " on his/her hand.") #never seen this happen in game, removable?
    
    #function to add a card to the grid
    #also allows for conditions if the card is placed outside of the list
    def addCard(self,card):
        #adds cards
        self.cards.append(card)

    #function that allows user to click on card in hand
    def getSelectedCard(self):
        #for loop for card inside self.cards, if they are clicked on
        for card in self.cards:
            if card.clickedCard: #change
                return card
        return None
