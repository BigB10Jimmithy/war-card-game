from tools import *
import random

class Board(object):
    def __init__(self,size, players):
        self.size = size
        self.board = []
        self.player = players
        #self.curPlayerNum = randint(0,len(self.player)-1)
        self.curPlayerNum = 0
        self.curPlayer = self.player[self.curPlayerNum]
        self.pointsOnBoard = 0
        self.TotalScore = 0

        for y in range(size):
            line = []
            for x in range(size):
                line.append(atHolder(y,x) )
            self.board.append(line)

        if Point():
            self.TotalScore = randint(1,6)
            print("player's score is " + str(self.TotalScore) + ".")
        else:
            print("current score is 0")

        while self.pointsOnBoard != self.TotalScore:
            randomX = randint (0, self.size -1)
            randomY = randint (0, self.size -1)

            #animation keeps disapears? look into this
            if not self.board[randomY][randomX].beaten:
                self.pointsOnBoard += 1
                self.board[randomY][randomX].defeated()

        self.finalizeScore()

#I want to get this bit changed to a computer ai instead of a second player
#or at least have it included
    def NextPlayerTurn(self):
        self.curPlayerNum = (self.curPlayerNum+1) % len(self.player)
        self.curPlayer = self.player[self.curPlayerNum]

###################################################################################
    def get(self, X, Y):
         return self.board[Y][X].inside

###############################################################################
    #deals with attack arrows allows for combat to happen
    #checks to see if the card is on the very edge of the board
    def outerInterface(self, number, cards):
        limitMax = self.size-1
        #x and y = 0 means very top of the grid
        if number == 0 and cards.x!=0 and cards.y!=0:
            return False
        elif number == 1 and cards.y!=0:
            return False
        elif number == 2 and cards.x!=limitMax and cards.y!=0:
            return False
        elif number == 3 and cards.x!=limitMax:
            return False
        elif number == 4 and cards.x!=limitMax and cards.y!=limitMax:
            return False
        elif number == 5 and cards.y!=limitMax:
            return False
        elif number == 6 and cards.x!=0 and cards.y!=limitMax:
            return False
        elif number == 7 and cards.x!=0:
            return False
        return True
        

#################################################################################################
    def battlePhase(self, cards):
        battle = []
        for number in cards.arrows.keys():
            #if there is an arrow with an attack number(0 to 7)
            if cards.arrows[number] == 1 and not self.outerInterface(number, cards):
                X = getX(number, cards.x)
                Y = getY(number, cards.y)
                #[X][Y] was originally [Y][X]
                if self.board[Y][X].placed and self.get(X, Y).player != cards.player:
                    if self.get(X, Y).arrows[(number+4)%8]==1:
                        battle.append(number)
        return battle

##########################################################################################################
    
##########################################################################################################
    #surrounded function deals with when a card is fighting more than one card at once
    #surrounded only happens after battle has already taken place
    #it is the function that causes a chain reaction of colour changes
    def Surrounded(self, cards, MapGrid):
        Deckcard = []#array for the cards in this chainreaction
        for number in cards.arrows.keys():#for the numbers(arrows) inside the cards
            if cards.arrows[number] == 1 and not self.outerInterface(number, cards): #I think this means card arrows are pointing at each other
                X = getX(number, cards.x)#checks if it's both by X coordinate
                Y = getY(number, cards.y)#checks if it's both by Y coordinate
                if self.board[Y][X].placed and self.get(X,Y).player != cards.player:
                    Deckcard.append([self.get(X,Y), self.get(X,Y).colour])
                    self.get(X,Y).playerSwitch(cards.player, cards.colour)
        for i in range(1,6):
            for Deckcards in Deckcard:
                Deckcards[0].colour = Deckcards[1]
            time.sleep(actionTime) #animationTime may be redunent better see if you gotta drop it
            self.DrawBoard(MapGrid)
            for Deckcards in Deckcard:
                #changes enemy cards colour when defeated
                Deckcards[0].colour = cards.colour
            time.sleep(actionTime)
            self.DrawBoard(MapGrid)

###########################################################################################################
    def strike(self, cards):
        for number in cards.arrows.keys():
            if cards.arrows[number] == 1 and not self.outerInterface(number, cards):
                X = getX(number, cards.x)
                Y = getY(number, cards.y)
                if self.board[Y][X].placed and self.get(X,Y).player != cards.player:
                    if self.get(X,Y).arrows[(number+4)%8]==0:
                        self.get(X,Y).playerSwitch(cards.player, cards.colour)

###########################################################################################################
    def playPhase(self, cards, X, Y, MapGrid):
        if not (self.board[Y][X].placed or self.board[Y][X].beaten):
            self.board[Y][X].add(cards)
            cardStatus = True
            battle = self.battlePhase(cards)
            while len(battle)!=0:
                if len(battle)>1:
                    print (battle)
                    #this line appears to let the user pick which card to fight first
                    #this will be removed or adjusted to based on the first player card played first
                    number = self.pickEnemyCard(MapGrid, battle, cards)
                elif len(battle) == 1:
                    number = battle[0]

                if number in battle:
                    X = getX(number, cards.x)
                    Y = getY(number, cards.y)
                    cardStatus = cards.battle(self.get(X,Y), self, MapGrid)
                    # combos
                    if cardStatus:
                        self.Surrounded(self.get(X,Y), MapGrid) 
                        battle = self.battlePhase(cards)
                    else:
                        self.Surrounded(cards, MapGrid)
                        battle = []

                else :
                    print ("you must choose a card to fight")############change
            # attacks
            if cardStatus:
                self.strike(cards)
            self.finalizeScore()
            return True    
        else :
            print ("This atHolder is placed or beaten.")##############change
            self.finalizeScore()
            return False
#################################################################################################
    #determine if you've made a distiction between player and players
    #I think this is the first time I've seen players better double check
    #might be best to turn it into plyrz for the sake of differentation 
    def finalizeRounds(self, MapGrid):
        winner = self.player[0]###############
        for player in self.player:
            if player.score > winner.score:
                winner = player
        if winner.score > 5:
            winner.round = winner.round +1 #oringinally +1 if doesn't work fix
            #this line allows for the player to restart the game into a new round
            #i would like to change this so that it creates a menu to ask if they want a new round or to quit
            retryBtn("The Player " + winner.name + " is the winner.", MapGrid)


#################################################################################################
    def finalizeScore(self): ###
        for player in self.player:#this was previously self.players
            player.score = 0
        for line in self.board:
            for atHolder in line:
                if atHolder.placed:
                    for player in self.player:
                        if atHolder.inside.player == player.number:
                            player.score = player.score+1

#################################################################################################
    def pickEnemyCard(self, MapGrid, battle, cards):
        #find the card
        self.DrawBoard(MapGrid)
        #creates an array for cards in battle
        fightAllAtOnce = []
        for number in battle:
            X = getX(number, cards.x)
            Y = getY(number, cards.y)
            fightAllAtOnce.append([self.get(X,Y), number])

        for cardValue in fightAllAtOnce:
            pickFight = cardValue[0]
            pygame.draw.rect(MapGrid, red, pygame.Rect(pickFight.px, pickFight.py, cardWidth, cardHeight), 2)
        pygame.display.flip()
        selectedOpponentCard = False
        number = None
        while not selectedOpponentCard:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    click_X = event.pos[0]
                    click_Y = event.pos[1]
                    for cardValue in fightAllAtOnce:
                        pickFight = cardValue[0]
                        if pickFight.CardIsClickedOn(click_X,click_Y):
                            selectedOpponentCard = True
                            number = cardValue[1]
        return number
#################################################################################################
    #this function determines what to do if both players hands are empty
    #currently the program just restarts the game or moves to another level
    #I will be changing this in the future to just give out another hand
    def emptyHand(self):
        for player in self.player:
            if not len(player.cards)==0:
                return False
        return True

#################################################################################################
    #not fully sure what this does
    #possibly end the program once two rounds are won?
    def winStateScenario(self, MapGrid):
        for player in self.player:
            if player.round == 2:
                return True
        return False
#################################################################################################
    
    def DrawBoard(self, MapGrid):
        MapGrid.fill(white)
        #turns out to be reduntant but good practice for frame of reference
        #pygame.draw.rect(MapGrid, red, pygame.Rect(0, 0, cardWidth, cardHeight), 2)
        
        #creates outer rectangle that contains the other rectangles
        pygame.draw.rect(MapGrid, black, pygame.Rect(140, 97, 4 * (cardWidth + 62.3) + 3, 4 * (cardHeight + 10) + 3), 2)

        #allows for grid to be created
        #see atHoldler for details
        for line in self.board:
            for atHolder in line:
                if not atHolder.beaten:
                    #determines the location for the outline for the map board 
                    pygame.draw.rect(MapGrid, black, pygame.Rect(143 + (atHolder.x) * (cardWidth + 10), 100 + (atHolder.y) * (cardHeight + 10), cardWidth + 6, cardHeight + 6), 2)
                if atHolder.placed:
                    atHolder.inside.draw(MapGrid)

        #range of handCards is the number of outlines for card placers in hand
        for handCards in range(0,6):
            
            #creates black outlines to show where player's hand is
            pygame.draw.rect(MapGrid, black, pygame.Rect(50, 50 + handCards * (cardHeight + 10), cardWidth + 6, cardHeight + 6), 2)
            pygame.draw.rect(MapGrid, black, pygame.Rect(650, 50 + handCards * (cardHeight + 10), cardWidth + 6, cardHeight + 6), 2)

        #randomList = random.sample(range(5),5)
        for player in self.player:
			#for i in randomList:
			#	cards = player.cards[i]
        	#	cards.draw(MapGrid)
            for cards in player.cards:
            	cards.draw(MapGrid)#draws inside mapgrid
            	
        scoreTracker = pygame.font.SysFont("monospace", 20).render(
            self.player[0].name + " " + str(self.player[0].score) + "  /  " + str(self.player[1].score) + " " +
            self.player[1].name, 10, black)
        roundsTracker = pygame.font.SysFont("monospace", 20).render(
            self.player[0].name + " " + str(self.player[0].round) + "  /  " + str(self.player[1].round) + " " +
            self.player[1].name, 10, black)
        #determines location of graphics inside pygame window
        MapGrid.blit(scoreTracker, (250, 80))
        MapGrid.blit(roundsTracker, (250, 50))
        pygame.display.update()#displays
            
