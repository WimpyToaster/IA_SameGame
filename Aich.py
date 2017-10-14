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


def board_find_groups(board):
	result = []
	temp = False
	for y in range(len(board)):
		for x in range(len(board[0])):
			for z in range(len(result)):
				if [x,y] in result[z]:
					temp = True
			if not(temp):
				result.append( board_aux_find_group(board, [], x, y, board[y][x]) );
	return result

def board_aux_find_group(board, curList, x, y, color):
	if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
		return curList

	if (board[y][x] == color) and not([x,y] in curList):
		# UP
		curList.append([x,y])
		print(curList)
		print
		print
		print

		if not([x, y-1] in curList):
			print("UP")
			curList.extend( board_aux_find_group(board, curList, x, y-1, color) )
		# DWN
		if not([x, y+1] in curList):
			print("DWN")
			curList.extend( board_aux_find_group(board, curList, x, y+1, color) )
		# LFT
		#print([x-1, y] in curList)
		if not([x-1, y] in curList):
			print("LFT")
			curList.extend( board_aux_find_group(board, curList, x-1, y, color) )
		# RGT
		#print([x+1, y] in curList)
		if not([x+1, y] in curList):
			print("RGT")
			curList.extend( board_aux_find_group(board, curList, x+1, y, color) )


	return curList

board = [[2,2,1,2,1],[2,2,2,1,2],[1,2,1,2,1],[2,1,2,1,2]]

a = [[1,2]]
#print([1,2] in a)


board_find_groups(board)