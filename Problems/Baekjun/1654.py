# baekjun problem no.1654

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stack = deque()
for _ in range(n):
    if n > stack[0]:
        