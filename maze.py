from cell import Cell
import time
import random

class Maze:
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
        self.__win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):

                cell = Cell(self.__win)
                row.append(cell)
            self._cells.append(row)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)
        
        self.break_entrance_and_exit()

    def _draw_cell(self, i, j):
        if self.__win is None:
            return
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self._animate()
        

    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)

    def break_entrance_and_exit(self):
        n = random.randint(0, 1)
        if n == 0:
            self._cells[0][0].has_top_wall = False
        else:
            self._cells[0][0].has_left_wall = False

        n = random.randint(0, 1)
        if n == 0:
            self._cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        else:
            self._cells[self.num_rows - 1][self.num_cols - 1].has_right_wall = False 


