import math
import numpy as np
"""
a   b   c
d   e   f
g   h   i
dis: distance between 2 points
"""
def slopeCalc(a,b,c,d,e,f,g,h,i,dis):
    dzdx = ((c + (2*f) + i) - (a + (2*d) + g)) / (8 * dis)
    dzdy = ((g + (2*h) + i) - (a + (2*b) + c)) / (8 * dis)
    rise= math.sqrt(pow(dzdx,2)+pow(dzdy,2))
    slope= math.atan(rise)*57.29578
    return slope



#print(slopeCalc(50,45,50,30,30,30,8,10,10,5))
