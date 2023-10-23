# baekjun problem no.4485
# 무조건 0,0 시작이며 4방향 탐색을 이용해 이동해야함
import sys, heapq

# 가중그래프로 표현된 동굴, 초기화 된 노드 간 가중치 리스트, 출발 x 좌표, 출발 y 좌표
def dijkstra(cave, cost, x, y):
    # 동굴 크기
    n = len(cave)
    # heapq 생성
    hq = []
    # 힙
    heapq.heappush(hq, (cave[x][y], x,y))      # 동굴의 각 칸의 크기를 힙큐에 넣는다.
    while hq:
        # 현재 가중치, x좌표, y좌표를 꺼냄
        curr_cost, curr_x, curr_y = heapq.heappop(hq)
        if cost[curr_x][curr_y] < curr_cost:      # 현재 위치의 가중치가 현 가중치보다 작을 경우, 즉 이미 최소 비용인 경우 다음으로 넘어간다.
            continue
        # 4방향 탐색
        for i in range(4):
            # 다음 위치 설정
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]
            # 위치가 적합한지 확인
            if 0 <= next_x < n and 0 <= next_y < n:
                # 다음 위치 비용 확인
                next_cost = cave[next_x][next_y] 
                # 현재 비용과 다음 위치로 이동하는 비용의 합이 다음 위치의 비용보다 작은지 확인
                if curr_cost + next_cost < cost[next_x][next_y]:
                    # 비용 최신화
                    heapq.heappush(hq, (curr_cost + next_cost, next_x, next_y))
                    cost[next_x][next_y] = curr_cost + next_cost
    # 동굴 끝에 갔을때 비용
    return cost[n-1][n-1]

input = sys.stdin.readline
# 4방햐야 이동 정의
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
# 누적 요금 초기화 값
inf = int(100000) 
# 테스트 카운터
t = 1

while 1:
    n = int(input())
    if n==0:
        break
    # 동굴 2차원 배열에 저장
    cave = [list(map(int,input().split())) for _ in range(n)]
    # 첫 비용 초기화
    cost = [[inf] * n for _ in range(n)]

    result = dijkstra(cave,cost,0,0)
    print(f'Problem {t}: {result}')
    t+=1