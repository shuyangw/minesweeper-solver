from func import screen, setboard
from client import gui
from func.structures.boardnode import Node
from func.draw import Pen

import time
import os

timemilli = 0

def print_elapsed_time():
	print("Elapsed time: " + str((int(round(time.time() * 1000)) - timemilli)/1000.0) + " secs")

if __name__ == "__main__":
	timemilli = int(round(time.time() * 1000))

	print("Starting...")

	print("Begin Phase 1: Acquiring screen pixels")
	tilepixels, screenpixels, rect = screen.acquire_rgb_matrices()
	print("End Phase 1")

	print("Begin Phase 2")
	setboard.setup_board(tilepixels, screenpixels, rect)
	pen = Pen()

	print(pen.change_color_by())
	print(pen.mut_3tuple((255,0,255), 1, 51))
	print_elapsed_time()

