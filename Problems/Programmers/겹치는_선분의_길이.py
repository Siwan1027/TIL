# https://school.programmers.co.kr/learn/courses/30/lessons/120876
def solution(lines):
    length, intersections = [], []
    total = 0
    for _ in lines:
        a = set(range(min(_),max(_)+1))
        length.append(a)
    for i in range(len(length)):
        for j in range(i+1, len(length)):
            b = list(length[i].intersection(length[j]))
            b = list(length[i].intersection(length[j]))
            if bool(b) == False:
                pass
            else :
                total += abs(max(b)) - abs(min(b))
    return total
# 중복 배제가 안되네...

solution([[0, 5], [3, 9], [1, 10]])

solution([[0, 2], [-3, -1], [-2, 1]])