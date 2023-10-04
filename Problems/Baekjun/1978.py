# baekjun problem no.4949

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

for num in nums:
    for _ in range(2,num):
        if num 