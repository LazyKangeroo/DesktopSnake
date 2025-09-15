import os
import pyautogui as gui
import time

head = {'x':50,'y':50}
tail = []
duration = 0.12
direction_shift = {'x':50,'y':50}

def move_icons()
    gui.moveTo(x=50,y=50)
    gui.dragTo(x=100,y=50, duration=duration,button='left')
    