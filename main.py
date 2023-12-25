from get_events import update_events
from display_game import update_game_display
import pygame as pg
import sys

pg.init()
game_clock = pg.time.Clock()
running = True

while running:
    current_events = update_events()
    game_clock.tick_busy_loop(30)
    for event in current_events:
        if(event.type == pg.QUIT):
            running = False
    
    update_game_display()
else:
    pg.quit()
    sys.exit()