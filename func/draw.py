import wx

from func.errors.errors import IllegalColorError

#Draws stuff directly to the screen without the need of another window
class Pen():
	def __init__(self):
		self.app = wx.App(False)
		self.dc = wx.ScreenDC()
		self.dc.Pen = wx.Pen("#FF0000")

	#Mainly for debugging purposes
	def draw_point(self, x ,y):
		self.dc.DrawPoint(x,y)

	#Draws a cross in the center of the tile with the upper left coordinates of (x,y)
	def draw_off_centered_cross(self, x, y):
		centerX = x + 7
		centerY = y + 7

		#Draws vertical line first then horizontal
		for currY in range(centerY - 7, centerY + 8):
			self.dc.DrawPoint(centerX, currY)
		for currX in range(centerX - 7, centerX + 8):
			self.dc.DrawPoint(currX, centerY)

	#Draws a cross centered at (x,y)
	def draw_centered_cross(self, x, y):
		#Draws vertical line first then horizontal
		for currY in range(y - 7, y + 8):
			self.dc.DrawPoint(x, currY)
		for currX in range(x - 7, x + 8):
			self.dc.DrawPoint(currX, y)

	#Draws a line from the center of the tile cornered by (origin_x, origin_y)
	#	to the respective tile indicated by (dest_x, dest_y). Works similarly to
	#	draw_off_centered_cross(self, x, y)
	def draw_off_centered_line(self, origin_x, origin_y, dest_x, dest_y):
		self.dc.DrawLine(origin_x + 7, origin_y + 7, dest_x + 7, dest_y + 7)

	#Draws a line from (origin_x, origin_y) to (dest_x, dest_y)
	def draw_centered_line(self, origin_x, origin_y, dest_x, dest_y):
		self.dc.DrawLine(origin_x, origin_y, dest_x, dest_y)

	#Takes in a 3-Tuple and sets the new color of the pen to the color defined by the tuple
	def set_color_to(self, new_color):
		self.dc.Pen.SetColour(new_color)

	#Takes in a 3-byte hexadecimal and sets the new color of the pen to the color defined by the hex value
	def set_colorh_to(self, new_color_hex):
		if new_color_hex[0] != '#':
			raise IllegalColorError

		rval = int(new_color_hex[1:2], 16)
		gval = int(new_color_hex[3:4], 16)
		bval = int(new_color_hex[5:6], 16)
		self.dc.Pen.SetColour((rval, gval, bval))

	#Changes color of pen forwards in the rainbow
	def change_color(self):
		curr_color = self.dc.Pen.GetColour()[:-1]
		section = self._get_color_section(curr_color)
		if section == 0:
			curr_color = self.mut_3tuple(curr_color, 1, 51)
		elif section == 1:
			curr_color = self.mut_3tuple(curr_color, 0, -51)
		elif section == 2:
			curr_color = self.mut_3tuple(curr_color, 2, 51)
		elif section == 3:
			curr_color = self.mut_3tuple(curr_color, 1, -51)
		elif section == 4:
			curr_color = self.mut_3tuple(curr_color, 0, 51)
		elif section == 5:
			curr_color = self.mut_3tuple(curr_color, 2, -51)
		else:
			pass

		# self.dc.Pen.SetColour(wx.Colour(curr_color))
		self.dc.SetPen(wx.Pen(wx.Colour(curr_color)))
		print("new color " + str(self.dc.Pen.GetColour()[:-1]))
		return curr_color

	#Inputs a tuple, an index of the tuple to be changed, and the change amount and returns
	#	a mutated tuple
	def mut_3tuple(self, tuple, change_index, change):
		tup_list = []
		for val in tuple:
			tup_list.append(val)
		for index in range(0,3):
			if index == change_index:
				tup_list[index] += change
		return (tup_list[0], tup_list[1], tup_list[2])

	#Partitions the ranges of colors and its changes in the rainbow depending on which rgb value changes and
	#	which stays still
	def _get_color_section(self, color_tuple):
		if color_tuple[0] == 255 and color_tuple[1] >= 0 and color_tuple[1] <= 255 and color_tuple[2] == 0:
			if color_tuple[1] == 255:
				return 1
			return 0
		elif color_tuple[1] == 255 and color_tuple[0] >= 0 and color_tuple[0] <= 255 and color_tuple[2] == 0:
			if color_tuple[0] == 255:
				return 2
			return 1
		elif color_tuple[1] == 255 and color_tuple[2] >= 0 and color_tuple[2] <= 255 and color_tuple[0] == 0:
			if color_tuple[2] == 255:
				return 3
			return 2
		elif color_tuple[2] == 255 and color_tuple[1] >= 0 and color_tuple[1] <= 255 and color_tuple[0] == 0:
			if color_tuple[1] == 255:
				return 4
			return 3
		elif color_tuple[2] == 255 and color_tuple[0] >= 0 and color_tuple[0] <= 255 and color_tuple[1] == 0:
			if color_tuple[0] == 255:
				return 5
			return 4
		elif color_tuple[0] == 255 and color_tuple[2] >= 0 and color_tuple[2] <= 255 and color_tuple[1] == 0:
			if color_tuple[2] == 255:
				return 0
			return 5
		else:
			pass

	#Clears the screen
	def clear(self):
		self.dc.Clear()
		self.dc.Clear()