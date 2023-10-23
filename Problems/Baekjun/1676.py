# baekjun problem no.1676

import sys

n = int(sys.stdin.readline())

# def factorial(n):
#     if n == 1:      # n이 1일 때
#         return 1    # 1을 반환하고 재귀호출을 끝냄
#     return n * factorial(n - 1)    # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함
 

# print(str(factorial(n)).count('0'))

# 문제가 이해가 안돼서 참고한 블로그
# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1676%EB%B2%88-%ED%8C%A9%ED%86%A0%EB%A6%AC%EC%96%BC-0%EC%9D%98-%EA%B0%9C%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

# n = int(input())

def count_five(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

result = count_five(n)
print(result)
