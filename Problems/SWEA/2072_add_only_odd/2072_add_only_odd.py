# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1
import sys
sys.stdin = open("input.txt")
T = int(input())

for _ in range(T):
    numbers = map(int, list(input().split()))
    tmp = 0
    for num in numbers:
        if num % 2:
            tmp += num

    print(f'#{_+1}', tmp)


