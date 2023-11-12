import keyboard
import time
from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KeyController, Key

mouse = Controller()
keyboard_ctrl = KeyController()

is_autoclicker_running = False
pause_requested = False

def toggle_autoclicker():
    global is_autoclicker_running
    is_autoclicker_running = not is_autoclicker_running
    if is_autoclicker_running:
        print("Autoclicker started.")
        autoclicker()
    else:
        print("Autoclicker paused.")

def autoclicker():
    global pause_requested
    while is_autoclicker_running:
        mouse.press(Button.left)
        time.sleep(0.2)
        mouse.release(Button.left)
        keyboard_ctrl.press('s')
        time.sleep(0.11)
        keyboard_ctrl.release('s')
        time.sleep(0.1)

        keyboard_ctrl.press('w')
        time.sleep(0.01)
        keyboard_ctrl.release('w')
        time.sleep(0.05)
        
        # Check if a pause request is received
        if pause_requested:
            print("Autoclicker paused.")
            pause_requested = False
            break

# Start autoclicker on F6
keyboard.add_hotkey('F6', toggle_autoclicker)

# Check for pause request outside the autoclicker loop
while True:
    if keyboard.is_pressed('F7'):
        pause_requested = True
        time.sleep(0.1)  # Small delay to avoid multiple toggles with a single press
    time.sleep(0.1)
