# 상자넣기
from sys import stdin
n = int(input())
array = list(map(int, stdin.readline().split()))
dp = [1] * n

for i in range (1,n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# 앞의 상자가 현재 상자보다 작으면 담고있는 상자의 개수 +1
