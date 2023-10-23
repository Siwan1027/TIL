# baekjun problem no.1764

import sys

input = sys.stdin.readline
n,m = map(int,input().split())

no_seen = set()
no_heard = set()

for _ in range(n):
    no_seen.add(input().strip())

for _ in range(m):
    no_heard.add(input().strip())

# 사전순이다..
result = sorted(list(no_seen & no_heard))

print(len(result))
for name in result:
    print(name)