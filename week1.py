# 100 80 70 60
# 80 70 80 90

from sys import stdin

MG_info, MG_math, MG_science, MG_eng = map(int, stdin.readline().split())
# print(f'input: {MG_info, MG_math, MG_science, MG_eng}')
MS_info, MS_math, MS_science, MS_eng = map(int, stdin.readline().split())
# print(f'input: {MS_info, MS_math, MS_science, MS_eng}')

S = MG_info + MG_math + MG_science + MG_eng
T = MS_info + MS_math + MS_science + MS_eng

if S < T:
    print(T)
else:
    print(S)
