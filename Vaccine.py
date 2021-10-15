import requests
import bs4
from PIL import ImageDraw,Image,ImageFont
import datetime as date

today=date.datetime.now().date()


f=requests.get(url="https://covid19.ncema.gov.ae/en/page/about-the-vaccine", verify=False)
f.raise_for_status()
block=bs4.BeautifulSoup(f.text,'html.parser')
#print("\n\n\n\n\n\n\n")
arr=['doses','tests','total','deaths','recovered','active']
output=list()
for a in arr:
    Num=block.select(f".{a}")[0].select(".counter")[0].text
    output.append(f"{a}: {Num}")
    #print(f"{a}: \t",Num)
width=345
height=275
img=Image.new('RGB',(height, width),(255,255,255))
draw=ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 30)
for index,a in enumerate(output):
    draw.text((10,index*60),font=font,text=a,fill=(200,0,0))
    draw.line((0,index*60+45,width,index*60+45),fill=(0,0,250),width=3)
corner=[(0,0),(0,width),(height,width),(height,0)]
for a in range(3):
    draw.line(corner[a]+corner[a+1],fill=(0,255,0),width=5)
draw.line(corner[0]+corner[3],fill=(0,255,0),width=6)
img.show()
img.save(rf'vaccine/{today}.jpg')

#print(block.select(".tests")[0].select(".counter"))