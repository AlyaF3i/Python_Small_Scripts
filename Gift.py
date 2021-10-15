import ctypes
from PIL import Image, ImageDraw,ImageFont
import os

s="LEGEND NEVER DIE"
font=ImageFont.truetype("arial.ttf", 100)
img=Image.new('RGB',(700,500),(255,255,255))
draw=ImageDraw.Draw(img)
draw.text((0,500//3),font=font,text=s,fill=(0,0,240))
img.save("hi.bmp")
ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{os.getcwd()}\hi.bmp" , 0)
os.remove(f"{os.getcwd()}\hi.bmp")