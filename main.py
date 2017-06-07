from func import screen, board
from client import gui
from func.structures.boardnode import Node
from func.draw import Pen

from func import mvengine as mv

import time
import os
import wx


timemilli = 0

def print_elapsed_time():
	print("Elapsed time: " + str((int(round(time.time() * 1000)) - timemilli)/1000.0) + " secs")

if __name__ == "__main__":
	timemilli = int(round(time.time() * 1000))
	print("Starting...")

	print("Begin Phase 1: Acquiring screen pixels")
	tilepixels, screenpixels, rect = screen.acquire_rgb_matrices()
	mv.setup(rect)
	mv.game_reset()
	print("End Phase 1")

	print("Begin Phase 2")
	x_dim, y_dim, boardStartX, boardStartY= board.setup_board(tilepixels, screenpixels, rect)
	board = board.reparse()

	print("Begin Phase 3")
	mv.clickt(0,0, board)
	mv.clickt(9,9, board)

	print_elapsed_time()

	while(True):
		inp = input()
		if inp == "r":
			print("Reparsing...")
			board.reparse()
		if inp == "p":
			board.print_state()
