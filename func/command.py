from func import screen, board, solver

#Function to run a input command line thing for the sake of debugging
#While loop broken by user input through command line, i.e. something like Ctrl + C
def on():
	while(True):
		inp = input()
		for i in range(len(str(inp))):
			if inp[i] == "r":
				board.reparse()
			if inp[i] == "p":
				board.print_state()
			if inp[i] == "c":
				print(board.find_conditions())
			if inp[i] == "m":
				solver.make_move()
			if inp[i] == "l":
				solver.loop()