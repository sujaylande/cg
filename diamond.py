import math
import matplotlib.pyplot as plt
# Define the vertices of the square
sqx, sqy = [], []
print("Enter vertices of Square : ")
for i in range(4) :
    x = int(input("x"+str(i+1)+" : "))
    y = int(input("y" + str(i + 1) + " : "))
    sqx.append(x)
    sqy.append(y)
sqx.append(sqx[0])
sqy.append(sqy[0])
# Find the center of the square
xcent = sum(x for x in sqx) / len(sqx)
ycent = sum(y for y in sqy) / len(sqy)
# Rotate each point around the center to form a diamond
dx, dy = [], []
for i in range(len(sqx)):
    # Translate the coordinates relative to the center
    xtrans = sqx[i] - xcent
    ytrans = sqy[i] - ycent
    # Rotate the translated coordinates by 45 degrees (pi/4 radians)
    xrot = xtrans * math.cos(math.pi/4) - ytrans * math.sin(math.pi/4)
    yrot = xtrans * math.sin(math.pi/4) + ytrans* math.cos(math.pi/4)
    # Translate the rotated coordinates back relative to the original center
    x = xrot + xcent
    y = yrot + ycent
    dx.append(x)
    dy.append(y)

plt.plot(dx, dy)
plt.plot(sqx,sqy)
plt.show()
