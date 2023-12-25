import pygame as pg
import oculo_globals

def update_events(): # DO NOT USE THIS. EVER. EXCEPT FOR MAIN LOOP
    #oculo_globals.GAME_STATUS['events'] = pg.event.get()
    #print(len(oculo_globals.GAME_STATUS['events']))
    return pg.event.get()

def get_events():
    return oculo_globals.GAME_STATUS['events']