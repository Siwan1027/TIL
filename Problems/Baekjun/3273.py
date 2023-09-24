# https://www.acmicpc.net/problem/3273

"""
1. 수열의 크기 최대 100000만개
2. 수열
3. 타겟 값

수열의 첫번째부터 수열안에 값들과 더해서 타겟값이 되는 수가 있는지 찾아야 함
x - nums[i] = y
즉 y 값이 주어진 수열 내에 존재 하는지 판단하여 카운트
python 리스트 구조에서 in 연산자 사용하려함 in 연산자의 시간 복잡도는 O(n)
set, dictionart 에서는 O(1) 부터 O(n)
반복된 탐색 작업을 해야하는 경우 set,dict 형이 유리함

여기서 sort 구현이 귀찮기 때문에 quick sort 기반 내장 함수 사용
후에 set 자료형으로 변환

그 후에는 이진 탐색 방식으로 up down 게임진행하듯이 하면 될 듯
nums[len(nums)/2] 와 비교
크다면 nums[(len(nums)/2+len(nums))/2)] 반복
작다면 nums[len(nums)/2,4,6,8]


"""
import sys

n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().strip().split())))
t = int(sys.stdin.readline())
# target 에 적합한 해의 갯수 카운터
cnt = 0
# 이진탐색 구현
# 쌍으로 나타내기 때문에 set을 사용할까 했는데 리스트의 절반까지만 탐색하는 방식으로 구현 set으로도 가능할지도?
for num in nums:
    x = t - num
    first, last = 0, n-1
    while first <= last:
        mid = (first+last)//2
        if nums[mid] == x:
            cnt += 1
            break
        # 리스트 중앙값이 더 크다면 0 ~ 중앙-1 까지 범위에서 가운데 값을 확인
        if nums[mid] > x:
            last = mid-1
        # 리스트 중앙값이 더 작다면 중앙 +1 ~ 마지막까지 범위에서 가운데 값을 확인
        else:
            first = mid+1

# 쌍이기 때문에 중복값 제거하고 절반만 출력
# 리스트의 절반만 하니까 실패함.. 왜...?
print(cnt//2)