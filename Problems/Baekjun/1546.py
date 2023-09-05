# baekjun problem no.1546

# 나의 풀이

import sys

n = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
result = float()
for i in scores:
    i = i/max(scores)*100
    result += i

print(result/n) 