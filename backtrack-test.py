coins = [5000, 2000, 1000, 500, 200]
N = 2000
M = 3
res = []


def dfs(i, cur, total, count):
    if total == N:
        res.append(cur.copy())
        return
    if i >= len(coins) or total > N or count == M:
        return
    cur.append(coins[i])
    dfs(i, cur, total + coins[i], count + 1)
    cur.pop()
    dfs(i + 1, cur, total, count)


dfs(0, [], 0, 0)
print(f"co {len(res)} phuong an.")
for i in range(len(res)):
    print(f"phuong an {i + 1}: {res[i]}")
