# baekjun problem no.2292

import sys

input = sys.stdin.readline

n = int(input())

nums_group, nums_group_end = 1, 1

while n > nums_group:
    nums_group += 6 * nums_group_end
    nums_group_end += 1

print(nums_group_end)