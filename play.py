import pyautogui as gui
import keyboard
import time
import math


top, left, width, height = 293, 0, 700, 465
last = 0
total_time = 0
x_start = 350
x_end = 380
y_search_cactus = 350


time.sleep(5)
while True:
    start_time = time.time()
    print('start')
    print(f'{start_time=}')
    if keyboard.is_pressed('q'):
        break
    if math.floor(total_time) != last:
        x_end += 2
        if x_end >= width:
            x_end = width
        last = math.floor(total_time)
    screenshot = gui.screenshot(region=(left, top, width, height))
    print('screenshot done')
    pixels = screenshot.load()

    background_color = pixels[440, 30]
    for i in reversed(range(x_start, x_end)):
        if pixels[i, y_search_cactus] != background_color:
            keyboard.press('space')
            print('jump')
            break

    end_time = time.time() - start_time
    print(f'{end_time=}')
    print('end')
    total_time += end_time
    print(f'{total_time=}')
