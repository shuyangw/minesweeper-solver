from func import adjmattest, screen, search
from client import gui

import time
import os

if __name__ == "__main__":
	print("Starting...")

	print("Begin Phase 1: Acquiring screen pixels")
	tilepixels, screenpixels, rect = screen.acquire_rgb_matrices()
	print("End Phase 1")

	print("Begin Phase 2")
	search.get_tile_element(tilepixels, screenpixels, rect)
