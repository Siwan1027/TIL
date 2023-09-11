# baekjun problem no.11399

import sys

T = int(sys.stdin.readline())

for i in range(T):
    C = int(sys.stdin.readline())
    q,d,n,p = (25,10,5,1)
    rq = C//q
    C -= rq*q
    rd = C//d
    C -= rd*d
    rn = C//n
    C -= rn*n
    rp = C//p
    C -= rp*p
    print(f'{rq} {rd} {rn} {rp}')
    