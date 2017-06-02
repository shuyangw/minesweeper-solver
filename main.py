from func import adjmattest, screen
from client import gui

import os

if __name__ == "__main__":
	tilepixels, screenpixels = screen.acquireRGBMatrices()
	print(len(tilepixels))
	print(len(screenpixels))
