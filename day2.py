with open('day2input.txt') as f:
    data = [int(n) for n in f.read().split(',')]
current_index = 0
data[1] = 12
data[2] = 2
while data[current_index] != None and current_index < len(data) and data[current_index] != 99:
    if data[current_index] == 1:
        data[data[current_index+3]] = data[data[current_index+1]] + data[data[current_index+2]]
    else:
        data[data[current_index+3]] = data[data[current_index+1]] * data[data[current_index+2]]
    current_index += 4
print(f'{data[0]}')
