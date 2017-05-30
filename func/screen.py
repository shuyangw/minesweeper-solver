import os
import sys

import win32gui
import win32api
import win32con
import win32ui

import numpy as np
from PIL import Image

#Input: 	String that denotes the name of a file of an png or bmp
#Output: 	Inserts the RGB values of the image into tilepixels array
def parseTilePng(filename):
	im = Image.open(filename)
	tilepixels = np.array(im)
	return tilepixels
def parseScreenBmp(filename):
	im = Image.open(filename)
	screenpixels = np.array(im)
	return screenpixels

#Prints the RGB values of the current image, 16 pixels per line
def printPixelsRGB():
	try:
		for i in range(256):
			if i % 16 == 0 and i != 0:
				print("\n" + str(tilepixels[i]), end = " ")
			else:
				print(str(tilepixels[i]), end = " ")
		print()
	except(IndexError):
		print("Array of pixels is empty")

#Quite useful
#Input:		String in the window title
#Output:	List of handles for that window. Often of size 1 with just the desired handle
def get_windows_bytitle(title_text, exact = False):
    def _window_callback(hwnd, all_windows):
        all_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    windows = []
    win32gui.EnumWindows(_window_callback, windows)
    if exact:
        return [hwnd for hwnd, title in windows if title_text == title]
    else:
        return [hwnd for hwnd, title in windows if title_text in title]

#Takes screenshot and saves it to the directory denoted in the last line of the function
def screenshot(hwnd = None):
    from time import sleep
    if not hwnd:
        hwnd=win32gui.GetDesktopWindow()

    l,t,r,b=win32gui.GetWindowRect(hwnd)
    h=b-t
    w=r-l
    hDC = win32gui.GetWindowDC(hwnd)
    myDC=win32ui.CreateDCFromHandle(hDC)
    newDC=myDC.CreateCompatibleDC()

    myBitMap = win32ui.CreateBitmap()
    myBitMap.CreateCompatibleBitmap(myDC, w, h)

    newDC.SelectObject(myBitMap)

    #Throws an error for some reason
    # try:
    # 	win32gui.SetForegroundWindow(hwnd)
    # except:
    # 	print("Error with line: win32gui.setForegroundWindow(hwnd)")

    sleep(.2) 
    newDC.BitBlt((0,0),(w, h) , myDC, (0,0), win32con.SRCCOPY)
    myBitMap.Paint(newDC)

    #Save directory for screen bmp in tmp in tmp folder
    savecwd = os.getcwd()[:-15]+"\\tmp\\screen.bmp"

    #Saves the screen bmp
    myBitMap.SaveBitmapFile(newDC, savecwd)
    return savecwd

def setupWindow():
	currenthwndList = get_windows_bytitle("Minesweeper X")

	try:
		#For some reason, there could be two things that could pop up
		#for Minesweeper X
		hwnd = currenthwndList[0]	#hwnd of the Minesweeper window
	except(IndexError):
		print("Error: Window not found. Please launch Minesweeper ensure that it's open")
		sys.exit()

	#Sets window to be in front
	win32gui.SetForegroundWindow(hwnd)

	#Gets upper left corner and bottom right coordinate
	rect = win32gui.GetWindowRect(hwnd)

	#Probably don't need
	appX = rect[2] - rect[0]
	appY = rect[3] - rect[1]

	print(appX, appY)
	print(rect)

def acquireRGBMatrices():
	os.chdir("func\\testfiles")
	setupWindow()
	imageDir = screenshot()
	screenpixels = parseScreenBmp(imageDir)
	tilepixels = parseTilePng("tile.png")
	return tilepixels, screenpixels