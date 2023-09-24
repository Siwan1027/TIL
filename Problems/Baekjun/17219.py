# baekjun problem no.17219

import sys

n,m = map(int, sys.stdin.readline().split())
memo = dict()
for _ in range(n):
    key,value = sys.stdin.readline().split()
    memo[key] = value
for _ in range(m):
    key = sys.stdin.readline().strip()
    print(memo[key])