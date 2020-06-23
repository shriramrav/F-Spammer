import pynput
import time
import keyboard
import pyautogui

spammer = pynput.keyboard.Controller()
clicker = pynput.mouse.Controller()

# 5 seconds to open up chat and hover mouse position over 'send'
time.sleep(5)

while True:
    time.sleep(.1)
    spammer.press('f');
    time.sleep(.1)
    clicker.position = pyautogui.position()
    clicker.click(pynput.mouse.Button.left, 1)

    # press 'q' to quit the spammer
    if keyboard.is_pressed('q'): 
        break