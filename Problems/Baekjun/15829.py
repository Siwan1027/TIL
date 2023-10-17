# baekjun problem no.15892

import sys
# 영 소문자 모듈
from string import ascii_lowercase

input = sys.stdin.readline

hash_dict = {letter:i for i, letter in enumerate(ascii_lowercase, start=1)}
hash_value = [31**i for i in range(50)]
n = int(input())
letters = input()
result_hash = 0
mod = 1234567891
for i in range(n):
    result_hash += (hash_dict[letters[i]]*hash_value[i])

print(result_hash % mod)