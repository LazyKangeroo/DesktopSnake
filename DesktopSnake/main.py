import pyautogui as gui
import keyboard as kb
import time

####! Fail save
gui.FAILSAFE = True

DURATION_INTERVAL = .5 #! interval for drag for each icon
duration = .5 #* duration of drag

screen_width, screen_height = gui.size() #* get screen size
grid_x = 100
grid_y = 100

default_head_pos = {'x' : 30+grid_x*2,'y' : 50} #* initial head position
new_head_pos = {'x': None, 'y': None}
tail = [default_head_pos,{'x' : 30+grid_x,'y' : 50},{'x' : 30,'y' : 50}] #* initial tail positions
direction = {'x': grid_x, 'y': 0} #* initial direction

##! Function to move icons
def move_icons(from_x,from_y,to_x,to_y):
    gui.moveTo(x=from_x,y=from_y) #? move to end of tail
    gui.dragTo(x=to_x,y=to_y, duration=duration,button='left') #? drag icon to the new front or 'head'

##! Input function to determine new direction position
def input():
    if kb.is_pressed('w'): #* up
        print('up')
        return {'x':0,'y':-grid_y}
    if kb.is_pressed('s'): #* down
        print('down')
        return {'x':0,'y':grid_y}
    if kb.is_pressed('a'): #* left
        print('left')
        return {'x':-grid_x,'y':0}
    if kb.is_pressed('d'): #* right
        print('right')
        return {'x':grid_x,'y':0}

##! Collision detection function
def collision(head):
    if head['x'] < 0 or head['x'] > screen_width or head['y'] < 0 or head['y'] > screen_height:
        print('collision with wall')
        return True
    for segment in tail[1:]:
        if head['x'] == segment['x'] and head['y'] == segment['y']:
            print('collision with self')
            return True
    return False

##! Manage drag duration
def duration_manager(amnt_icons):
    global duration
    duration = DURATION_INTERVAL * amnt_icons

##! Main loop
while not kb.is_pressed('x'): #* press 'x' to exit
    duration_manager(len(tail)) # update drag duration based on tail length

    time.sleep(.2) #! as to not overload CPU with calculations

    new_direction = input() # get new direction from input
    time.sleep(.1) #! small delay to avoid multiple inputs

    if new_direction is None: #! if no key was pressed, skip the rest of the loop
        direction = direction # keep current direction
    else:
        direction = new_direction # update direction

    #? Manipulate head position
    head = tail[0] # get current head position

    #! Collision with wall or tail
    if collision(head):
        print('End of Game')
        break

    #? update new head position based on direction
    new_head_pos = {'x': head['x'] + direction['x'], 'y': head['y'] + direction['y']}

    #? update tail and head positions
    tail.insert(0,new_head_pos) # add new head to the front of the list

    move_icons(tail[-1]['x'],tail[-1]['y'],new_head_pos['x'],new_head_pos['y'])

    tail.pop() # remove the last element of the list

    print(tail) # print tail positions for debugging