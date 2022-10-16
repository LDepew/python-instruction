import os
import qrcode

img = qrcode.make("https://youtu.be/xcFZjo5PgG0")

img.save("qr.png", "PNG")

os.system("open qr.png")