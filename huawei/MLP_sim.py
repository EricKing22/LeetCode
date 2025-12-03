rows =  input().split(";")
x = []
for row in rows:
    x.append(list(map(int,row.split(","))))

print(x)

ctr_cvr_rows = input().split(";")
ctr_cvr = []
for row in ctr_cvr_rows:
    ctr_cvr.append(list(map(int,row.split(","))))

iteration = int(input())
lr = float(input())
alpha = float(input())

# forward
