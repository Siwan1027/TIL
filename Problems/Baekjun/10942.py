# baekjun problem no.10942

import sys

input = sys.stdin.readline

n = int(input())
nums = []
result = 1
for _ in range(n):
    nums.append(int(input()))
t = int(input())
for _ in range(t):
    s, e = map(int,input().strip().split())
    t_nums = nums[s:e]
    if len(t_nums) == 1:
        print(1)
    else:
        for i in range(len(t_nums)):
            if t_nums[i] != t_nums[-i]:
                result = 0
    