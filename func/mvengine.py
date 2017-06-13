import win32con, win32api
#Engine that runs mouse movement

rect = None

#Sets up the window rectangle
def setup(rectangle):
	global rect
	rect = rectangle

#Clicks the screen at the specified coordinates of the screen
def click(x, y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def rclick(x, y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

def rclickt(x, y, board):
	rclick(board[x,y].scr_coord[0]+3, board[x,y].scr_coord[1]+3) #Off set by +3 for more accuracy

#Clicks the tile associated with the board data structure position
def clickt(x, y, board):
	click(board[x,y].scr_coord[0]+3, board[x,y].scr_coord[1]+3) #Off set by +3 for more accuracy

def movet(x, y, board):
	move(board[x,y].scr_coord[0]+3, board[x,y].scr_coord[1]+3)	#Off set by +3 for more accuracy

#Moves the mouse to the specified coordinate of the screen
def move(x, y):
	win32api.SetCursorPos((x,y))

#Resets the game by pressing the smiley button in the middle of the window
def game_reset():
	x = int((rect[2]+rect[0])/2)
	y = rect[1]+75
	click(x,y)
