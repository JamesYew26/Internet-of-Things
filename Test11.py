from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import Image,ImageDraw,ImageFont

serial = i2c(port=1, address=0x3C)
device = sh1106(serial, rotate=2, height=128)

# with canvas(device) as draw:
#     draw.rectangle(device.bounding_box, outline="white", fill="black")
#     draw.text((50,50), "@@@@@@@@@@", fill="blue")

image = Image.open("god.jpg")
image = image.resize((128,128))
image = image.convert('1')

device.dither = True
device.display(image)
device.show()