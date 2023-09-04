# baekjun problem no.11650
import sys


# 입력받을 값의 개수
n = int(sys.stdin.readline())
# 입력받은 값을 저장할 리스트
coors = list(range(0,n))

# 정해진 횟수만큼 입력받아 리스트에 저장
for i in range(n):
    # 받은 문자열을 분할, 형변환하여 리스트에 저장
    coors[i] = list(map(int, sys.stdin.readline().split()))

# python sort() 메소드는 기본적으로 [0][0]의 값과 [1][0]의 값이 같은 경우 [0][1]의 값과 [1][1]의 값을 비교하여 오름차순 정렬
coors.sort()

for i in coors:
    print(i[0], i[1])