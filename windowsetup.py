from tkinter import Tk, BOTH, Canvas
class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title = ("maze solver")
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)

        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()

        print(("window closed..."))

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
        
    def close(self):
        self.running = False

    

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )

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




        
    


