# 1로 만들기

n = int(input())
answer =[]
dp = [0] * (n+1)
answer = []



for i in range(2,n+1):
    # i-1이 1이 되는데 필요한 연산 + 1회
    dp[i] =dp[i-1] +1

    if i % 3 ==0:
        # (위의 dp[i] 값) vs (i를 3으로 나누어 1로 만드는데 필요한 최소 연산 수 +1회)
        dp[i] = min(dp[i], dp[i // 3] + 1)

    if i % 2 ==0:
        dp[i] = min(dp[i], dp[i // 2] + 1)


print(dp[n])