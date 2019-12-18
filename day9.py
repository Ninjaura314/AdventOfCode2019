with open('day9input.txt') as f:
    nums = [int(i) for i in f.read().split(',')]
indexes = [0 for i in range(5)]
relative_bases = [0 for i in range(5)]
input_queue = [[] for i in range(5)]
input_queue[0].append(1)
memory = {i:0 for i in range(100000)}
for i in range(len(nums)):
    memory[i] = nums[i]
def intcode(data, amp_num):
    current_index = indexes[amp_num]
    broken_by_wait = False
    while current_index < len(data):
        operator = data[current_index]
        if operator == 99 or operator == 99999:
            break
        operator_string = str(operator)
        while len(operator_string) < 5:
            operator_string = '0' + operator_string
        #print(operator_string)
        modes = [int(operator_string[2-i]) for i in range(3)]
        #print(modes)
        opcode = int(str(operator)[-1])
        if any(opcode == i for i in [1,2,5,6,7,8,9]):
            if data[current_index+1] not in memory.keys():
                data[current_index+1] = 0
            if data[current_index+2] not in memory.keys():
                data[current_index+2] = 0
            if modes[0] == 1:
                first_value = data[current_index+1]
            elif modes[0] == 0:
                first_value = data[data[current_index+1]]
            else: # if modes[0] == 2
                first_value = data[data[current_index+1]+relative_bases[amp_num]]
            if modes[1] == 1:
                second_value = data[current_index+2]
            elif modes[1] == 0:
                second_value = data[data[current_index+2]]
            else: # if modes[0] == 2
                second_value = data[data[current_index+2]+relative_bases[amp_num]]
        if opcode == 1:
            data[data[current_index+3]] = first_value + second_value
            current_index += 4
        elif opcode == 2:
            data[data[current_index+3]] = first_value * second_value
            current_index += 4
        elif opcode == 3:
            if len(input_queue[amp_num]) == 0:
                broken_by_wait = True
            else:
                data[data[current_index+1]] = input_queue[amp_num].pop(0)
                current_index += 2
            if broken_by_wait:
                break
            else:
                continue
        elif opcode == 4:
            data[0] = data[data[current_index+1]]
            input_queue[(amp_num+1)%len(input_queue)].append(data[0])
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
            current_index += 4
        elif opcode == 8:
            data[data[current_index+3]] = int(first_value==second_value)
            current_index += 4
        elif opcode == 9:
            relative_bases[amp_num] += first_value
            current_index += 2
    if broken_by_wait:
        indexes[amp_num] = current_index
        return None
    return data[0]
print(intcode(memory.copy(), 0))
'''mem_copies = [memory.copy() for i in range(5)]
outs = [None for i in range(5)]
while None in outs:
    for i in range(5):
        outs[i] = intcode(mem_copies[i],i)
print(max(outs))'''
