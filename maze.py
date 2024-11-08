from cell import Cell
import time
import random

class Maze():
	def __init__(
			self,
			x1,
			y1,
			num_rows,
			num_cols,
			cell_size_x,
			cell_size_y,
			win=None,
			seed=None
		):
		self.x1 = x1
		self.y1 = y1
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.cell_size_x = cell_size_x
		self.cell_size_y = cell_size_y
		self._win = win

		if seed is not None:
			random.seed(seed)

		self._cells = []
		self._create_cells()
		self._break_entrance_and_exit()

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
		time.sleep(0.05)

	def _break_entrance_and_exit(self):
		self._cells[0][0].has_top = False
		self._draw_cell(0, 0)
		self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom = False
		self._draw_cell(self.num_cols - 1, self.num_rows - 1)

	def _break_walls_r(self, i, j):
		self._cells[i][j].visited = True

		while True:
			to_visit = []
			if i - 1 > 0:
				if not self._cells[i - 1][j].visited:
					to_visit.append((i - 1, j))
			if j - 1 > 0:
				if not self._cells[i][j - 1].visited:
					to_visit.append((i, j - 1))
			if i + 1 < self.num_cols:
				if not self._cells[i + 1][j].visited:
					to_visit.append((i + 1, j))
			if j + 1 < self.num_rows:
				if not self._cells[i][j + 1].visited:
					to_visit.append((i, j + 1))

			if len(to_visit) == 0:
				self._draw_cell(i, j)
				return

			else:
				d = to_visit[random.randrange(len(to_visit))]
				if d[0] < i:
					self._cells[i][j].has_left = False
					self._cells[d[0]][d[1]].has_right = False
				elif d[0] > i:
					self._cells[i][j].has_right = False
					self._cells[d[0]][d[1]].has_left = False
				elif d[1] < j:
					self._cells[i][j].has_top = False
					self._cells[d[0]][d[1]].has_bottom = False
				elif d[1] > j:
					self._cells[i][j].has_bottom = False
					self._cells[d[0]][d[1]].has_top = False

				self._break_walls_r(d[0], d[1])









