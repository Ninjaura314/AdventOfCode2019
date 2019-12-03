with open('day1input.txt') as f:
    lines = [int(line) for line in f.read().split('\n')[:-1]]
def get_fuel(n):
    return int(n/3)-2
part = input('Part 1 or 2?: ')
line_s = []
for line in lines:
    line_s.append(get_fuel(line))
    if part == '2':
        current_fuel = get_fuel(get_fuel(line))
        while current_fuel > 0:
            line_s.append(current_fuel)
            current_fuel = get_fuel(current_fuel)
print(f'Sum of all fuel is {sum(line_s)}')
