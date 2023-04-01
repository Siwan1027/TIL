# https://www.acmicpc.net/problem/11021
T = int(input())

for cs in range(T):
    a, b = map(int, input().split())
    print(f'Case #{cs+1}:', a+b)