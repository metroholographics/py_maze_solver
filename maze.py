from cell import Cell
import time

class Maze():
	def __init__(
			self,
			x1,
			y1,
			num_rows,
			num_cols,
			cell_size_x,
			cell_size_y,
			win=None
		):
		self.x1 = x1
		self.y1 = y1
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.cell_size_x = cell_size_x
		self.cell_size_y = cell_size_y
		self._win = win
		self._cells = []
		self._create_cells()

	def _create_cells(self):
		for x in range(self.num_cols):
			col_cells = []
			for y in range(self.num_rows):
				col_cells.append(Cell(self._win))
			self._cells.append(col_cells)

		for i in range(self.num_cols):
			for j in range(self.num_rows):
				self._draw_cell(i, j)

	def _draw_cell(self, i, j):
		if self._win is None:
			return 
		x_1 = self.x1 + (i * self.cell_size_x)
		y_1 = self.y1 + (j * self.cell_size_y)
		x_2 = x_1 + self.cell_size_x
		y_2 = y_1 + self.cell_size_y
		self._cells[i][j].draw(x_1, y_1, x_2, y_2)
		self._animate()

	def _animate(self):
		if self._win is None:
			return
		self._win.redraw()
		time.sleep(0.005)

