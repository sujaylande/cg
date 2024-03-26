import matplotlib.pyplot as plt

def dda(x1,y1,x2,y2) :
    xa,ya = [], []
    dy, dx = y2-y1, x2-x1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    xinc, yinc = dx/steps, dy/steps
    for i in range(steps+1) :
        xa.append(x1)
        ya.append(y1)
        x1 += xinc
        y1 += yinc
    plt.plot(xa,ya,color = "black")

def drawH(x,y) :
    dda(x,y,x,y+200)
    dda(x,y+100,x+100,y+100)
    dda(x+100,y,x+100,y+200)

def drawE(x,y) :
    dda(x,y,x,y+200)
    dda(x,y,x+100,y)
    dda(x,y+100,x+100,y+100)
    dda(x,y+200,x+100,y+200)

def drawL(x,y) :
    dda(x,y,x,y+200)
    dda(x,y,x+100,y)

def drawO(x,y) :
    dda(x,y,x,y+200)
    dda(x,y+200,x+100,y+200)
    dda(x+100,y+200,x+100,y)
    dda(x+100,y,x,y)

hx = int(input("Hx coorindates : "))
hy = int(input("Hy coorindates : "))
ex = int(input("Ex coorindates : "))
ey = int(input("Ey coorindates : "))
lx1 = int(input("First Lx coorindates : "))
ly1 = int(input("First Ly coorindates : "))
lx2 = int(input("Second Lx coorindates : "))
ly2 = int(input("Second Ly coorindates : "))
ox = int(input("Ox coorindates : "))
oy = int(input("Oy coorindates : "))

xa = [hx,ex,lx1,lx2,ox]
ya = [hy,ey,ly1,ly2,oy]

drawH(xa[0],ya[0])
drawE(xa[1],ya[1])
drawL(xa[2],ya[2])
drawL(xa[3],ya[3])
drawO(xa[4],ya[4])
plt.show()