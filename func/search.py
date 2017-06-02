import sys

import numpy as np
from PIL import Image

scrp = None
tilep = None

#Prelim:
#	Looping over one of the input matrices results in looping
#		over rows of pixels for each input, i.e., looping over 
#		the correct scrp will render 1080 iterations where each
#		the 1080 iterations will have an entry of length 1920
#	Varies depending on native screen resolution, in general
#		first loop will be over height, while the second will be
#		over length
def get_tile_element(tilepixels, screenpixels, rect): 
	global tilep
	global scrp
	tilep = tilepixels
	scrp = screenpixels

	#WARNING: tilep and scrp are indexed as [y,x]
	#Bottom right pixel of screen is: scrp[1079, 1919]
	appUpX = rect[0]
	appUpY = rect[1]
	appBotX = rect[2]
	appBotY = rect[3]

	print("window rect: " + str(rect))
	#	O(n^2) naive search
	for y in range(appUpY, appBotY):
		for x in range(appUpX, appBotX):
			if arePixelsEqual(scrp[y,x], tilep[0,0]) == True: #If detect first pixel of tile
				if confirm_tile(y, x) == True:
					print("Detected tile")
					print("Determining board...")
					num_tiles = determine_board(y, x)
					print(num_tiles)
					sys.exit()


#Given a starting (y,x) coordinate, checks to see of the 16x16 box starting from (y,x) is the tile
def confirm_tile(beginY, beginX):
	x, y = 0, 0
	for j in range(beginY, beginY + 16):
		for i in range(beginX, beginX + 16):
			if(arePixelsEqual(scrp[j, i], tilep[y, x]) == False):
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
			if confirm_tile(currY, currX) == True:
				currX += 16
				countX += 1
			else:
				break
		currX = originalX

		#Checks how many tiles there are up to down
		while(True):
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

	#Returns product of two
	return countX * countY

#Tests to see if pixels are equal
#Takes in two pixels in the form [RBG, RBG, RBG] and returns a boolean
def arePixelsEqual(p1, p2):
	for i in p1:
		for j in p2:
			if i != j:
				return False
	return True