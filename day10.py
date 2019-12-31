import numpy as np
import math
with open('day10input.txt') as f:
    lines = f.read().split('\n')
x_range = 21
y_range = 21
point_vals = []
def get_angles(point, get_points=False):
    angles = []
    points = []
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
                    points.append([x,y])
    if not get_points:
        return angles
    else:
        return angles, points
for y in range(y_range):
    point_vals.append([])
    for x in range(x_range):
        if lines[y][x] == '#':
            point_vals[y].append(len(get_angles([x,y])))
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
base_location = index
def get_points_clockwise():
    angles, points = get_angles(base_location, get_points=True)
    angle_dict = {}
    for i in range(len(angles)):
        angle_dict[(math.pi/2.0)-angles[i]] = points[i]
    angle_dict = sorted(angle_dict.items())
    return angle_dict
asteroids_by_angle = get_points_clockwise()
counter = 0
print(asteroids_by_angle[-22])