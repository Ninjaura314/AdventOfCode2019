with open('day5input.txt') as f:
    data = [int(i) for i in f.read().split(',')]
input_num = int(input('Input number: '))
current_index = 0
#data = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
#data = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
while current_index < len(data):
    operator = data[current_index]
    if operator == 99 or operator == 99999:
        break
    if operator < 10:
        if operator == 1:
            data[data[current_index+3]] = data[data[current_index+1]] + data[data[current_index+2]]
            current_index += 4
            continue
        elif operator == 2:
            data[data[current_index+3]] = data[data[current_index+1]] * data[data[current_index+2]]
            current_index += 4
            continue
        elif operator == 3:
            data[data[current_index+1]] = input_num
            current_index += 2
            continue
        elif operator == 4:
            data[0] = data[data[current_index+1]]
            current_index += 2
            continue
        elif operator == 5:
            if data[data[current_index+1]] != 0:
                current_index = data[data[current_index+2]]
            else:
                current_index += 3
            continue
        elif operator == 6:
            if not data[data[current_index+1]]:
                current_index = data[data[current_index+2]]
            else:
                current_index += 3
            continue
        elif operator == 7:
            data[data[current_index+3]] = int(data[current_index+1]<data[current_index+2])
            current_index += 4
            continue
        elif operator == 8:
            data[data[current_index+3]] = int(data[current_index+1]==data[current_index+2])
            current_index += 4
            continue
    operator_string = str(operator)
    while len(operator_string) < 5:
        operator_string = '0' + operator_string
    #print(operator_string)
    modes = [int(operator_string[2-i]) for i in range(3)]
    #print(modes)
    opcode = int(str(operator)[-1])
    if any(opcode == i for i in [1,2,5,6,7,8]):
        first_value = data[data[current_index+1]] if not modes[0] else data[current_index+1]
        second_value = data[data[current_index+2]] if not modes[1] else data[current_index+2]
    if opcode == 1:
        data[data[current_index+3]] = first_value + second_value
    elif opcode == 2:
        data[data[current_index+3]] = first_value * second_value
    elif opcode == 3:
        data[data[current_index+1]] = input_num
        current_index += 2
        continue
    elif opcode == 4:
        data[0] = data[data[current_index+1]]
        current_index += 2
        continue
    elif opcode == 5:
        if first_value != 0:
            current_index = second_value
        else:
            current_index += 3
        continue
    elif opcode == 6:
        if not first_value:
            current_index = second_value
        else:
            current_index += 3
        continue
    elif opcode == 7:
        data[data[current_index+3]] = int(first_value<second_value)
    elif opcode == 8:
        data[data[current_index+3]] = int(first_value==second_value)
    current_index += 4

print(f'{data[0]}')
