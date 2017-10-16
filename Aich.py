from search import Problem

# TAI color 
# sem cor = 0 
# com cor > 0 

def get_no_color(): 
    return 0 
def no_color (c): 
    return c==0 
def color (c): 
    return c > 0 

# TAI pos 
# Tuplo (l, c) 
def  make_pos (l, c): 
    return (l, c)
def pos_l (pos): 
    return pos[0] 
def pos_c (pos): 
    return pos[1]

def checkIn(el, list):
	for x in list:
		if el in x:
			return True
	return False


def board_find_groups(board):
	result = []
	for y in range(len(board)):
		for x in range(len(board[0])):
			if not(checkIn(make_pos(y, x), result)):
				result.append( board_aux_find_group(board, [], y, x, board[y][x]) );
	return result

def board_aux_find_group(board, curList, y, x, color):
	if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
		return curList

	if (board[y][x] == color) and not(make_pos(y, x) in curList):
		# UP
		curList.append(make_pos(y, x))

		if not(make_pos(y-1, x) in curList):
			curList = board_aux_find_group(board, curList, y-1, x, color)
		# DWN
		if not(make_pos(y+1, x) in curList):
			curList = board_aux_find_group(board, curList, y+1, x, color)
		# LFT
		#print([x-1, y] in curList)
		if not(make_pos(y, x-1) in curList):
			curList = board_aux_find_group(board, curList, y, x-1, color)
		# RGT
		#print([x+1, y] in curList)
		if not(make_pos(y, x+1) in curList):
			curList = board_aux_find_group(board, curList, y, x+1, color)


	return curList

def print_board(board):
	for x in board:
		print(x)


def board_gravity(board):
	for x in range(len(board[0])):
		i = len(board) - 2
		while i >= 0:
			if(color(board[i][x]) and no_color(board[i+1][x])):
				board[i+1][x] = board[i][x]
				board[i][x]   = get_no_color()
			i -= 1
	return boarddef board_remove_move_side(board):
 
 	ult_linha = len(board) - 1
 	colunas_zero = []
 	do_it = False
 
 	for i in range(len(board[0])):
 		if (board[ult_linha][i] == 0):
 			do_it = True
 			colunas_zero.append(i)
 
 	if (not do_it):
 		return board
 
 
 	for y in range(colunas_zero[0], ult_linha):
 		for i in range(1, len(board[0]) - y):
 			if (board[ult_linha][y+i] != 0):
 				for x in range(ult_linha + 1):
 					board[x][y] = board[x][y+i]
 					board[x][y+i] = 0
 				break
 					
 		
 	return board
 
	
def board_gravity(board):
	for x in range(len(board[0])):
		i = len(board) - 2
		while i >= 0:
			if(color(board[i][x]) and no_color(board[i+1][x])):
				board[i+1][x] = board[i][x]
				board[i][x]   = get_no_color()
			i -= 1
	return board
 
def board_remove_group(board, group):

	for x in group:
		board[x[0]][x[1]] = 0

	board_gravity(board)
	board_move_side(board)

	return board
 
def print_board(board):
 
 	for x in range( len(board) ):
 		for y in range( len(board[0]) ):
 			print(board[x][y], end=' ')
 		print()
		
def pb(b):
	for x in b:
		print(x)

 		

board = [[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]]



class sg_state:

	def __init__(self, board):
		self.board = board

class same_game(Problem):

	def __init__(self, board):
		Problem.__init__(self, sg_state(board))

	def actions(self, state):
		"""Returns a list of possible actions (groups to pop)"""
		return [x for x in board_find_groups(state.board) if len(x) > 1]

	#def goal_test(self, state):

	#def path_cost(self, c, state1, action, state2):

	#def h(self, node):


print_board( same_game(board).actions(sg_state(board)) )
