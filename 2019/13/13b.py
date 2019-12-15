from computer import Computer, IOInputAction, IOOutputAction
from curses import wrapper, KEY_LEFT, KEY_RIGHT
from time import sleep
from collections import defaultdict
from copy import deepcopy

tile_types = {
    0: ' ',
    1: '#',
    2: '@',
    3: '-',
    4: '*'
}

def main():
    score = 0
    count = 0

    def game(stdscr):
        nonlocal score
        nonlocal count

        computer = Computer()
        computer.load_file("13.txt")
        computer.memory[0] = 2
        input_order = -1
        x = 0
        y = 0
        past = []
        playing = True
        screen = {}

        while playing:
            for action in computer.execute():
                if isinstance(action, IOOutputAction):
                    input_order += 1
                    input_order %= 3
                    if input_order == 0:
                        x = action.value
                    elif input_order == 1:
                        y = action.value
                    elif input_order == 2:
                        tile = action.value
                        if x == -1 and y == 0:
                            score = tile
                        else:
                            stdscr.addch(y, x, tile_types[tile])
                            stdscr.refresh()
                            screen[(y, x)] = tile_types[tile]
                elif isinstance(action, IOInputAction):
                    past.append((computer.save(), deepcopy(screen)))
                    count += 1
                    key_press = stdscr.getch()
                    if key_press == KEY_LEFT:
                        action.value = -1
                    elif key_press == KEY_RIGHT:
                        action.value = 1
                    elif key_press == ord('z'):
                        past.pop()
                        break
                    else:
                        action.value = 0
            else:
                playing = False
            if playing:
                past.pop()
                state, screen = past.pop()
                computer.restore(state)
                stdscr.clear()
                for (y, x), tile in screen.items():
                    stdscr.addch(y, x, tile)

    wrapper(game)
    print('Count: ' + str(count))
    print('Score: ' + str(score))

main()
