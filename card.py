from tools import *

class Card(object):
    #things to figure out
    #what does n represent
    ####previous error was fixed by changing attribute color to colour
    #initiate the attributes such as card health and arrows
    def __init__(self, n, player, number, colour):
        self.number = number
        self.x = None
        self.y = None
        self.px = 53 + (player-1)*600#location places the card hand graphics on screen
        self.py = 53 + (number-1)*(cardHeight+10)
        self.player = player
        self.colour = colour
        self.name = str(self.number) + str(self.player)[0]
        self.arrows = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
        self.HP = 20-2*n #HP is 20 - 2 X n (what is n)
        self.maxHP = self.HP
        self.clickedCard = False #refered to in Player
        arrowNum = 0
        #this appears to create a random amount of arrows on a card
        while arrowNum != n:
            random = randint(0, 7)
            if self.arrows[random]==0:
                arrowNum += 1
                self.arrows[random]=1

    #function for card to be selectable
    def CardIsClickedOn(self, x, y):#CardIsClickedOn = isClickedon
        return x >= self.px and x <= self.px + cardWidth and y >= self.py and y <= self.py + cardHeight
    #function player establish player and colour code
    #this function also also necessary for allowing players to change
    def playerSwitch(self, player, colour):#playerSwitch = changePlayer
        self.player = player
        self.colour = colour
        
    #function for the status of a card that has changed sides once beaten
    def respawn(self):
        self.HP = (self.maxHP)/2
        
    def battle(self, cardTwo, mapChart, MapGrid):
        print (self.name + " in battle with " + cardTwo.name)
        strike = True
        if not (self.player==cardTwo.player):#if card 2 is not the same as player's card then
            while(self.HP != 0 and cardTwo.HP != 0 ):#while card's or card 2's hp isn't 0 then
                if(strike):#if in strike(attack)
                    cardTwo.HP -= 1#reduce card 2's hp by 1
                    
                    strike = not strike#I think this means stop the strike attribute

                    time.sleep(0.1)#time this should  take

                    mapChart.DrawBoard(MapGrid)#don't know but I think this means send data to mapchart DrawBoard
                else:
                    self.HP -= 1#reduce the player's card by 1

                    strike = not strike 

                    time.sleep(actionTime) #time this should take

                    mapChart.DrawBoard(MapGrid)
            if self.HP == 0:#if self's health reaches 0 then
                self.respawn()#set up the respawn
                self.playerSwitch(cardTwo.player, cardTwo.colour)#this swtiches the losing card's colour
                time.sleep(actionTime)#how long this takes
                mapChart.DrawBoard(MapGrid)
                return False#not sure what this is for
            else:
                cardTwo.respawn()
                cardTwo.playerSwitch(self.player, self.colour)
                time.sleep(actionTime)
                mapChart.DrawBoard(MapGrid)
                return True

    #not sure what getName does but it seems to allow for the cards to function            
    def getName(self):
        #what is zfill? double check?
        return self.name + "(" + str (self.HP).fill(2) + "/" + str(self.maxHP).fill(2) + self.player

######################################################################################

    #also try and sort it so that you reload a new hand when exhausting all the cards
    #function for creating the graphic of the card and what it'll will all contain
    def draw(self, MapGrid):
        #this creates the actual coloured card,
        pygame.draw.rect(MapGrid, self.colour, pygame.Rect(self.px, self.py, cardWidth, cardHeight))

        #this for loop displays the attacks arrows
        for number in self.arrows.keys(): #for numbers inside the arrows attribute

            #arrows[number] has to equal exactly one for card battle to happen
            if (self.arrows[number] == 1):#if statement to check if arrows(number) equals at exactly 1 then
                
                self.createArrwos(MapGrid, number)#allows for arrows to be created once standards are met
                
        #label inside card to display information
        label = pygame.font.SysFont("monospace", 20).render(str(self.HP), 10, white)
        
        #creates and displays information inside the card such as HP number
        MapGrid.blit(label, (self.px + cardWidth / 2-10, self.py + cardHeight / 2-10))

        #if card is clicked on, then it will highllight the card with a red ring
        if self.clickedCard:
            pygame.draw.rect(MapGrid, red, pygame.Rect(self.px, self.py, cardWidth, cardHeight), 3)

#####################################################################################################

    #This seems to create the arrows in the hand
    #the reason its goes up to eight is probably due to the fact that there are eight possible sides the arrow can point
    def createArrwos(self, MapGrid, number):
        if(number == 0):
            X = self.px+2
            Y = self.py+2
            pygame.draw.polygon(MapGrid, red, [[X, Y], [X+5, Y], [X, Y+5]], 0)
        if(number == 1):
            X = self.px + cardWidth / 2
            Y = self.py + 2
            #creates attack arrow pointing up
            pygame.draw.polygon(MapGrid, white, [[X, Y], [X+r2, Y+r2], [X-r2, Y+r2]], 0)
        if(number == 2):
            #X -2 is creates the location on the card, in this case the top right corner
            X = self.px + cardWidth - 2
            Y = self.py + 2
            pygame.draw.polygon(MapGrid, green, [[X, Y], [X-5, Y], [X, Y+5]], 0)
        if(number == 3):
            X = self.px+cardWidth-2
            Y = self.py+cardHeight/2
            pygame.draw.polygon(MapGrid, yellow, [[X, Y], [X-r2, Y+r2], [X-r2, Y-r2]], 0)
        if(number == 4):
            X = self.px+cardWidth-2
            Y = self.py+cardHeight-2
            pygame.draw.polygon(MapGrid, clearblue, [[X, Y], [X-5, Y], [X, Y-5]], 0)
        if(number == 5):
            X = self.px+cardWidth/2
            Y = self.py+cardHeight-2
            pygame.draw.polygon(MapGrid, white, [[X, Y], [X+r2, Y-r2], [X-r2, Y-r2]], 0)
        if(number == 6):
            X = self.px+2
            Y = self.py+cardHeight-2
            pygame.draw.polygon(MapGrid, brown, [[X, Y], [X+5, Y], [X, Y-5]], 0)
        if(number == 7):
            X = self.px+2
            Y = self.py+cardHeight/2
            pygame.draw.polygon(MapGrid, black, [[X, Y], [X+r2, Y+r2], [X+r2, Y-r2]], 0)

###############################################################################################




            
        
    
