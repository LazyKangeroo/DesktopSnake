import pyautogui as gui
import keyboard as kb
import time

#! Validation package
from validation import ErrMsg
errmsg = ErrMsg()

####! Fail save
gui.FAILSAFE = True

default_head_pos = {'x' : 30,'y' : 50}
new_head_pos = {'x': None, 'y': None}
tail = [default_head_pos]
duration = .2
grid_size = 100

def move_icons(from_x,from_y,to_x,to_y):
    gui.moveTo(x=from_x,y=from_y) #? move to end of tail
    gui.dragTo(x=to_x,y=to_y, duration=duration,button='left') #? drag icon to the new front or 'head'

##* Input function to determine new head position
def input(x,y):
    if kb.is_pressed('w'): #* up
        return {'x':x,'y':y-grid_size}
    if kb.is_pressed('s'): #* down
        return {'x':x,'y':y+grid_size}
    if kb.is_pressed('a'): #* left
        return {'x':x-grid_size,'y':y}
    if kb.is_pressed('d'): #* right
        return {'x':x+grid_size,'y':y}

##! Main Gameloop
while not kb.is_pressed('x'): #* press 'x' to exit
    time.sleep(.5) #? as to not overload CPU with calculations

    #? get new head position
    head = tail[0] # get current head position
    new_head_pos = {'x': head['x'] + grid_size, 'y': head['y']}

    #? update tail and head positions
    tail.insert(0,new_head_pos) # add new head to the front of the list
    print(tail)

    #* movement of icons
    move_icons(tail[-1]['x'],tail[-1]['y'],new_head_pos['x'],head['y'])
    print('moved')

    tail.pop() # remove the last element of the list