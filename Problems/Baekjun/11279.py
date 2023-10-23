# baekjun problem no.2164

import sys, heapq

input = sys.stdin.readline

n = int(input())
hq = []
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(hq, -x)
    else:
        if len(hq):
            print(-heapq.heappop(hq))
        else:
           print(0)