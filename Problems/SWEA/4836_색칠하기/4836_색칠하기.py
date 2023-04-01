"""
1. test 횟수 T
2. n 색칠해야 하는 구간의 개수
3. input 을 n 번 받는다. 3번 칠한다
4. 빨강은 1로, 파랑은 2로 나타낸다.
5. 중복되는 경우가 있을 수 있으니 더할 값이 기존 값과 같다면 패스하자
6. 2차원 배열은 10x10 크기기 때문에 그냥 만든다.
7. 다 칠하고 값이 3인 원소의 개수를 세고 출력
8. 출력 형식은 # cs+1, cnt

3
2
2 2 4 4 1
3 3 6 6 2   #1 4
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2   #2 5
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2   #3 7



10
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2
5
1 6 8 3 1
3 4 5 2 2
"""

# import copy

T = int(input())

# m_field = [[0 for i in range(11)] for j in range(11)]
for cs in range(T):
    field = [[0 for i in range(11)] for j in range(11)]
    n = int(input())
    cnt = 0
    for _ in range(n):
        colors = list(map(int, input().split()))
        # colors = [2,2,4,4,1]
        rows = [colors[0], colors[2]]
        cols = [colors[1], colors[3]]
        for row in range(rows[0], rows[1]+1):
            for col in range(cols[0], cols[1]+1):
                if field[row][col] != colors[-1] and field[row][col] < 3:
                    field[row][col] += colors[-1]
                else:
                    pass
        for _ in range(len(field)):
            cnt += field[_].count(3)
    print(f'#{cs+1}', cnt)
