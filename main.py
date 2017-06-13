from func import screen
from client import gui
from func.structures.boardnode import Node
from func.draw import Pen

from func import mvengine as mv
from func import command as cmd
from func import solver as sol
from func import board as bd

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
	x_dim, y_dim, boardStartX, boardStartY = bd.setup_board(tilepixels, screenpixels, rect)
	board = bd.reparse()

	print("Begin Phase 3")
	# print(board[5,5].scr_coord[0]+3)
	# mv.clickt(0,0, board)
	# mv.clickt(9,9, board)

	print_elapsed_time()
	sol.update_board(x_dim, y_dim)
	cmd.on()

	