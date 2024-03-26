import matplotlib.pyplot as plt

LE = 0b0001
RE = 0b0010
BE = 0b0100
TE = 0b1000

def inside(a):
    return not a
def reject(a, b):
    return a & b
def accept(a, b):
    return not (a | b)
def round_int(a):
    return int(a)

def dda(x1, y1, x2, y2):
    xa, ya = [], []
    dy, dx = y2 - y1, x2 - x1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    xinc, yinc = dx / steps, dy / steps
    for i in range(steps + 1):
        xa.append(x1)
        ya.append(y1)
        x1 += xinc
        y1 += yinc
    plt.plot(xa, ya, color="black")

def encode(p1x, p1y, xwmin, ywmin, xwmax, ywmax):
    code = 0b0000
    if p1x < xwmin:
        code |= LE
    if p1x > xwmax:
        code |= RE
    if p1y < ywmin:
        code |= BE
    if p1y > ywmax:
        code |= TE
    return code

def clip_line(p1x, p1y, p2x, p2y, xwmin, xwmax, ywmin, ywmax):
    done = False
    draw = False
    m = 0
    while not done:
        code1 = encode(p1x, p1y, xwmin, ywmin, xwmax, ywmax)
        code2 = encode(p2x, p2y, xwmin, ywmin, xwmax, ywmax)
        if accept(code1, code2):
            done = True
            draw = True
        elif reject(code1, code2):
            done = True
        else:
            if inside(code1):
                p1x, p1y, p2x, p2y = p2x, p2y, p1x, p1y
                code1, code2 = code2, code1
            if p2x != p1x:
                m = (p2y - p1y) / (p2x - p1x)
            if code1 & LE:
                p1y += (xwmin - p1x) * m
                p1x = xwmin
            elif code1 & RE:
                p1y += (xwmax - p1x) * m
                p1x = xwmax
            elif code1 & BE:
                if p2x != p1x:
                    p1x += (ywmin - p1y) / m
                p1y = ywmin
            elif code1 & TE:
                if p2x != p1x:
                    p1x += (ywmax - p1y) / m
                p1y = ywmax
    if draw:
        dda(round_int(p1x), round_int(p1y), round_int(p2x), round_int(p2y))

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
clip_line(x1, y1, x2, y2, xmin, xmax, ymin, ymax)
plt.plot(window_X, window_Y)
plt.plot([x1,x2], [y1,y2])
plt.axis('off')
plt.show()
