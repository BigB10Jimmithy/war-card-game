import random

class AI(object):
	def __init__(self):
		self.currBoardState  = [[0]*7 for i in range(7)]
		self.nextMoveOptions = {}
		
	def getOpponentMoves(self,opponentMoves):
		self.opponentMoves = opponentMoves
		for card in self.opponentMoves:
			print(card.y,card.x,card.number,card.arrows)#tells whhere the players card is
			#row = self.currBoardState[card.y]
			#row[card.x] = 1
			self.currBoardState[card.y][card.x] = 1
		#print('current board',self.currBoardState)
		
		self.getAvailableCells()
		print('Available Moves\n',self.nextMoveOptions)#prints available places the ai's card can be placed next to the user's card 

	#this function is checking if a nahbouring position on the board is available
	def getAvailableCells(self):
		self.nextMoveOptions.clear()
		for i in range(7):#i checks the rows
			for j in range(7):#j checks the collums
				if(self.currBoardState[i][j] == 1):
					print('Opponent card position',i,j)
					if(i>0 and j>0):	#top left
						if(self.currBoardState[i-1][j-1] == 0):
							self.nextMoveOptions[(i-1,j-1)]  = 1
					if(i>0):	#top 
						if(self.currBoardState[i-1][j] == 0):
							self.nextMoveOptions[(i-1,j)] =1 
					if(i>0 and j<6):	#top right
						if(self.currBoardState[i-1][j+1] == 0):
							self.nextMoveOptions[(i-1,j+1)] = 1 #this indicates that the card is at the position it can detect the top right position
					if(j<6):	#Right
						if(self.currBoardState[i][j+1] == 0):
							self.nextMoveOptions[(i,j+1)] = 1
					if(i<6 and j<6):	#Bottom RIght
						if(self.currBoardState[i+1][j+1] == 0):
							self.nextMoveOptions[(i+1,j+1)] = 1
					if(i<6):	#Bottom
						if(self.currBoardState[i+1][j] == 0):
							self.nextMoveOptions[(i+1,j)] = 1
					if(i<6 and j>0):	#Bottom left
						if(self.currBoardState[i+1][j-1] == 0):
							self.nextMoveOptions[(i+1,j)] = 1
					if(j>0):	#left
						if(self.currBoardState[i][j-1] == 0):
							self.nextMoveOptions[(i,j-1)] = 1
	def makeMove(self):
		choice = random.randrange(0,len(self.nextMoveOptions.keys()))
		key = list(self.nextMoveOptions.keys())[choice]
		X,Y = key
		self.currBoardState[X][Y] = 1#shows the ai's own cards position on the board
		return key



