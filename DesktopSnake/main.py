import pyautogui as gui
import keyboard as kb
import time

from apple import Apple, get_apple_position

####! Fail save
gui.FAILSAFE = True

DURATION_INTERVAL = .15 #! interval for drag for each icon
duration = .15 #* duration of drag

screen_width, screen_height = gui.size() #* get screen size
grid_x = 100
grid_y = 120

default_head_pos = {'x' : 30,'y' : 50} #* initial head position
new_head_pos = {'x': None, 'y': None}
tail = [default_head_pos] #* initial tail positions
direction = {'x': grid_x, 'y': 0} #* initial direction

#! Apple setup
apples = [] #* list to hold apples
apple_stored_pos = [] #* position to store apple spawn position
apple_spawn_interval = 20 #* spawn an apple every 15 loops
apple_timer = 0 #* timer to track apple spawns intervals

##! Function to move icons
def move_icons(from_x,from_y,to_x,to_y):
    gui.moveTo(x=from_x,y=from_y) #? move to end of tail
    gui.dragTo(x=to_x,y=to_y, duration=duration,button='left') #? drag icon to the new front or 'head'

##! Input function to determine new direction position
def input():
    if kb.is_pressed('w'): #* up
        return {'x':0,'y':-grid_y}
    if kb.is_pressed('s'): #* down
        return {'x':0,'y':grid_y}
    if kb.is_pressed('a'): #* left
        return {'x':-grid_x,'y':0}
    if kb.is_pressed('d'): #* right
        return {'x':grid_x,'y':0}

##! Collision detection function
def collision(head):
    if head['x'] < 0 or head['x'] > screen_width or head['y'] < 0 or head['y'] > screen_height:
        print('----Collision with Wall-----')
        return True
    for segment in tail[1:]:
        if head['x'] == segment['x'] and head['y'] == segment['y']:
            print('----Collision with ASelf----')
            return True
    return False

##! Manage drag duration
def duration_manager(amnt_icons):
    global duration
    duration = DURATION_INTERVAL * amnt_icons

##! Initial setup
print('-----Desktop Snake-----')
print('Please hover over all the icons you want to use for the snake/apples.\nPress "r" to record and "enter" to continue...')

apple_stored_pos = get_apple_position() # get possible apple positions from user

print('\nPlace one icon at the top left corner of the screen (This will be the head)')
print('Use W A S D to move the snake')
print('Press x to exit')

print('Starting in 3 seconds...')
time.sleep(3) #? give user time to switch to desired window

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

    #! Init Apple at random position at set intervals
    if apple_timer == 0 or apple_timer == apple_spawn_interval: # spawn apple at start or at set intervals
        if len(apple_stored_pos) > 0: #? check if there are stored apple positions left
            apples.append(Apple(stored_pos=apple_stored_pos[-1],tail=tail,apples=apples,all_stored_pos=apple_stored_pos)) #* spawn new apple at random position
        else: #? no more apple stored
            print('\n - No more stored apples! -\n\n----YOU WON!----')
            break
        apple_timer = 0 # reset timer
    apple_timer += 1 # increment timer