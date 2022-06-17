n, m, k = [int(i) for i in input().split()]

customerInfo = []
for _ in range(k):
    t, d, a = [int(i) for i in input().split()]
    customerInfo.append([t, d, a])

res = []
hashmap = []


def solution(i, n, m, customerInfo, hashmap):
    # n: int
    # m: int
    # customerInfo: List[int]
    if i == k:
        return
    checkNM = hashmap.copy()
    for start in range(len(checkNM)):
        if customerInfo[i][0] - checkNM[start][1] > 0:
            if checkNM[start][2] == 1:
                n += 1
                m += 1
            else:
                n += 1
            hashmap.remove(checkNM[start])

    if customerInfo[i][2] == 1:
        if n - 1 > -1 and m - 1 > -1:
            n -= 1
            m -= 1
            res.append("Yes")
            hashmap.append(customerInfo[i])
        else:
            res.append("No")
    else:
        if n - 1 > -1 and m > -1:
            n -= 1
            res.append("Yes")
            hashmap.append(customerInfo[i])
        else:
            res.append("No")
    solution(i + 1, n, m, customerInfo, hashmap)
    return res


solution(0, n, m, customerInfo, hashmap)

for i in range(len(res)):
    print(res[i])
