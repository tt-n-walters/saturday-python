import curses
from random import randint

screen = curses.initscr()
max_rows, max_columns = screen.getmaxyx()
curses.curs_set(0)
curses.noecho()
screen.timeout(100)

snowflakes = {}

while True:
    row = 0
    column = randint(0, max_columns - 2)
    snowflakes[(row, column)] = True

    screen.clear()

    # The concurrency problem
    iceflakes = {}
    for row, column in snowflakes:
        screen.addch(row, column, "*")
        if row < max_rows - 1 and not snowflakes.get((row + 1, column)):
            row += 1
        
        iceflakes[(row, column)] = True
    
    # Then comes the switch
    snowflakes = iceflakes

    if screen.getch() == 3:
        exit()
