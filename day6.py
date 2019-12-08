with open('day6input.txt') as f:
    lines = f.read().split('\n')[:-1]
orbits = {}
bodies = []
subs = []
pars = []
for line in lines:
    base, orbiter = line.split(')')
    if base not in bodies:
        bodies.append(base)
    if orbiter not in bodies:
        bodies.append(orbiter)
    if base not in orbits.keys():
        orbits[base] = []
    orbits[base].append(orbiter)
to_check = []
for body in bodies:
    if body not in orbits.keys():
        subs.append(body)
    else:
        to_check.append(body)
def parse_map(start_point):
    if start_point not in orbits.keys():
        return start_point
    current_list = {}
    children = orbits[start_point]
    remove = []
    to_check.remove(start_point)
    for child in children:
        if not any(child in orbits[k] for k in to_check):
            current_list[child] = parse_map(child)
        else:
            remove.append(child)
    for r in remove:
        orbits[start_point].remove(child)
    return {start_point: current_list}
star_map = parse_map('COM')
def get_orbits(current_map, current_place):
    if type(current_map) is str:
        return 0
    sum_of_orbits = 0
    for k in current_map.keys():
        sum_of_orbits += current_place + get_orbits(current_map[k], current_place+1)
    return sum_of_orbits
print(get_orbits(star_map,1))
