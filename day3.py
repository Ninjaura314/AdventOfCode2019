with open('day3input.txt') as f:
    wire_inputs = f.read().split('\n')
wire_moves = [wire_inputs[0].split(','), wire_inputs[1].split(',')]
wire_points = [[[0,0]],[[0,0]]]
current_points = [[0,0],[0,0]]
def move(w,d):
    direction = d[0]
    distance = int(d[1:])
    next_point = []
    if direction == 'R':
        next_point = [current_points[w][0]+distance,current_points[w][1]]
    elif direction == 'L':
        next_point = [current_points[w][0]-distance,current_points[w][1]]
    elif direction == 'U':
        next_point = [current_points[w][0],current_points[w][1]+distance]
    elif direction == 'D':
        next_point = [current_points[w][0],current_points[w][1]-distance]
    wire_points[w].append(next_point)
    current_points[w] = next_point
def between_points(p1, p2):
    b_points = []
    if p1[0] == p2[0]:
        for i in range(1,abs(p2[1]-p1[1])):
            if p2[1] > p1[1]:
                b_points.append([p1[0],p1[1]+i])
            else:
                b_points.append([p1[0],p1[1]-i])
    else:
        for i in range(1,abs(p2[0]-p1[0])):
            if p2[0] > p1[0]:
                b_points.append([p1[0]+i,p1[1]])
            else:
                b_points.append([p1[0]-i,p1[1]])
    return b_points
for w in range(2):
    for d in range(len(wire_moves[w])):
        move(w,wire_moves[w][d])
matching_points = []
points_before = []
for i in range(len(wire_points[0])-1):
    current_point_s = [wire_points[0][i],wire_points[0][i+1]]
    for j in range(len(wire_points[1])-1):
        other_points = [wire_points[1][j],wire_points[1][j+1]]
        if ((other_points[0][0] == other_points[1][0]) and (current_point_s[0][0] == current_point_s[1][0])) or \
        ((other_points[0][1] == other_points[1][1]) and (current_point_s[0][1] == current_point_s[1][1])):
            continue
        if other_points[0][1] == other_points[1][1]:
            if ((other_points[0][0] < current_point_s[0][0]) and (other_points[1][0] > current_point_s[0][0])) or \
            ((other_points[0][0] > current_point_s[0][0]) and (other_points[1][0] < current_point_s[0][0])):
                current_points_between = between_points(current_point_s[0],current_point_s[1])
                second_points_between = between_points(other_points[0],other_points[1])
                for c in current_points_between:
                    if c in second_points_between:
                        points_before.append([current_point_s[0],other_points[0]])
                        matching_points.append(c)
                        break
        if other_points[0][0] == other_points[1][0]:
            if ((other_points[0][1] < current_point_s[0][1]) and (other_points[1][1] > current_point_s[0][1])) or \
            ((other_points[0][1] > current_point_s[0][1]) and (other_points[1][1] < current_point_s[0][1])):
                current_points_between = between_points(current_point_s[0],current_point_s[1])
                second_points_between = between_points(other_points[0],other_points[1])
                for c in current_points_between:
                    if c in second_points_between:
                        points_before.append([current_point_s[0],other_points[0]])
                        matching_points.append(c)
                        break
def abs_sum(p):
    return abs(p[0]) + abs(p[1])
m_sums = []
for mp in matching_points:
    m_sums.append(abs_sum(mp))
print(f'Part 1: {min(m_sums)}')
wire_distances = []
def get_wire_distance_to(p,fp,w):
    current_sum = 0
    index = wire_points[w].index(p)
    for i in range(index):
        current_sum += int(wire_moves[w][i][1:])
    current_sum += abs(fp[0]-p[0]) + abs(fp[1]-p[1])
    return current_sum
for i in range(len(matching_points)):
    wire_distances.append(get_wire_distance_to(points_before[i][0], matching_points[i], 0) + get_wire_distance_to(points_before[i][1], matching_points[i], 1))
print(f'Part 2: {min(wire_distances)}')
