# baekjun problem no.10816

import sys

input = sys.stdin.readline

# 입력 받기
n = int(input())
nums = list(map(int, input().split()))
t = int(input())
targets = list(map(int, input().split()))

# 1번째 풀이
# for _ in targets:
#     result.append(nums.count(_))

# for _ in result:
#     print(_, end = ' ')

# 2번째 풀이
# nums_dict = {x: nums.count(x) for x in nums}
# for _ in targets:
#     try:
#         print(nums_dict[_], end = ' ')
#     except:
#         print(0, end = ' ')

# 3번째 풀이
nums_dict = {}

for num in nums:
    if num in nums_dict:
        nums_dict[num] += 1
    else:
        nums_dict[num] = 1

for _ in targets:
    try:
        print(nums_dict[_], end = ' ')
    except:
        print(0, end = ' ')