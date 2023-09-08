# baekjun problem no.18110

import sys
from collections import deque


k,n = map(int, sys.stdin.readline().split())

nums = deque()
for i in range(1,k+1):
    nums.append(i)
result = []

while nums:
    for i in range(n-1):
        nums.append(nums.popleft())
    result.append(nums.popleft())

print('<', end ='')
for i in range(len(result)-1):
    print(f'{result[i]}, ', end = '')
print(f'{result[-1]}>')