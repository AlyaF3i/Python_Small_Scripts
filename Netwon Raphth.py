def func(x):
    #F(x)=(x-2)^4
    #F`(x)=4(x-2)
    #g(x)=x-(F(x)/F`(x))
    #g(x)=x-((x-2)^4/(x-2)^3) = x-(x-2)/4 = 3x/4 + 1/2
    num=x*3/4 + 0.5
    print(num)
    return num
def func1(x):
    #F(x)=(x-2)^4
    #F`(x)=4(x-2)
    #g(x)=x-(F(x)/F`(x))
    #g(x)=x-((x-2)^4/(x-2)^3) = x-(x-2)/4 = 3x/4 + 1/2
    num=x/2 + 1
    print(num)
    return num
num=2.1
for a in range(10):
    num=func1(num)