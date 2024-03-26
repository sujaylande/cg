import matplotlib.pyplot as plt

def reflect(lx,ly,id) :
    refx, refy = [], []
    for x, y in zip(lx, ly) :
        rx = x*id[0][0] + y*id[1][0] + id[2][0]
        refx.append(rx)
        ry = x*id[1][0] + y*id[1][1] + id[2][1]
        refy.append(ry)
    return refx, refy

lx, ly = [6,8,4,3], [7,8,8,4]
# print("Enter coordinates of Line : ")
# for i in range(2) :
#     x = int(input("x" + str(i + 1) + " : "))
#     y = int(input("y" + str(i + 1) + " : "))
#     lx.append(x)
#     ly.append(y)

id = [[0,1,0],[1,0,0],[0,0,1]]

refx, refy = reflect(lx,ly,id)
plt.plot(lx,ly,marker = '+')
plt.plot(refx,refy, marker = '*')
plt.show()