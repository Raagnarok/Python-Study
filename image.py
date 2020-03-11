from PIL import ImageGrab
import time

time.sleep(3)

 # supposed to get data from the picture
def image():
    im = Image.open('C:\pix.png', 'r')
    pix_val = list(im.getdata())
    pix_val = [x for sets in pix_val for x in sets]

 # print screens
def capture_screen():
    screen = ImageGrab.grab()
    return screen

 # supposed to detect the picture / message box when it shows up.
def detect_box(screen):
    for x in range(406, 576):
        for y in range(267, 312):
            box = screen.getpixel((x, y))
            if box == image:
                return True

while True:
    screen = capture_screen()
    print("running")

    if detect_box(screen):
        print("found it")









