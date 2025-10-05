import random
import pyautogui as gui
import keyboard as kb

class Apple:
    def __init__(self,stored_pos,all_stored_pos,tail,apples):
        self.position = {'x': None, 'y': None}
        self.stored_pos = stored_pos

        self.spawn(tail,apples,all_stored_pos)
        self.move_to_spawn()

    def spawn(self,tail,apples,all_stored_pos):
        screen_width, screen_height = gui.size()
        grid_x = 95
        grid_y = 120
        apple_x = random.randint(0, screen_width // grid_x) * grid_x
        apple_y = random.randint(0, screen_height // grid_y) * grid_y

        if self.check_collision(tail, apples,all_stored_pos): #? ensure no colliction with body of snake and other apples
            self.spawn(tail, apples,all_stored_pos) #! try again
            return

        self.position = {'x': apple_x, 'y': apple_y}

    #! moving apple to spawn position from stored position
    def move_to_spawn(self):
        #? Ignore keyboard interrupts during drag
        blocked_keys = ['w', 'a', 's', 'd', 'up', 'down', 'left', 'right']
        for key in blocked_keys:
            kb.block_key(key)

        try:
            #* Move apple from stored position to spawn position
            gui.moveTo(x=self.stored_pos['x'], y=self.stored_pos['y'])
            gui.dragTo(x=self.position['x'], y=self.position['y'], duration=0.5, button='left')
        finally:
            kb.unhook_all() #? Unblock all keys

    #! Ensure no colliction with body of snake and other apples
    def check_collision(self, tail, apples,all_stored_pos):
        for segment in tail:
            if self.position['x'] == segment['x'] and self.position['y'] == segment['y']:
                return True
        for apple in apples:
            if self.position['x'] == apple.position['x'] and self.position['y'] == apple.position['y']:
                return True
        for pos in all_stored_pos:
            if self.position['x'] == pos['x'] and self.position['y'] == pos['y']:
                return True
        return False

    #! Move apple to tail position last position
    def move_apple_to_tail(self,tail):
        #? Ignore keyboard interrupts during drag
        blocked_keys = ['w', 'a', 's', 'd', 'up', 'down', 'left', 'right']
        for key in blocked_keys:
            kb.block_key(key)

        try:
            #* Move apple from stored position to spawn position
            gui.moveTo(x=self.position['x'], y=self.position['y'])
            gui.dragTo(x=tail['x'], y=tail['y'], duration=0.5, button='left')
        finally:
            kb.unhook_all() #? Unblock all keys
        return


##! Function to get apple positions from user
def get_apple_position():
    positions = []
    formatted_positions = []
    amnt = 0

    while True:
        #! Wait for r to be pressed
        if kb.is_pressed("r"):
            pos = gui.position()
            positions.append(pos)
            amnt += 1
            print(f"   [{str(amnt)}] Recorded: {pos}")

            gui.sleep(0.2)#? prevent multiple recordings from one click

        #! Stop when Enter is pressed
        if kb.is_pressed("enter"):
            print("> Recording stopped.")
            break

    #? Formatting positions for easy use
    for p in positions:
        formatted_positions.append({'x': p[0], 'y': p[1]})

    return formatted_positions # set of recorded positions