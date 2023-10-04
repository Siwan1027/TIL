# baekjun problem no.4949
import sys

input = sys.stdin.readline

t = 1

while t :
    a = input()
    s = []

    if a[0] == "." :
        t = 0
        break

    for _ in a :
        if _ == '[' or _ == '(' :
            s.append(_)
        elif _ == ']' :
            if len(s) != 0 and s[-1] == '[' :
                s.pop()
            else : 
                break
        elif _ == ')' :
            if len(s) != 0 and s[-1] == '(' :
                s.pop()
            else :
                break
    print('yes') if len(s) == 0 else print('no')