# baekjun problem no.11403

import sys
input = sys.stdin.readline

n = int(input())
graph = [ list(map(int, input().split())) for _ in range(n) ]

def dfs(i):
    for j in range(n):
        if result[j] == 0 and graph[i][j] == 1:
            result[j] = 1
            dfs(j)

for x in range(n):
    result = [ 0 for _ in range(n)]
    dfs(x)
    print(*result)