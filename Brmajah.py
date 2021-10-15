from PIL import Image, ImageDraw, ImageFont

img= Image.new('RGB',(500,500), (255,255,255))
def DrawX(img, index):
    x=index[0]*300
    y=index[1]*300
    img.line((10+x,10+y,x-10+500//3,y-10+500//3), fill=(242,111,111), width=4)
    img.line((10+x,y-10+500//3,x+500//3-10,y+10), fill=(224,144,111), width=4)
def DrawO(img, index):
    x=index[0]*300
    y=index[1]*300
    img.line((10+x,10+y,10+x, y+500//3-10), fill=(124,142,111),width=2)
    img.line((10+x, y+500//3-10,x-10+500//3,y-10+500//3), fill=(124,142,111),width=2)
    img.line((x-10+500//3,y-10+500//3,x-10+500//3,y+10), fill=(124,142,111),width=2)
    img.line((x-10+500//3,y+10,10+x,10+y), fill=(124,142,111),width=2)

color = (0,0,1)

draw = ImageDraw.Draw(img)

for a in range(0,500,500//3):
    draw.line((0,a,500,a), fill=(4,1,6), width=3)
    draw.line((a,0,a,500), fill=(4,1,6), width=3)
DrawX(draw, [0,0])
DrawO(draw, [0,1])

img.show()
