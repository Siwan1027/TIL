# baekjun problem no.10773

import sys
from collections import deque

k = int(sys.stdin.readline())
stack = deque()
for i in range(k):
    n = int(sys.stdin.readline())
    if n:
        stack.append(n)
    else:
        stack.pop()

print(sum(stack))