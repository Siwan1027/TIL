# baekjun problem no.1978

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
cnt = 0

for num in nums:
    is_prime = True
    if num > 1:
        for _ in range(2,num):
            if num % _ == 0 :
                is_prime = False
                break
        if is_prime:
            cnt+=1

print(cnt)