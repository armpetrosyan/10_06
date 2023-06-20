def rotate_by(g, h):
    for i in range(h):
        a = g[i]
        g[i] = g[len(g) - 1 - i]
        g[len(g) - 1 - i] = a
    return g


array_size = int(input('Array size: '))
position = int(input('Positional rotation: '))


arr = []

for j in range(0, array_size):
    item = int(input())
    arr.append(item)


rotate_by(arr, position)

print(arr)
