import sys
import time

import numpy as np
from PIL import Image

from func.draw import Pen
from func.structures.boardnode import Node
import func.screen as sc
import func.mvengine as mv

#Numpy matrix of the board with dimensions depending on how many tiles there are
board = None

#Dimensions of the board
x_dim = 0
y_dim = 0

#Start coordinates of the playing board
boardStartX = 0
boardStartY = 0

#Matrix of screen pixels and the blank tile pixels respectively
scrp = None
blankp = None

#Found blank tile
found_blank_tile = None

#Array of every tile
tilearr = []

#Pen to draw things with
pen = None

#Prelim:
#	Looping over one of the input matrices results in looping over rows of pixels for each input, i.e., looping over 
#		the correct scrp will render 1080 iterations where each the 1080 iterations will have an entry of length 1920
#	Varies depending on native screen resolution, in general
#		first loop will be over height, while the second will beover length
def prelim_setup(blank_tile_pixels, screenpixels, rect): 
	global pen, blankp, scrp, x_dim, y_dim, boardStartX, boardStartY
	# global blankp
	# global scrp

	blankp = blank_tile_pixels
	scrp = screenpixels
	pen = Pen()

	#WARNING: blankp and scrp are indexed as [y,x]
	#Bottom right pixel of screen is: scrp[1079, 1919]
	appUpX = rect[0]
	appUpY = rect[1]
	appBotX = rect[2]
	appBotY = rect[3]

	countX = 0
	countY = 0
	#	O(n^2) naive search
	for y in range(appUpY, appBotY):
		for x in range(appUpX, appBotX):
			if are_pixels_equal(scrp[y,x], blankp[0,0]) == True: #If detect first pixel of tile
				if confirm_tile(y, x) == True:
					boardStartX, boardStartY = x, y-2 #Correction by -2 not sure why
					print("Detected tile\nDetermining board...")
					countX, countY = determine_board(y, x)
					num_tiles = countX * countY
					pen.clear()
					print("Number of tiles : " +str(num_tiles))
					break
		#Executes if inner loop is ended normally
		else: 
			continue
		#Executes if inner loop is broken
		break
	x_dim, y_dim = countX, countY
	return countX, countY, boardStartX, boardStartY

#Given a starting (y,x) coordinate, checks to see of the 16x16 box starting from (y,x) is the tile
def confirm_tile(beginY, beginX):
	x, y = 0, 0
	for j in range(beginY, beginY + 16):
		for i in range(beginX, beginX + 16):
			if(are_pixels_equal(scrp[j, i], blankp[y, x]) == False):
				return False
			x += 1
			y += 1
			if x == 16 and y == 16:
				return True
	return True

#Given a starting (y,x) coordinate, counts the number of tiles there are on the board
def determine_board(currY, currX):
	#Counting how many there are horizontally and vertically so we can simply return the product as the number of tiles
	countX, countY = 0, 0
	originalY = currY
	originalX = currX
	try:
		#Checks how many tiles there are across
		while(True):
			pen.draw_off_centered_cross(currX, currY)
			time.sleep(0.01)
			if confirm_tile(currY, currX) == True:
				currX += 16
				countX += 1
			else:
				break
		currX = originalX

		#Checks how many tiles there are up to down
		while(True):
			pen.draw_off_centered_cross(currX, currY)
			time.sleep(0.01)
			if confirm_tile(currY, currX) == True:
				currY += 16
				countY += 1
			else:
				break
	except(IndexError):
		print("Please ensure that the complete Minesweeper window is in your main screen and restart")
		sys.exit()
	except:
		print("Unexpected error, please restart Minesweeper and retry")
		sys.exit()

	print("Board determined")
	return countX, countY

#Tests to see if pixels are equal
#Takes in two pixels in the form [RBG, RBG, RBG] and returns a boolean
def are_pixels_equal(p1, p2):
	for i in p1:
		for j in p2:
			if i != j:
				return False
	return True

#Determines if two tiles given as 16x16 numpy matrices are equal
def are_tiles_equal(tile1, tile2):
	flat1 = tile1.flatten()
	flat2 = tile2.flatten()
	for i in range(256):
		if flat1[i] != flat2[i]:
			return False
	return True

#Same as are_tiles_equal but leaves a +- 16 valuess of error
def are_tiles_equal_err(tile1, tile2):
	flat1 = tile1.flatten()
	flat2 = tile2.flatten()
	for i in range(256):
		if flat1[i] != flat2[i]:
			if(abs(flat1[i]-flat[2]) > 16):
				return False
	return True

#Extracts the tile rooted at the screen coordinates (x,y)
def extr_tile(x, y):
	return scrp[y:y+16,x:x+16]	

#Initializes the board data structure with an arbitrary node
def init_board(x_dim, y_dim):
	global board
	board = np.empty((x_dim, y_dim), dtype = object)
	for j in range(y_dim):
		for i in range(x_dim):
			if i == x_dim or j == y_dim:
				return
			board[i,j] = Node(-2, None)

#Reparses the minesweeper board to collect new information
def reparse():
	savedir = sc.screenshot()
	global scrp
	scrp = sc.parse_screen_bmp(savedir) 
	currX = boardStartX
	currY = boardStartY
	for j in range(y_dim):
		currX = boardStartX
		for i in range(x_dim):
			curr_tile = extr_tile(currX, currY)
			pen.draw_point(i, j)
			t_type = get_tile_type(curr_tile)
			if t_type == -1:
				board[i, j] = Node(-1, (currX, currY))
			elif t_type == 0:
				board[i, j] = Node(0, (currX, currY))
			elif t_type != -2:
				board[i, j] = Node(t_type, (currX, currY))
			else:
				print("Err")
			currX += 16
		currY += 16
	return board

def acquire_aux_files():
	global found_blank_tile, tilearr
	found_blank_tile = sc.parse_tile_png("b.png")
	tilearr.append(sc.parse_tile_png("1.png"))
	tilearr.append(sc.parse_tile_png("2.png"))
	tilearr.append(sc.parse_tile_png("3.png"))
	tilearr.append(sc.parse_tile_png("4.png"))
	tilearr.append(sc.parse_tile_png("5.png"))
	tilearr.append(sc.parse_tile_png("6.png"))
	tilearr.append(sc.parse_tile_png("7.png"))
	tilearr.append(sc.parse_tile_png("8.png"))

#Prints the state of the board, the data associated with it and their coordinates
def print_state():
	for j in range(y_dim):
		for i in range(x_dim):
			if len(str(board[i,j].type)) == 1:
				print("("+str(i)+","+str(j)+")"+ " " +str(board[i,j].type)+",        ", end="")
			else:
				print("("+str(i)+","+str(j)+")"+ " " +str(board[i,j].type)+",       ", end="")
		print()

#Returns the type of tile
#	-1 if it's an explored tile
#	0 if it's an explored tile
#	the number of the tile if it's a numbered tile
#   -2 if there is an error 
def get_tile_type(tile):
	if are_tiles_equal(tile, blankp):
		return -1
	elif are_tiles_equal(tile, found_blank_tile):
		return 0
	else:
		for i in range(1,9):
			if are_tiles_equal(tile, tilearr[i-1]):
				return i
	return -2

def setup_board(blank_tile_pixels, screenpixels, rect):
	x_dim, y_dim, boardStartX, boardStartY = prelim_setup(blank_tile_pixels, screenpixels, rect)
	init_board(x_dim, y_dim)
	acquire_aux_files()
	mv.move(rect[0] - 10, rect[1] - 10)
	return x_dim, y_dim, boardStartX, boardStartY