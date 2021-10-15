from pyinsta.download import profile_pic

for a in range(65,26+65):
    try:
        c=str(chr(a))
        profile_pic(c)
    except:
        continue