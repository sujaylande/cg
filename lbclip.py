import matplotlib.pyplot as plt
def clipTest(p, q, u1, u2):
    returnValue = True
    r = q / p
    if p < 0.0:
        if r > u2:
            returnValue = False
        elif r > u1:
            u1 = r
    elif p > 0.0:
        if r < u1:
            returnValue = False
        elif r < u2:
            u2 = r
    elif q < 0:
        returnValue = False
    return (returnValue, u1, u2)

def dda(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    xa, ya = [], []
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps
    x, y = x0, y0
    for _ in range(steps + 1):
        xa.append(x)
        ya.append(y)
        x += x_increment
        y += y_increment
    plt.plot(xa,ya)

def liangBarsky(xwmin, ywmin, xwmax, ywmax, p1x, p1y, p2x, p2y):
    u1, u2 = 0.0, 1.0
    dx, dy = p2x - p1x, p2y - p1y
    clipTestResult, u1, u2 = clipTest(-dx, p1x - xwmin, u1, u2)
    if clipTestResult:
        clipTestResult, u1, u2 = clipTest(dx, xwmax - p1x, u1, u2)
        if clipTestResult:
            clipTestResult, u1, u2 = clipTest(-dy, p1y - ywmin, u1, u2)
            if clipTestResult:
                clipTestResult, u1, u2 = clipTest(dy, ywmax - p1y, u1, u2)
                if clipTestResult and u2 < 1.0:
                    p2x = p1x + u2 * dx
                    p2y = p1y + u2 * dy
                if u1 > 0.0:
                    p1x += u1 * dx
                    p1y += u1 * dy
                dda(round(p1x), round(p1y), round(p2x), round(p2y))

x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))
print("\nEnter dimensions of Window : ")
xmin = int(input("xmin : "))
xmax = int(input("xmax : "))
ymin = int(input("ymin : "))
ymax = int(input("ymax : "))
window_X = [xmin, xmax, xmax, xmin, xmin]
window_Y = [ymin, ymin, ymax, ymax, ymin]
liangBarsky(xmin, ymin, xmax, ymax, x1, y1, x2, y2)
plt.plot(window_X, window_Y)
plt.plot([x1,x2], [y1,y2])
plt.axis('off')
plt.show()
