# baekjun problem no.10942

import sys

input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
t = int(input())
for _ in range(t):
    s, e = map(int,input().strip().split())
    if len(nums[s:e]) == 1:
        print(1)
    if len(nums[s:e]) > 1:
        for _ in range(len(nums[s:e])):
            t_nums = nums[s:e]
            t_nums[_]