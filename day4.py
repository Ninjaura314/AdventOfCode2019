bottom = 367479
top = 893698
valid_count = 0
s_valid_count = 0
for i in range(bottom, top+1):
    current_string = str(i)
    separate_ints = [int(c) for c in current_string]
    valid = True
    for i in range(5):
        if separate_ints[i] > separate_ints[i+1]:
            valid = False
            break
    if all(str(i)*2 not in current_string for i in range(10)):
        valid = False
    if valid:
        valid_count += 1
        groups = {}
        for i in range(10):
            groups[str(i)] = 0
        for c in current_string:
            groups[c] += 1
        # TIL about the any function and the power therein
        if any(i == 2 for i in groups.values()):
            s_valid_count += 1

print(valid_count)
print(s_valid_count)
