n, m, p, k = list(map(int, input().split()))

exp_p = list(map(float, input().split()))
if m < p:
    print("error")
    exit()
if not n % m == 0 or n < k:
    print("error")
    exit()
if len(exp_p) < k:
    print("error")
    exit()

length = int(n / m)
label = 0

class Group():
    def __init__(self, arr, index_list):
        self.arr = arr
        self.mx = max([float(p) for p in arr])
        self.label = zip(arr, index_list)

groups = []
arr = []
index = 0
for prob in exp_p:
    arr.append(prob)
    if len(arr) == length:
        group = Group(arr, range(index, index+length))
        groups.append(group)
        arr = []
        index += length

groups.sort(key=lambda x:x.mx, reverse=True)
groups = groups[:p]


labels = []
for group in groups:
    labels += group.label

labels.sort(key = lambda x : x[0], reverse = True)
labels = labels[:k]

results = [index for (prob, index) in labels]
results.sort()

s = str(results[0])
for r in results[1:]:
    s += " " + str(r)
print(s)

