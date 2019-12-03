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
    bp = []
    if p1[0] == p2[0]:
        for i in range(1,abs(p2[1]-p1[1])):
            if p2[1] > p1[1]:
                bp.append([p1[0],p1[1]+i])
            else:
                bp.append([p1[0],p1[1]-i])
    else:
        for i in range(1,abs(p2[0]-p1[0])):
            if p2[0] > p1[0]:
                bp.append([p1[0]+i,p1[1]])
            else:
                bp.append([p1[0]-i,p1[1]])
    return bp
for w in range(2):
    for d in range(len(wire_moves[w])):
        move(w,wire_moves[w][d])
sbp = []
for i in range(len(wire_points[1]) - 1):
    sbp.append(between_points(wire_points[1][i],wire_points[1][i+1]))
matching_points = []
for i in range(len(wire_points[0])-1):
    cps = [wire_points[0][i],wire_points[0][i+1]]
    for j in range(len(wire_points[1])-1):
        nps = [wire_points[1][j],wire_points[1][j+1]]
        if ((nps[0][0] == nps[1][0]) and (cps[0][0] == cps[1][0])) or ((nps[0][1] == nps[1][1]) and (cps[0][1] == cps[1][1])):
            continue
        if nps[0][1] == nps[1][1]:
            if ((nps[0][0] < cps[0][0]) and (nps[1][0] > cps[0][0])) or ((nps[0][0] > cps[0][0]) and (nps[1][0] < cps[0][0])):
                cpb = between_points(cps[0],cps[1])
                spb = between_points(nps[0],nps[1])
                for c in cpb:
                    if c in spb:
                        matching_points.append(c)
                        break
        if nps[0][0] == nps[1][0]:
            if ((nps[0][1] < cps[0][1]) and (nps[1][1] > cps[0][1])) or ((nps[0][1] > cps[0][1]) and (nps[1][1] < cps[0][1])):
                cpb = between_points(cps[0],cps[1])
                spb = between_points(nps[0],nps[1])
                for c in cpb:
                    if c in spb:
                        matching_points.append(c)
                        break
def abs_sum(p):
    return abs(p[0]) + abs(p[1])
m_sums = []
for mp in matching_points:
    m_sums.append(abs_sum(mp))
print(f'{min(m_sums)}')
