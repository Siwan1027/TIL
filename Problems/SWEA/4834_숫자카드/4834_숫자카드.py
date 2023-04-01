# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
"""
1. 테스트 회수 입력
2. 카드 장수 N
3. N개의 숫자가 여백 없이 주어짐
4. 그 중에서 가장 많은 카드 숫자와 장수 차례 출력
5. 출력 양식은 # 테스트 넘버 카드 숫자 카드 장수
6. 문자열을 리스트로 변환 후 카운트로 [0] 부터 셈
7. 변수 tmp(카드 숫자), cnt(카드 장수)
8. 첫번째 카드 장수를 기본으로 설정, 만약 모든 카운트가 1일 경우 tmp = [-1], cnt = 1
9. 두번째 카드부터 count 값이 기본 저장된 값보다 클 경우 tmp, cnt 갱신

3
5
49679   #1 9 2
5
08271   #2 8 1
10
7797946543  #3 7 3
"""
T = int(input())

for cs in range(T):
    length = int(input())
    nums = input()
    numbers = list(nums)
    cnt, tmp = numbers.count(numbers[-1]), numbers[-1]
    for i in numbers:
        if numbers.count(i) > cnt:
            cnt = numbers.count(i)
            tmp = i
        else:
            pass
    if cnt == 1:
        tmp = max(numbers)
    print(f'#{cs+1}', tmp, cnt)

