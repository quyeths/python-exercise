A = [31, 41, 59, 26, 41, 58]
ALength = len(A)


def sort(arr):
    for i in range(ALength - 1):
        for j in range(i + 1, ALength):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print(sort(A))
