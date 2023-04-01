# https://www.acmicpc.net/problem/2588
x = int(input())
y = list(input())
for _ in y[::-1]:
    print(x*int(_))
print(x*int(''.join(y)))