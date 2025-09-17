import pyautogui as gui
import keyboard as kb
import time

#! Validation package
from validation import ErrMsg
errmsg = ErrMsg()

head = {
    'x' : 50,
    'y' : 50
    }
tail = [head]
duration = 0.12
grid_size = 50

def move_icons(from_x,from_y,to_x,to_y):
    gui.moveTo(x=from_x,y=from_y) #? move to end of tail
    gui.dragTo(x=to_x,y=to_y, duration=duration,button='left') #? drag icon to the new front or 'head'

def input(x,y):
    if kb.is_pressed('w'): #* up
        return {'x':x,'y':y-grid_size}
    if kb.is_pressed('s'): #* down
        return {'x':x,'y':y+grid_size}
    if kb.is_pressed('a'): #* left
        return {'x':x-grid_size,'y':y}
    if kb.is_pressed('d'): #* right
        return {'x':x+grid_size,'y':y}

while not kb.is_pressed('x'):
    time.sleep(0.01) #? as to not overload CPU with calculations
    new_head_pos = input(head['x'],head['y']) # using key input to determine new head
    #! here the snake doesnt move on it's own yet

    if new_head_pos is None:
        errmsg.dataErr("Data value None returned instead of expected type of { x:int, y:int }", 32)

    #* movement of icons
    move_icons(tail[-1]['x'],tail[-1]['y'],new_head_pos['x'],new_head_pos['y']) # type: ignore