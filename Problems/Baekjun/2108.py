# baekjun problem no.2108

import sys
# 파이썬 통계 내장모듈
from statistics import median, mean
# 파이썬 카운터 내장모듈
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()
# 최빈값 구하기 + 조건문
mode = Counter(nums). most_common()
if len(mode) > 1:
    if mode[0][1] == mode[1][1]:
        mode = mode[1][0]
    else:
        mode = mode[0][0]
else:
    mode = mode[0][0]

print(round(mean(nums)))
print(median(nums))
print(mode)
print(max(nums) - min(nums))