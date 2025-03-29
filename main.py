from windowsetup import Window, Point, Line
from cell import Cell, Maze

def main():
    win = Window(800, 600)

    maze = Maze(0, 0, 6, 6, 50, 50, win)

    maze._create_cells()




    win.wait_for_close()

main()
