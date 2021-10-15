import matplotlib.pyplot as draw

marks=[44, 33, 34, 52, 29, 32, 33, 49, 48, 46, 59, 51, 34, 53, 48, 55, 47, 42, 51, 55, 48, 48, 57, 43, 54, 54, 32, 48, 48, 53, 57, 45, 4]

draw.hist(marks,20,stacked=True,facecolor='red', alpha=0.5,edgecolor="black")
draw.title("Web Marks out of 60")
draw.show()