# baekjun problem no.1920

import sys

n = int(sys.stdin.readline())
nums_n = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
nums_m = list(map(int,sys.stdin.readline().split()))

for _ in nums_m:
    print(1) if _ in nums_n else print(0)