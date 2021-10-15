from PIL import Image, ImageDraw, ImageFont
begin=50
Requests=[95, 180, 34, 119, 11, 123, 62, 64]
steps=[50,34,11,180,123,119,95,64,62]
SeekLength=(50-34)+(34-11)+(180-11)+(180-123)+(123-119)+(119-95)+(95-64)+(64-62)#386
AverageSeekLength=SeekLength/len(Requests)
#print(SeekLength/len(Requests))48.25
#draw.line(xStart,yStart, xEnd,yEnd)

height=600
width=2100
color=(0,0,0)
img = Image.new('RGB',(width, height),(255,255,255))
draw=ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 100)
draw.text((width/2-300,10),font=font,text="Look (down)",fill=(0,255,0))
font = ImageFont.truetype("arial.ttf", 15)
draw.text((width-200,height-50),font=font,text=f"Seek Length: {SeekLength}\nAverage Seek Length: {AverageSeekLength}",fill=(150,150,0))
draw.line((50, height/2, width-50, height/2), fill=color,width=3)
draw.line((50, height/2, 100,height/2-50), fill=color,width=3)
draw.line((50, height/2, 100,img.size[1]/2+50), fill=color,width=3)
draw.line(( width-50, height/2, width-100,height/2-50), fill=color,width=3)
draw.line(( width-50, height/2, width-100,height/2+50), fill=color,width=3)
for r in Requests:
    draw.line(( 50+r*10, height/2-30, 50+r*10,height/2+30), fill=color,width=3)
    draw.text((42+r*10,height/2-50),font=font,text=f"{r}",fill=(0,0,240))
x=steps[0]*10+50
y=height/2+100
draw.ellipse([(x,y), (x+10, y+10)],fill="#ff0000",outline="yellow",width=3)
for s in steps[1:]:
    draw.ellipse([(x,y), (x+10, y+10)],fill="#ff0000",outline="yellow",width=3)
    draw.line(( x+5, y+5, s*10+55,y+25), fill=color,width=3)
    y+=20
    x=s*10+50
img.save('Look.png')
img.show()
