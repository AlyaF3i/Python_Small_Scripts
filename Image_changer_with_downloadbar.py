from PIL import Image
from sys import argv
import time
import os
def ToTime(num):
    num = int(num)
    sec = str(num % 60).zfill(2)
    min = str(num // 60).zfill(2)
    return f"{min} : {sec}"

def load(num):

    square = int(num//5)
    num = round(num,2)
    s = str(num)
    if len(s.split('.')) != 2:
        s = s + '0'
    s=str(num).zfill(5)
    print("█"*square,end="")
    print(" "*(20-square),end="")
    print(f"  => {s}%   ",end="")
dir = f"images_{argv[1].split('.')[0]}"
os.mkdir(dir)   
image = Image.open(argv[1])
w,h = image.size
n = 5
pics = n**3
timee = time.time()
estimated_time = "Calculating . . ."
for a in range(n):
    for b in range(n):
        for c in range(n):
            image = Image.open(argv[1])
            img = image.load()
            filename = f"{a}{b}{c}.jpg"
            for i in range(w):
                for j in range(h):
                    color = list(img[i,j])
                    color.append(sum(color)//3)
                    color.append(0)
                    img[i,j] = (color[a], color[b], color[c])
                if i % 10 == 0:
                    load((i/w)*100)
                    print(f"{filename}\t{time.time()-timee}\testimated time: {estimated_time}")
            image.save(f'{dir}/{filename}')
            estimated_time = ToTime(
                round(
                    (
                        (
                            pics/(
                                (a+1)*
                                (b+1)*
                                (c+1)
                                )
                            )-1
                        )*
                    (time.time()-timee)
                    ,2)
            )
            print(f"{filename} Has Been Created")


print("DONE!")
#image.show()