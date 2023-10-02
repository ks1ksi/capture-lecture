# capture current screen

import os

import keyboard
import pyautogui

num = 1
dirname = 'computer_network_5_1'

# create a directory for screenshots
if not os.path.exists(dirname):
    os.mkdir(dirname)

print('lecture %s' % dirname)

# take screenshot of a specific region. save it to directory with a name
while True:
    print('waiting for tab key...')
    keyboard.wait('tab')
    pyautogui.screenshot(
        f'{dirname}/screenshot{num}.png', region=(340, 140, 2030, 1530))
    print(f'screenshot{num}.png saved!')
    # alert user that screenshot is taken

    num += 1
