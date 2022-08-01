import math
def isPrime(n):
    if n < 2:
        return False
    maxRange = int(math.sqrt(n)) + 1
    for i in range(2, maxRange):
        if n % i == 0:
            return False
    return True

N = int(input())
nums = list(int(num) for num in input().strip().split())[:N]
newNums = sorted(nums)
numCheck = int(math.sqrt(newNums[-1])) + 1
count = 0

# ayza la binh phuong cua 1 so nguyen to
# -> kiem tra tu so 2 cho den can bac 2 cua so lon nhan trong mang
# neu so kiem tra la so nguyen to va ninh phuong so kiem tra co trong mang thi count += 1

for i in range(2, numCheck):
    if isPrime(i) and i * i in nums:
        count += 1
print(count)

# kiem tra tu so can bac 2 cua so lon nhat trong mang + 1
# neu so check la so nguyen to va binh phuong so check > so lon nhat trong mang
# in ket qua va ngung vong lap
while True:
    if isPrime(numCheck) and numCheck * numCheck > newNums[-1]:
        print(numCheck * numCheck)
        break
    numCheck += 1
