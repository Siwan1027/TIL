# baekjun problem no.1929
# 에라토스테네스의 채 https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
import sys

input = sys.stdin.readline

m,n = map(int,input().split())

def erasto(num):
    if num <2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
        
for i in range(m,n+1):
    if erasto(i):
        print(i)