# https://www.acmicpc.net/problem/8958

T = int(input())

for _ in range(T):
    ox = input()
    score = 0
    tmp = 0
    for i in list(ox):
        if i == 'O':
            tmp += 1
            score += tmp
        elif i == 'X':
            tmp = 0
            score += tmp
    print(score)