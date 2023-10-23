# baekjun problem no.2164

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(list(range(1, n+1)))
while len(q) > 1:
    q.popleft()
    q.rotate(-1)

print(q[0])

# 미쳤다.. 
# n,m = int(input()), 1
# while m<n: # O(logn)
#     m *= 2
# print(2*n-m)