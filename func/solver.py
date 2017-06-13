import numpy as np
import func.mvengine as mv

import random, time

from func import board as b
from func.errors.errors import EmptyBoardError

#Entire board
board = None
notouch = None
x_dim = 0
y_dim = 0

bool = True

#Move number
move_num = 0

#Self explanatory
def update_board(x, y):
	global board, x_dim, y_dim
	board = b.reparse()
	x_dim = x
	y_dim = y

def loop():
	while b.find_conditions() != "win":
		make_move()

#Performs 1 move towards possible victory
def make_move():
	global move_num, board, notouch, bool
	board = b.reparse()
	notouch = np.zeros((y_dim, x_dim), dtype = int)

	if move_num == 0:
		rand()
		move_num += 1
		return

	if bool:
		count = 0
		for y in range(y_dim):
			for x in range(x_dim):
				if board[x,y].type != -1:
					count += 1
		if count <= 8:
			rand()
			move_num += 1
			return
		else:
			bool = False
			return

	for y in range(y_dim):
		for x in range(x_dim):
			if board[x,y].type == 1:
				strat1(board[x,y])
				strat2(board[x,y])
			if board[x,y].type == 2:
				strat2_mod(board[x,y])

def strat1(n):
	global board
	adjacents = adj(n)
	count = 0
	for node in adjacents:
		if node.type == -1:
			count += 1
		if node.type == "f":
			return
	if count == 1:
		for node in adjacents:
			if node.type == -1 and notouch[node.b_coord[1], node.b_coord[0]] == 0:
				mv.rclickt(node.b_coord[0], node.b_coord[1], board)
				notouch[node.b_coord[1], node.b_coord[0]] = 1

def strat2(n):
	adjacents = adj(n)
	count = 0
	for node in adjacents:
		if node.type == "f":
			count += 1
	if count == 1:
		for node in adjacents:
			if node.type == -1 and notouch[node.b_coord[1], node.b_coord[0]] == 0:
				mv.clickt(node.b_coord[0], node.b_coord[1], board)
				notouch[node.b_coord[1], node.b_coord[0]] = 1

def strat2_mod(n):
	adjacents = adj(n)
	count = 0
	for node in adjacents:
		if node.type == "f":
			count += 1
	if count == 2:
		for node in adjacents:
			if node.type == -1 and notouch[node.b_coord[1], node.b_coord[0]] == 0:
				mv.clickt(node.b_coord[0], node.b_coord[1], board)
				notouch[node.b_coord[1], node.b_coord[0]] = 1

def rand():
	randX = random.randint(0, x_dim-1)
	randY = random.randint(0, y_dim-1)
	mv.clickt(randX, randY, board)

def adj(node):
	ret = []
	if node.b_coord[0]-1 >= 0:
		ret.append(board[node.b_coord[0]-1, node.b_coord[1]])
		if node.b_coord[1]-1 >= 0:
			ret.append(board[node.b_coord[0]-1, node.b_coord[1]-1])
		if node.b_coord[1]+1 < y_dim:
			ret.append(board[node.b_coord[0]-1, node.b_coord[1]+1])
	if node.b_coord[0]+1 < x_dim:
		ret.append(board[node.b_coord[0]+1, node.b_coord[1]])
		if node.b_coord[1]-1 >= 0:
			ret.append(board[node.b_coord[0]+1, node.b_coord[1]-1])
		if node.b_coord[1]+1 < y_dim:
			ret.append(board[node.b_coord[0]+1, node.b_coord[1]+1])
	if node.b_coord[1]-1 >= 0:
		ret.append(board[node.b_coord[0], node.b_coord[1]-1])
	if node.b_coord[1]+1 < y_dim:
		ret.append(board[node.b_coord[0], node.b_coord[1]+1])
	return ret
