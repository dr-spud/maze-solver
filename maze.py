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
        self.seed = None

        if self.seed != None:
            random.seed(self.seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []
            
            if i - 1 >= 0:
                if not self._cells[i - 1][j].visited:
                    to_visit.append((i - 1, j))
            if i + 1 < self.num_rows:
                if not self._cells[i + 1][j].visited:
                    to_visit.append((i + 1, j))
            if j - 1 >= 0:
                if not self._cells[i][j - 1].visited:
                    to_visit.append((i, j - 1))
            if j + 1 < self.num_cols:
                if not self._cells[i][j + 1].visited:
                    to_visit.append((i, j + 1))
            
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            chosen = random.choice(to_visit)
            
            print("breaking wall")

            if chosen == (i - 1, j):
                self._cells[i][j].has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False
            elif chosen == (i + 1, j):
                self._cells[i][j].has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False
            elif chosen == (i, j - 1):
                self._cells[i][j].has_left_wall = False
                self._cells[i][j - 1].has_right_wall = False
            elif chosen == (i, j+ 1):
                self._cells[i][j].has_right_wall = False
                self._cells[i][j + 1].has_left_wall = False

            self._break_walls_r(chosen[0], chosen[1])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        current = self._cells[i][j]
        self._animate()
        current.visited = True

        directions = {
            "up": (i - 1, j),
            "down": (i + 1, j),
            "left": (i, j - 1),
            "right": (i, j + 1)
        }

        if i == self.num_rows - 1  and j == self.num_cols - 1:
            return True
        
        for direction, (new_i, new_j) in directions.items():
            if 0 <= new_i < self.num_rows and 0 <= new_j < self.num_cols:
                neighbour = self._cells[new_i][new_j]

                if (
                    direction == "up" and not current.has_top_wall or
                    direction == "down" and not current.has_bottom_wall or
                    direction == "left" and not current.has_left_wall or
                    direction == "right" and not current.has_right_wall
                ) and not neighbour.visited:
                    
                    current.draw_move(neighbour)

                    if self._solve_r(new_i, new_j):
                        return True
                    
                    current.draw_move(neighbour, undo=True)

        return False
            






                

        




