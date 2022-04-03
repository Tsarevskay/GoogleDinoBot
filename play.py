import pyautogui as pg
import keyboard
import time
import math


coord_search = {'top': 293, 'left': 0, 'width': 720, 'height': 465}
x_start = 362
x_end = 392
y_search_cactus = 350
last_time = 0
total_time = 0


def get_screen(left, top, width, height):
    screenshot = pg.screenshot(region=(left, top, width, height))
    print('screenshot done')
    n_pixel = screenshot.load()
    return n_pixel


def is_cactus(n_pixel, start, end, y_cactus):
    background_color = n_pixel[440, 30]
    for i in reversed(range(start, end)):
        if n_pixel[i, y_cactus] != background_color:
            return True


def search(coord, start, end, y_cactus, last_times, total_times):
    while True:
        start_time = time.time()
        print(f'{start_time=}')
        if keyboard.is_pressed('q'):
            break
        print(f'{total_times=}')
        print(f'{last_times=}')
        if math.floor(total_times) != last_times:
            end += 5
            if end >= coord['width']:
                end = coord['width']
            last_times = math.floor(total_times)

        pixels = get_screen(coord['left'], coord['top'], coord['width'], coord['height'])
        if is_cactus(pixels, start, end, y_cactus):
            keyboard.press('space')
            print('jump')

        end_time = time.time() - start_time
        print(f'{end_time=}')
        print('end')
        total_times += end_time
        print(f'{total_times=}')


if __name__ == '__main__':
    print('5 seconds to open the game window')
    time.sleep(5)
    keyboard.press('space')
    print('First start')
    search(coord_search,  x_start, x_end, y_search_cactus, last_time, total_time)
