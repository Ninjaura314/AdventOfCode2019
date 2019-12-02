with open('day1input.txt') as f:
    lines = [int(l) for l in f.read().split('\n')[:-1]]
def get_fuel(n):
    return int(n/3)-2
part = input('Part 1 or 2?: ')
ls = []
for l in lines:
    ls.append(get_fuel(l))
    if part == '2':
        cf = get_fuel(get_fuel(l))
        while cf > 0:
            ls.append(cf)
            cf = get_fuel(cf)
print(f'Sum of all fuel is {sum(ls)}')
