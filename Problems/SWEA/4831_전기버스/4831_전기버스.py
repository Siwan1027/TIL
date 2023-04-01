"""
1. 0~N 번 정류장까지 운행하는 버스
2. 한번에 최대 갈 수 있는 거리 K
3. 충전기가 설치된 M개의 정류장 번호(index)가 주어짐
4. 최소 충전 회수를 출력하라
5. 충전기 설치가 잘못돼 도착할 수 없으면 0을 출력
6. 테스트 회수 T
7. K(최대운행거리), N(종점), M(충전기가 설치된 정류장)
8. 출력 양식 print(f'#{cs+1}', cnt)
9. 충전소 사이 거리를 알고 있기에 충전소 간 가장 거리가 먼 곳(distance)을 먼저 계산
10. 만약 K 가 distance 보다 작다면 0을 리턴
11. K는 한 칸 갈때마다 -1
12. 다음 충전소 - 지금 충전소 > K 면 cnt += 1
13. N/M < K 면 절대 못가는게 아닌가??
3
3 10 5
1 3 5 7 9   #1 3
3 10 5
1 3 7 8 9   #2 0
5 20 5
4 7 9 14 17 #3 4
"""

T = int(input())
for cs in range(T):
    cnt = 0
    k, n, m = map(int, input().split())
    first_k = k
    chargers = list(map(int, input().split()))
    chargers.insert(0, 0)
    # 시작점 추가
    chargers.append(n)
    # 종료점 추가
    distance = []
    # 충전소 간 거리 리스트
    for _ in range(len(chargers)-1):
        distance.append(chargers[_+1] - chargers[_])
    for i in range(len(distance)-1):
        k = k - distance[i]
        if first_k < max(distance):
            cnt = 0
            break
        elif k < distance[i + 1]:
            cnt += 1
            k = first_k
    print(f'#{cs+1}', cnt)