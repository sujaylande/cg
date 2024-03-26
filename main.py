import matplotlib.pyplot as plt
def clipTest(p, q, u1, u2) :
    returnValue = True
    r = q/p
    if p < 0.0 :
        if r > u2 :
            returnValue = False
        elif r > u1 :
            u1 = r
    elif p > 0.0 :
        if r < u1 :
            returnValue = False
        elif r < u2 :
            u2 = r
    elif q < 0.0 :
        returnValue = False

    return (returnValue, u1, u2)

def dda(x1, y1, x2, y2) :
    dx, dy = x2 - x1, y2 -y1
    xa, ya = [], []
    steps = max(abs(dx), abs(dy))
    xinc, yinc = dx/steps, dy/steps
    for i in range(steps + 1) :
        xa.append(x1)
        ya.append(y1)
        x1 += xinc
        y1 += yinc
    plt.plot(xa,ya)

def liangBarsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax) :
    u1, u2 = 0.0, 1.0
    dx = x2-x1
    dy = y2-y1
    clip, u1, u2 = clipTest(-dx,x1-xmin,u1,u2)
    if clip :
        clip, u1, u2 = clipTest(dx, xmax - x1, u1, u2)
        if clip :
            clip, u1, u2 = clipTest(-dy, y1 - ymin, u1, u2)
            if clip :
                clip, u1, u2 = clipTest(dy, ymax - y1, u1, u2)
                if clip :
                    if u2 < 1.0 :
                        x2 = x1 + u2 * dx
                        y2 = y1 + u2 * dy
                    if u1 > 0.0 :
                        x1 = x1 + u1 * dx
                        y1 = y1 + u1 * dy
                    dda(round(x1), round(y1), round(x2), round(y2))


x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))
xmin = int(input("xmin : "))
xmax = int(input("xmax : "))
