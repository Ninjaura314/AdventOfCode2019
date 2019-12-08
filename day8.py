with open('day8input.txt') as f:
    nums = [int(i) for i in f.read()[:-1]]
layers = [[]]
width = 25
height = 6
current_row = -1
for i in range(len(nums)):
    if i % 25 == 0:
        if current_row == 5:
            layers.append([])
            current_row = -1
        current_row += 1
        layers[-1].append([])
    layers[-1][-1].append(nums[i])
zero_counts = [0 for i in range(len(layers))]
one_counts = [0 for i in range(len(layers))]
two_counts = [0 for i in range(len(layers))]
for i in range(len(layers)):
    for j in range(len(layers[i])):
        zero_counts[i] += layers[i][j].count(0)
        one_counts[i] += layers[i][j].count(1)
        two_counts[i] += layers[i][j].count(2)
best_image_index = zero_counts.index(min(zero_counts))
print(one_counts[best_image_index] * two_counts[best_image_index])
import numpy as np
import matplotlib.pyplot as plt
layers_np = np.array(layers)
image_out = np.full(layers_np[0].shape, -1)
for i in range(len(layers)):
    for j in range(height):
        for k in range(len(layers[i][j])):
            if layers_np[i, j, k] != 2 and image_out[j,k] == -1:
                image_out[j, k] = layers_np[i, j, k]
plt.imshow(image_out,'gray')
plt.show()
