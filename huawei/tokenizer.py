from collections import defaultdict

text = input()
n = int(input())
token_dict = defaultdict(int)
for _ in range(n):
    k,v = input().split()
    token_dict[k] = int(v)

m = int(input())

trans = defaultdict(int)
for _ in range(m):
    row = input().split()
    score = row[-1]
    words = " ".join(row[:-1])
    trans[words] = int(score)

# compute
max_score = -1e3
way = []
def dfs(s):
    global max_score
    if s == "":
        ans = 0
        for word in way:
            ans += token_dict[word]
        for i in range(1, len(way)):
            ans += trans[way[i-1] + " " + way[i]]
        max_score = max(ans, max_score)
        return

    for token in token_dict.keys():
        if s.startswith(token):
            way.append(token)
            dfs(s[len(token):])
            way.pop()
    return

dfs(text)
result = 0 if max_score == -1e3 else max_score
print(result)





