from windowsetup import Line, Point
import time
class Cell:
    def __init__(
            self,
            x1,
            x2,
            y1,
            y2,
            win,
            has_left_wall=True,
            has_right_wall=True,
            has_top_wall=True,
            has_bottom_wall=True  
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = win
    
    def draw(self):
        walls = {
            "left": (self.has_left_wall, Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)),
            "right": (self.has_right_wall, Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)),
            "top": (self.has_top_wall, Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)),
            "bottom": (self.has_bottom_wall, Point(self.__x1, self.__y2,), Point(self.__x2, self.__y2))
        }

        for wall_name, (has_wall, p1, p2) in walls.items():
            if has_wall:
                line = Line(p1, p2)
                self.__win.draw_line(line, "black")
    
    def draw_move(self, to_cell, undo=False):
        color = "red" if undo is False else "gray"
        p_original = Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)
        p_dest = Point((to_cell.__x1 + to_cell.__x2) / 2, (to_cell.__y1 + to_cell.__y2) / 2)
        line = Line(p_original, p_dest)
        self.__win.draw_line(line, color)

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win
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
                x1 = self.x1 + j * self.cell_size_x
                y1 = self.y1 + i * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y

                cell = Cell(x1, x2, y1, y2, self.__win)
                row.append(cell)
            self._cells.append(row)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()
        

    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)




