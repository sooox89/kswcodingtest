# 백준 1267번
# 영식 Y : 30초 마다 10원씩 29초까지 10원 , 30초부터 59초 : 10원 추가
# 민식 M : 60초 마다 15원씩 59초까지 15원 , 60초부터 119초 : 15원 추가

from sys import stdin
N = int(input())
sec = list(map(int, stdin.readline().split()))
y = 0
m = 0
for i in sec:
    y += i//30 * 10 + 10
    m += i//60 * 15 + 15
if y > m:
    print('M',m)
elif y < m:
    print('Y',y)
else:
    print('Y M',y)

