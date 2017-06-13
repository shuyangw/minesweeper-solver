#Base error class
class Error(Exception):
	pass

class IllegalColorError(Error):
	pass

class EmptyBoardError(Error):
	pass