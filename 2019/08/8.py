W = 25
H = 6

with open('8.txt') as f:
    data = f.read()

data = data[:-1]
data = list(map(int, data))

size = W * H
layers = len(data) // size

best_count = size + 1
best_layer = None

def get_data(layer):
    return data[layer * size:(layer + 1) * size]

for layer in range(layers):
    layer_data = get_data(layer)
    count = 0
    for pixel in layer_data:
        if pixel == 0:
            count += 1
    if count < best_count:
        best_count = count
        best_layer = layer

layer_data = get_data(best_layer)
count1 = 0
count2 = 0
for pixel in layer_data:
    if pixel == 1:
        count1 += 1
    elif pixel == 2:
        count2 += 1
print(count1 * count2)

image = [0] * size
for layer in range(0, layers)[::-1]:
    layer_data = get_data(layer)
    for i, pixel in enumerate(layer_data):
        if pixel == 2:
            continue
        image[i] = pixel

for row in range(H):
    print(image[row * W:(row + 1) * W])
