from random import randint
def CreatePixels(w=426,h=240):
    def APixel():
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        return (r,g,b)
    pixels=[]  
    for _ in range (h):
        Line=[]
        for __ in range (w):
            Line.append(APixel())
        pixels.append(Line)
    return pixels
