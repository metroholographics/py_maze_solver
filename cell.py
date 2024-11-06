from graphics import Line, Point

class Cell():
	def __init__(self, window, has_left=True, has_right=True, has_top=True, has_bottom=True):
		self.has_left = has_left
		self.has_right = has_right
		self.has_top = has_top 
		self.has_bottom = has_bottom
		self._x1 = None
		self._x2 = None
		self._y1 = None
		self._y2 = None
		self._win = window

	def draw(self,x1, y1, x2, y2, fill_color="black"):
		self._x1 = x1
		self._x2 = x2
		self._y1 = y1
		self._y2 = y2 
		if self.has_left:
			self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), fill_color)
		if self.has_right:
			self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), fill_color)
		if self.has_top:
			self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), fill_color)
		if self.has_bottom:
			self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), fill_color)

	def draw_move(self, to_cell, undo=False):
		if undo:
			fill = "gray"
		else:
			fill = "red"
		from_mid_x = (self._x1 + self._x2) // 2
		from_mid_y = (self._y1 + self._y2) // 2
		to_mid_x = (to_cell._x1 + to_cell._x2) // 2
		to_mid_y = (to_cell._y1 + to_cell._y2) // 2

		self._win.draw_line(Line(Point(from_mid_x, from_mid_y), Point(to_mid_x, to_mid_y)), fill)
