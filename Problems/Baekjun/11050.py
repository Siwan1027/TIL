# baekjun problem no.11650

import sys

N, K = map(int, sys.stdin.readline().split())

def factorial(num):
    if (num>1):
        return num * factorial(num-1)
    else:
        return 1
    
print(int(factorial(N)/(factorial(K)*factorial(N-K))))