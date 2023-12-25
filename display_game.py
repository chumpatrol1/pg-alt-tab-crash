import oculo_globals
import pygame as pg
pg.display.set_caption('Oculo Test')
oculo_globals.CACHE['display_area'] = pg.display.set_mode((960, 540))
oculo_globals.CACHE['game_display'] = pg.Surface((960, 540))

def update_game_display():
    oculo_globals.CACHE['display_area'].blit(oculo_globals.CACHE['game_display'], (0, 0))
    pg.display.flip()