import mss
import mss.tools
import time
from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw


def get_screen():
    sct = mss.mss()
    monitor = {"top": 220, "left": 500, "width": 910, "height": 225}
    image = sct.grab(monitor)
    return image


def get_filename():
    path = 'shot_{}.png'.format(int(time.time()))
    return path


def red_lines(image, l_step=50, l_width=2):
    img = Image.frombytes('RGB', image.size, image.bgra, 'raw', 'BGRX')
    draw = ImageDraw.Draw(im=img, mode=img.mode)
    fill = ImageColor.getrgb('red')
    width, height = img.size
    print(f'{width=}')
    print(f'{height=}')
    # vertical lines
    for i in range(0, width, l_step):
        draw.line(xy=((i, 0), (i, height)), fill=fill, width=l_width)
    # horizontal lines
    for i in range(0, height, l_step):
        draw.line(xy=((0, i), (width, i)), fill=fill, width=l_width)
    path = get_filename()
    img.save(path, "PNG")
    return path


def rectangle(path, coord):
    image = Image.open(path)
    draw = ImageDraw.Draw(image)
    xy = (
        (coord['left'], coord['top'],),
        (coord['left'] + coord['width'], coord['top'] + coord['height'])
    )
    draw.rectangle(xy, fill=None, outline='green', width=4)
    path = get_filename()
    image.save(path, "PNG")
    return path


time.sleep(2)
sct_img = get_screen()
filename = red_lines(sct_img)
coord_right = {'left': 750 + 50, 'top': 150, 'width': 100, 'height': 100-50}
coord_left = {'left': 350 + 50, 'top': 150, 'width': 100, 'height': 100-50}
filename = rectangle(filename, coord_right)
filename = rectangle(filename, coord_left)
