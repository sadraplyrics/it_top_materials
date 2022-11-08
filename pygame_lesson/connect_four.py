import pygame as pg
import sys
import math
import random
from config import *
from board import *

pg.init()
pg.display.set_caption('Connect 4')
width = COLUMNS * DISC_SIZE
height = (ROWS + 1) * DISC_SIZE

size = (COLUMNS * DISC_SIZE, (ROWS + 1) * DISC_SIZE)
screen = pg.display.set_mode(size)
my_font = pg.font.SysFont('Calibri', 60)

def draw_grid(grid):
    for col in range(COLUMNS):
        for row in range(ROWS):
            pg.draw.circle(
                screen,
                WHITE,
                (
                    int(col*DISC_SIZE + DISC_SIZE/2),
                    int((row*DISC_SIZE + DISC_SIZE/2) + DISC_RADUIS*3),
                ),
                DISC_RADUIS
            )
    for col in range(COLUMNS):
        for row in range(ROWS):
            if grid[row][col] == PLAYER_CHIP:
                pg.draw.circle(
                    screen,
                    YELLOW,
                    (
                        int(col*DISC_SIZE + DISC_SIZE/2),
                        int(row*DISC_SIZE + DISC_SIZE/2+ DISC_RADUIS*3),
                    ),
                    DISC_RADUIS
                )
            elif grid[row][col] == COMP_CHIP:
                pg.draw.circle(
                    screen,
                    RED,
                    (
                        int(col*DISC_SIZE + DISC_SIZE/2),
                        int(row*DISC_SIZE + DISC_SIZE/2 + DISC_RADUIS*3),
                    ),
                    DISC_RADUIS
                )


def is_valid_position(grid, col):
    return grid[ROWS - 1][col] == 0


def get_valid_position(grid):
    valid_position = []
    for col in range(COLUMNS):
        if is_valid_position(grid, col):
            valid_position.append(col)
    return valid_position


def get_next_open_row(grid, c):
    for r in range(ROWS):
        if grid[r][c] == 0:
            return r


def search_win_move(grid, piece):
# horizontal
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if grid[r][c] == piece and grid[r][c + 1] == piece \
            and grid[r][c + 2] == piece and grid[r][c + 3] == piece:
                return True
# vertical
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if grid[r][c] == piece and grid[r + 1][c] == piece \
                and grid[r + 2][c] == piece and grid[r + 3][c] == piece:
                return True
# positively sloped diaganols
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if grid[r][c] == piece and grid[r +
                1][c + 1] == piece \
                and grid[r + 2][c + 2] == piece and grid[r + 3][c + 3] == piece:
                    return True
# negatively sloped diaganols
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if grid[r][c] == piece and grid[r - 1][c + 1] == piece \
            and grid[r - 2][c + 2] == piece and grid[r - 3][c + 3] == piece:
                return True

   