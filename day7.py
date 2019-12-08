with open('day7input.txt') as f:
    nums = [int(i) for i in f.read().split(',')]
indexes = [0 for i in range(5)]
amp_outputs = [[] for i in range(5)]
input_queue = [[] for i in range(5)]
def intcode(data, phase_num, input_num, amp_num, part_two=False, init_value=False, loops=0):
    current_index = indexes[amp_num]
    first_time = True
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
        if any(opcode == i for i in [1,2,5,6,7,8]):
            first_value = data[data[current_index+1]] if not modes[0] else data[current_index+1]
            second_value = data[data[current_index+2]] if not modes[1] else data[current_index+2]
        if opcode == 1:
            data[data[current_index+3]] = first_value + second_value
        elif opcode == 2:
            data[data[current_index+3]] = first_value * second_value
        elif opcode == 3:
            if not part_two:
                if first_time:
                    data[data[current_index+1]] = phase_num
                    first_time = False
                else:
                    data[data[current_index+1]] = input_num
                current_index += 2
            else:
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
            if part_two:
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
        elif opcode == 8:
            data[data[current_index+3]] = int(first_value==second_value)
        current_index += 4
    if broken_by_wait:
        indexes[amp_num] = current_index
        return None
    return data[0]
from itertools import permutations
num_options = [''.join(p) for p in permutations('01234')]
results = []
for n in num_options:
    current_result = 0
    past_result = [0]
    for i in range(5):
        past_result.append(intcode(nums.copy(), int(n[i]), past_result[-1],i))
    results.append(past_result[-1])
num_options_part_2 = [''.join(p) for p in permutations('56789')]
print(max(results))
part_2_results = []
for n in num_options_part_2:
    amp_finals = [None for i in range(5)]
    amp_outputs = [[] for i in range(5)]
    input_queue = [[int(n[i])] for i in range(5)]
    input_queue[0].append(0)
    first_loop = True
    indexes = [0,0,0,0,0]
    reps = 0
    while None in amp_finals:
        #print(indexes)
        for i in range(5):
            if first_loop and i == 0:
                amp_finals[i] = intcode(nums.copy(), int(n[i]), 0, i, part_two=True, init_value=True, loops=reps)
                first_loop = False
            else:
                amp_finals[i] = intcode(nums.copy(), int(n[i]), 0, i, part_two=True, loops=reps)
        reps += 1
    part_2_results.append(amp_finals[-1])
print(max(part_2_results))
