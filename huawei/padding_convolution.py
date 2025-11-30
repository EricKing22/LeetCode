import numpy as np

m,n = map(int, input().split())

p = int((n-1 + m - n) / 2)

kernal = []
for _ in range(m):
    kernal.append(list(map(float, input().split())))

img = []
for _ in range(n):
    img.append(list(map(float, input().split())))

height, width = len(img), len(img[0])
for _ in range(p):
    img = [[0] * width] + img + [[0] * width]

img = [ [0]*p + row + [0]*p for row in img]




kernal = np.array(kernal)
img = np.array(img)

result = [[0] * n for _ in range(n)]

for i in range(len(result)):
    for j in range(len(result[0])):
        ans = np.sum(img[i:i+m,j:j+m] * kernal)
        result[i][j] = int(ans)

for row in result:
    print(" ".join([str(item) for item in row]))
