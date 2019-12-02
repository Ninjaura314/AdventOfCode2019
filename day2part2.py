with open('day2input.txt') as f:
    data = [int(n) for n in f.read().split(',')]
og_data = data.copy()
desired = 19690720
for i in range(1,100):
    for j in range(1,100):
        ci = 0
        data = og_data.copy()
        data[1] = i
        data[2] = j
        while data[ci] != None and ci < len(data) and data[ci] != 99:
            if data[ci] == 1:
                data[data[ci+3]] = data[data[ci+1]] + data[data[ci+2]]
            else:
                data[data[ci+3]] = data[data[ci+1]] * data[data[ci+2]]
            ci += 4
        if data[0] == desired:
            print(f'{(100*data[1])+data[2]}')
            break
