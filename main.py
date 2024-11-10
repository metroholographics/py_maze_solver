from graphics import Window
from cell import Cell
from maze import Maze

def main():
	width = 800
	height = 600
	num_rows = 12
	num_cols = 16
	margin = 50

	cell_size_x = (width - 2 * margin) / num_cols
	cell_size_y = (height - 2 * margin) / num_rows

	win = Window(width, height)
	maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win=win, seed=0)
	
	win.wait_for_close()



if __name__ == "__main__":
	main()


