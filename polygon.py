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

size = int(input("Number of Vertices : "))
dfx, dfy, op = [], [], []
for i in range(size) :
    x = int(input("x"+str(i)+": "))
    y = int(input("y" + str(i) + ": "))
    o = int(input("op" + str(i) + ": "))
    dfx.append(x)
    dfy.append(y)
    op.append(o)

dfx.append(dfx[0])
dfy.append(dfy[0])
op.append(2)

for i in range(size+1) :
    if op[i] == 1 :
        plt.plot(dfx[i],dfy[i])
    elif op[i] == 2 :
        dda(dfx[i-1] ,dfy[i-1],dfx[i],dfy[i])
    else :
        plt.plot(dfx[0],dfy[0])

plt.show()