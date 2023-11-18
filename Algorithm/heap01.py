# 힙(Heap) > 더 맵게

# scoville	            K	return
# [1, 2, 3, 9, 10, 12]	7	2

# Step1 : [3, 9, 10, 12],  pop(1,2) -> 1 + (2 * 2) = 5
# Step2 : [3, 5, 9, 10, 12],  push(5) - sort - check
# Step3 : [9, 10, 12],  pop(3,5) -> 3 + (5 * 2) = 13
# Step4 : [9, 13, 10, 12],  push(13) - sort - check - OK, 2번 섞으면 된다.

def solution(scoville, K):
    count = 0
    scoville.sort()

    while True :
        print(scoville)

        # 답이 나왔는지 확인하는 로직
        isFinish = True
        for s in scoville:
            if s < K:
                isFinish = False
                break
        if isFinish:
            return count

        # 더이상 K이상의 스코빌 지수를 만들수 없을 때 체크
        if len(scoville) < 2:
            return -1
        
        # 스코빌 지수 계산하는 코드
        val1 = scoville.pop(0)
        val2 = scoville.pop(0)
        val3 = val1 + (val2 * 2) # 스코빌 지수 만드는 수식
        scoville.append(val3)
        scoville.sort()
        count = count + 1

    return count

scoville1 = [1, 2, 3, 9, 10, 12]
K1 = 7
result = solution(scoville1, K1)
print(result)
