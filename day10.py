import numpy as np
import math
with open('day10input.txt') as f:
    lines = f.read().split('\n')
x_range = 21
y_range = 21
point_vals = []
def get_num_of_points(point):
    angles = []
    for y in range(y_range):
        for x in range(x_range):
            if [x, y] != point and lines[y][x] == '#':
                if x == point[0]:
                    angle_to = math.pi/2.0 if y > point[1] else 3*math.pi/2.0
                else:
                    angle_to = math.atan((y - point[1])/(x - point[0]))
                if x < point[0]:
                    angle_to += math.pi
                if angle_to not in angles:
                    angles.append(angle_to)
    return len(angles)
for y in range(y_range):
    point_vals.append([])
    for x in range(x_range):
        if lines[y][x] == '#':
            point_vals[y].append(get_num_of_points([x,y]))
        else:
            point_vals[y].append(0)
max_val = point_vals[0][0]
index = [0,0]
for y in range(y_range):
    for x in range(x_range):
        if point_vals[y][x] > max_val:
            max_val = point_vals[y][x]
            index = [x, y]
print(index, max_val)
