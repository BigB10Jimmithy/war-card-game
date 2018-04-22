import pygame
from sys import exit
from player import *
from board import *

pygame.init()
pygame.display.set_caption("Dark ")
MapGrid = pygame.display.set_mode((800, 800))
MapGrid.fill(white)
pygame.key.set_repeat(400, 30)

clock = pygame.time.Clock()

###################################################################################

def startNewRound(mapChart):
    for player in mapChart.player:
        player.handReset()
    return Board(7, mapChart.player)

#This function deals with what can be interacted with inside the game board grid
def mouseOverBoard(x, y):#mouseOverBoard 
    #helps determine the location of places the cards can be placed on the grid
    #must match with other coordinates clicked_x and px
    return x > 145 and x < 145 + (cardWidth + 10) * 7 and y > 103 and y < 103 + (cardHeight + 10) * 7

def gamePlay():
    #line seems to load actual game screen double
    #mapChart Board determines the number of squares on the board
    mapChart = Board(7, [Player("Player", 1, purple), Player("ps", 2, blue)])
    cursor_x = 0
    cursor_y = 0
    playersCard = None #refered to in class player, function cardPick
    clicked = False
    gamePlay = 1
    
    #DrawBoard = drawGame, refered to in board, function of the same name
    mapChart.DrawBoard(MapGrid)

###############pygame rendering#############################################
    while gamePlay:#while gameplay is active
        
        for event in pygame.event.get():
            
            if event.type == QUIT:#set to allow user to quit pygame program
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEMOTION:
                cursor_x = event.pos[0]
                cursor_y = event.pos[1]

                if (clicked and mouseOverBoard(cursor_x, cursor_y)):
                    
                    clicked_x = 145 + int((cursor_x - 145) / (cardWidth + 10)) * (cardWidth + 10)
                    clicked_y = 103 + int((cursor_y - 103) / (cardHeight + 10)) * (cardHeight + 10)
                    #doesn't seem to change colour, might not work
                    #pygame.draw.rect(MapGrid, red, pygame.Rect(clicked_x, clicked_y, cardWidth, cardHeight), 2)

            #mouse button event for when the user clicks on an area on screen
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:#if button is equal to one
                    click_x = event.pos[0]
                    click_y = event.pos[1]
                    
                    clicked = mapChart.curPlayer.cardPick(click_x, click_y)
                    playersCard = mapChart.curPlayer.getSelectedCard();

                    if (clicked and mouseOverBoard(click_x, click_y)):
                        #########203
                        X = int((click_x - 143) / (cardWidth + 10))
                        Y = int((click_y - 103) / (cardHeight + 10))
                        card = mapChart.curPlayer.getCard(playersCard.number)
                        #this line seems to only come in play when a card in the players hand is placed on the grid
                        cardPlayed = mapChart.playPhase(card, X, Y, MapGrid)
                        if not cardPlayed:
                            mapChart.curPlayer.addCard(card)
                        else:
                            clicked = False
                            playersCard = None
                            mapChart.NextPlayerTurn()

            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                print("no idea what this does")

        mapChart.DrawBoard(MapGrid)

        label = pygame.font.SysFont("monospace", 20).render(str(mapChart.curPlayerNum), 10, black)
        MapGrid.blit(label, (10, 200))

        pygame.display.flip()

        if (mapChart.emptyHand()):
            #this was previously finalizeScore, caused an error changed it to finalizeRounds
            mapChart.finalizeRounds(MapGrid)#######

            if mapChart.winStateScenario(MapGrid):
                gamePlay = 0
                break;
############################################
            mapChart = startNewRound(mapChart)

def Quit():
    pygame.quit()
    quit()

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        MapGrid.fill(white)
        btn(MapGrid, "Start Game", 50, 50, 200, 100, blue, red, gamePlay )



        btn(MapGrid, "Quit", 50, 500, 200, 100, grey, brown, Quit)

        pygame.display.update()
        clock.tick(15)

game_intro()
        
                            
                    

