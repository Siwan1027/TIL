# baekjun problem no.2798

import sys

n, m = map(int,sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

result_lst = []

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            total = nums[i] + nums[j] + nums[k]
            if total > m:
                continue
            else:
                result_lst.append(total)

print(max(result_lst))