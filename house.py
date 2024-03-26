import matplotlib.pyplot as plt
def house(x, y, xrel, yrel) :
    xa, ya = [], []
    for i in range (len(xrel)) :
        xa.append(x)
        ya.append(y)
        x = x + xrel[i]
        y = y + yrel[i]
    xa.append(x)
    ya.append(y)
    plt.plot(xa, ya)

xrel, yrel = [], []
print("Enter Relative array : ")
for i in range(5) :
    x = float(input("xrel " + str(i + 1) + " : "))
    y = float(input("yrel " + str(i + 1) + " : "))
    xrel.append(x)
    yrel.append(y)

hx = float(input("X - coordinate of House : "))
hy = float(input("Y - coordinate of House : "))
house(hx, hy, xrel, yrel)
house(hx + 0.3, hy, xrel, yrel)
house(hx + 0.6, hy, xrel, yrel)
plt.show()