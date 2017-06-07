import win32con, win32api

rect = None

def setup(rectangle):
	global rect
	rect = rectangle

def click(x, y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#Clicks the tile associated with the board data structure position
def clickt(x, y, board):
	click(board[x,y].coord[0]+3, board[x,y].coord[1]+3)

def move(x, y):
	win32api.SetCursorPos((x,y))

def game_reset():
	x = int((rect[2]+rect[0])/2)
	y = rect[1]+75
	click(x,y)
