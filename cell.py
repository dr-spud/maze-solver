from windowsetup import Line, Point
class Cell:
    def __init__( self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = win
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
        walls = {
            "left": (self.has_left_wall, Point(x1, y1), Point(x1, y2)),
            "right": (self.has_right_wall, Point(x2, y1), Point(x2, y2)),
            "top": (self.has_top_wall, Point(x1, y1), Point(x2, y1)),
            "bottom": (self.has_bottom_wall, Point(x1, y2,), Point(x2, y2))
        }

        for wall_name, (has_wall, p1, p2) in walls.items():
            line = Line(p1, p2)
            if has_wall:
                self.__win.draw_line(line, "black")
            else:
                self.__win.draw_line(line, "white")
    
    def draw_move(self, to_cell, undo=False):
        color = "red" if undo is False else "gray"
        p_original = Point((self.__x1 + self.__x2) / 2, (self.__y1 + self.__y2) / 2)
        p_dest = Point((to_cell.__x1 + to_cell.__x2) / 2, (to_cell.__y1 + to_cell.__y2) / 2)
        line = Line(p_original, p_dest)
        self.__win.draw_line(line, color)




