# baekjun problem no.4153

import sys

t = 1

while (t):
    nums = list(map(int, sys.stdin.readline().strip().split()))
    nums.sort()
    if (nums[0] == 0 & nums[1] == 0 & nums[2] == 0):
        break
    print('right') if nums[0]*nums[0] + nums[1]*nums[1] == nums[2]*nums[2] else print('wrong')
