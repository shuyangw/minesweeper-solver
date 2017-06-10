from func import screen, board

#Function to run a input command line thing for the sake of debugging
#While loop broken by user input through command line, i.e. something like Ctrl + C
def on():
	while(True):
		inp = input()
		if len(str(inp)) == 1:
			if inp == "r":
				print("Reparsing...")
				board.reparse()
			if inp == "p":
				board.print_state()
		else:
			for i in range(len(str(inp))):
				if inp[i] == "r":
					print("Reparsing...")
					board.reparse()
				if inp[i] == "p":
					board.print_state()
