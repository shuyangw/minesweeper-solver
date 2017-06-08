import numpy as np

#Structure to support a 2x2 board
class Node:
	#Constructor:
	#	Type of node, i.e. -1 for unexplored, 0 for empty and explored and
	#		1-8 for numbering
	#	scr_coord, coordinate on the display
	#	b_coord, coordinate on the board structure
	def __init__(self, type, scr_coord, b_coord):
		self.type = type
		self.scr_coord = scr_coord
		self.b_coord = b_coord
