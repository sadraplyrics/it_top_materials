import pygame as pg
import sys
from config import *
from connect_four import *
import board
import random
import math
# ------------ pygame initialization ------------
pg.init()
pg.display.set_caption("Connect Four")
# ------------ InGame variables ------------
win_width = COLUMNS * DISC_SIZE
win_height = (ROWS + 1) * DISC_SIZE
size = (win_width, win_height)
current_player = 0
screen = pg.display.set_mode(size)
inner_font = pg.font.SysFont("Calibri", 60)
clock = pg.time.Clock()
# ------------ Functions ------------

    


def main():
    game_board = board.create_board()
    game_on = True
    current_player = random.randint(PLAYER, COMP)
    while game_on:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_on = False
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    game_on = False
                    sys.exit()

            if event.type == pg.MOUSEMOTION:
                pg.draw.rect(
                    screen,
                    WHITE,
                    (
                       0,
                       0,
                        win_width,
                        DISC_SIZE
                    )
                )
                
                position_x = event.pos[0]

                if current_player == PLAYER:
                    pg.draw.circle(
                        screen,
                        YELLOW,
                        (
                           position_x,
                           int(DISC_SIZE/2)
                        ),
                        DISC_RADUIS
                    )
                elif current_player == COMP:
                    pg.draw.circle(
                        screen,
                        RED,
                        (
                           position_x,
                           int(DISC_SIZE/2)
                        ),
                        DISC_RADUIS
                    )

            if event.type == pg.MOUSEBUTTONDOWN:
                pg.draw.rect(
                    screen,
                    WHITE,
                    (
                       0,
                       0,
                        win_width,
                        DISC_SIZE
                    )
                )  
                if current_player == PLAYER:
                    position_x = event.pos[0]
                    column = int(math.floor(position_x/DISC_SIZE))    
                if is_valid_position(game_board, column):
                    row = get_next_open_row(game_board, column)
                    game_board[row][column] = PLAYER_CHIP
                    if search_win_move(game_board, PLAYER_CHIP):
                        label = my_font.render("Player 1 wins!", 1, RED)
                        screen.blit(label, (10, 10))
                        game_over = True
                    current_player += 1
                    current_player = current_player % 2
                    draw_grid(game_board)
            pg.display.update()


        screen.fill(BLUE)
        draw_grid(game_board)
        #pg.display.flip()
        #clock.tick(60)
    pg.quit()

if __name__ == "__main__":
    main()