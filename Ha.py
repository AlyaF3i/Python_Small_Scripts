from PIL import Image, ImageDraw,ImageFont
text='HHAZXCV'
width=len(text)*215
font = ImageFont.truetype("arial.ttf", 300)
Images=[]
img=Image.new('RGB',(width, 300),(220,230,210))
draw=ImageDraw.Draw(img)
draw.text((0,0),font=font,text=f"{text}",fill=(10,20,20))

for a in range(0,width-300,50):
    Images.append(img.crop((a,0,a+300,300)))
Images[0].save('output.gif',save_all=True, append_images=Images[1:], optimize=False, duration=150, loop=0)

img.show()