with open('day2input.txt') as f:
    data = [int(n) for n in f.read().split(',')]
ci = 0
data[1] = 12
data[2] = 2
while data[ci] != None and ci < len(data) and data[ci] != 99:
    if data[ci] == 1:
        data[data[ci+3]] = data[data[ci+1]] + data[data[ci+2]]
    else:
        data[data[ci+3]] = data[data[ci+1]] * data[data[ci+2]]
    ci += 4
print(f'{data[0]}')
