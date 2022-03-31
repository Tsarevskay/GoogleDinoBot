from PIL import ImageGrab
import time


time.sleep(2)
while True:
    image = ImageGrab.grab().convert('L')
    pixels = image.load()

    # cactus
    for i in range(275, 325):
        for j in range(563, 650):
            pixels[i, j] = 0
    image.show()
    break
