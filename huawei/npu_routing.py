n = int(input())
m = int(input())

lengths = map(int, input().split())
lengths = sorted(lengths, reverse=True) # 从大到小

way = [ 0  for _ in range(n)]

# class Group():
#     def __init__(self, sizes):
#         self.sum = sum(sizes)
#         self.sizes = sizes
#
#     def add(self, num):
#         self.sizes += num
#         self.sum += num

for length in lengths:
    way.sort()
    way[0] += length

print(max(way))

