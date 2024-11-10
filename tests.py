import unittest
from maze import Maze

class Tests(unittest.TestCase):
	def test_maze_create_self(self):
		num_cols = 12
		num_rows = 10
		m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
		self.assertEqual(
			len(m1._cells),
			num_cols,
		)
		self.assertEqual(
			len(m1._cells[0]),
			num_rows,
		)

	def test_maze_create_cells_large(self):
		num_cols = 20
		num_rows = 12
		m1 = Maze(0, 0, num_rows, num_cols, 5, 5, seed=None)
		self.assertEqual(
			len(m1._cells),
			num_cols,
		)
		self.assertEqual(
			len(m1._cells[0]),
			num_rows,
		)

	def test_maze_entrance_and_exit(self):
		num_cols = 5
		num_rows = 5
		m1 = Maze(0, 0, num_rows, num_cols, 5, 5, seed=None)

		self.assertEqual(
			m1._cells[0][0].has_top,
			False,
		)

		self.assertEqual(
			m1._cells[num_cols - 1][num_rows - 1].has_bottom,
			False,
		)


	def test_cells_reset_after_maze(self):
		num_cols = 5
		num_rows = 5
		m1 = Maze(0, 0, num_rows, num_cols, 5, 5, seed=0)

		self.assertEqual(
			m1._cells[0][0].visited,
			False,
		)

		self.assertEqual(
			m1._cells[num_cols - 1][num_rows - 1].visited,
			False,
		)

		self.assertEqual(
			m1._cells[1][2].visited,
			False,
		)



if __name__ == "__main__":
	unittest.main()