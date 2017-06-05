import sys
import time

import numpy as np
from PIL import Image

from func.draw import Pen
from func.structures.boardnode import Node

scrp = None
tilep = None
pen = None

#Prelim:
#	Looping over one of the input matrices results in looping over rows of pixels for each input, i.e., looping over 
#		the correct scrp will render 1080 iterations where each the 1080 iterations will have an entry of length 1920
#	Varies depending on native screen resolution, in general
#		first loop will be over height, while the second will beover length
def get_tile_element(tilepixels, screenpixels, rect): 
	global pen
	global tilep
	global scrp

	tilep = tilepixels
	scrp = screenpixels
	pen = Pen()

	#WARNING: tilep and scrp are indexed as [y,x]
	#Bottom right pixel of screen is: scrp[1079, 1919]
	appUpX = rect[0]
	appUpY = rect[1]
	appBotX = rect[2]
	appBotY = rect[3]

	countX = 0
	countY = 0

	boardStartX = 0
	boardStartY = 0

	#	O(n^2) naive search
	for y in range(appUpY, appBotY):
		for x in range(appUpX, appBotX):
			if are_pixels_equal(scrp[y,x], tilep[0,0]) == True: #If detect first pixel of tile
				if confirm_tile(y, x) == True:
					boardStartX = x
					boardStartY = y
					print("Detected tile")
					print("Determining board...")
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
	return countX, countY, boardStartX, boardStartY

#Given a starting (y,x) coordinate, checks to see of the 16x16 box starting from (y,x) is the tile
def confirm_tile(beginY, beginX):
	x, y = 0, 0
	for j in range(beginY, beginY + 16):
		for i in range(beginX, beginX + 16):
			if(are_pixels_equal(scrp[j, i], tilep[y, x]) == False):
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

#TODO
# def are_tiles_equal(t1_startX, t1_startY, t2_startX, t2_startY):
# 	for yiter in range(0,16):
# 		for xiter in range(0,16):
# 			if 

#TODO
#Extracts the 16x16 tile as a numpy array with an upper left tile at (t_startX, t_startY)
def extract_tile(t_startX, t_startY):

	tile = np.empty((16,16), dtype = object)

#TODO
def create_board_object(x_dim, y_dim):
	board = np.empty((x_dim, y_dim), dtype = object)
	for i in range(x_dim):
		for j in range(y_dim):
			board[i, j] = None

def get_center_coord(x, y):
	return x + 7, y + 7

def setup_board(tilepixels, screenpixels, rect):
	x_dim, y_dim, boardStartX, boardStartY = get_tile_element(tilepixels, screenpixels, rect)
	board = create_board_object(x_dim, y_dim)