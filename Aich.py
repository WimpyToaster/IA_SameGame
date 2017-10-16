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
			if not(checkIn(make_pos(x, y), result)):
				result.append( board_aux_find_group(board, [], x, y, board[y][x]) );
	return result

def board_aux_find_group(board, curList, x, y, color):
	if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
		return curList

	if (board[y][x] == color) and not(make_pos(x, y) in curList):
		# UP
		curList.append(make_pos(x, y))
		print(curList)
		print
		print
		print

		if not(make_pos(x, y-1) in curList):
			print("UP")
			curList = board_aux_find_group(board, curList, x, y-1, color)
		# DWN
		if not(make_pos(x, y+1) in curList):
			print("DWN")
			curList = board_aux_find_group(board, curList, x, y+1, color)
		# LFT
		#print([x-1, y] in curList)
		if not(make_pos(x-1, y) in curList):
			print("LFT")
			curList = board_aux_find_group(board, curList, x-1, y, color)
		# RGT
		#print([x+1, y] in curList)
		if not(make_pos(x+1, y) in curList):
			print("RGT")
			curList = board_aux_find_group(board, curList, x+1, y, color)


	return curList


def board_remove_move_side(board):
 
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
 				for x in range(ult_linha  1):
 					board[x][y] = board[x][y+i]
 					board[x][y+i] = 0
 				break
 					
 		
 	return board
 
 
 
 def print_board(board):
 
 	for x in range( len(board) ):
 		for y in range( len(board[0]) ):
 			print(board[x][y], end=' ')
 		print()
		
		
board = [[2,2,1,2,1],[2,2,2,1,2],[1,2,1,2,1],[1,1,1,0,0	]]

a = [[1,2]]
#print([1,2] in a)

print("hello")
#print board_find_groups(board)
print("ended")

def printboard(board):
	for x in board:
		print x


def board_gravity(board):
	for x in range(len(board[0])):
		i = len(board) - 2
		while i >= 0:
			if(color(board[i][x]) and no_color(board[i+1][x])):
				board[i+1][x] = board[i][x]
				board[i][x]   = get_no_color()
			i -= 1
	return board
printboard(board)
print
printboard(board_gravity(board))



class sg_state:

	def __init__(self, board):
		this.board = board
