# baekjun problem no.1620

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
podocs_index = []
podocs = {}
for _ in range(n):
    pname = input().strip()
    podocs_index.append(pname)
    podocs[pname] = _+1


for _ in range(m):
    target = input().strip()
    try:
        print(podocs_index[int(target)-1])
    except:
        print(podocs[target])