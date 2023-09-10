# baekjun problem no.11399

import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(' ')))

result = int()

nums.sort()
for i in range(n):
    result += sum(nums[:i+1])


print(result)