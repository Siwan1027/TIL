# https://www.acmicpc.net/problem/5355
T = int(input())
for _ in range(T):
    formular = list(map(str, input().split()))
    result = float(formular[0])
    for i in range(1, len(formular)):
        if formular[i] == '@':
            result *= 3
        elif formular[i] == '%':
            result += 5
        elif formular[i] == '#':
            result -= 7
    print(format(result, '.2f'))
