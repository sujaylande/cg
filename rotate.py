import matplotlib.pyplot as plt
import math
def rotate_point(x, y, angle):
    angle_rad = math.radians(angle)
    new_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    new_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return new_x, new_y

def rotate_line(x1, y1, x2, y2, angle):
    x1_rotated, y1_rotated = rotate_point(x1, y1, angle)
    x2_rotated, y2_rotated = rotate_point(x2, y2, angle)
    return x1_rotated, y1_rotated, x2_rotated, y2_rotated

# Original line points
x1, y1 = 40, 60
x2, y2 = 80, 90

# Angle of rotation
angle = 45

# Rotate the line
x1_rotated, y1_rotated, x2_rotated, y2_rotated = rotate_line(x1, y1, x2, y2, angle)

print("Original line:", (x1, y1), "->", (x2, y2))
print("Rotated line:", (x1_rotated, y1_rotated), "->", (x2_rotated, y2_rotated))
plt.plot([x1,x2],[y1,y2])
plt.plot([x1_rotated,  x2_rotated],[y1_rotated, y2_rotated])
plt.show()
