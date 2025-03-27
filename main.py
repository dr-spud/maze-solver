from windowsetup import Window, Point, Line, Cell

def main():
    win = Window(800, 600)

    c1 = Cell(100, 200, 100, 200, win, has_right_wall=False)

    c1.draw()

    c2 = Cell(400, 450, 400, 450, win, has_top_wall=False)

    c2.draw()





    win.wait_for_close()

main()
