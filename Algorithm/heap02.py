# 힙(Heap) > 디스크 컨트롤러

# jobs	                    return
# [[0, 3], [1, 9], [2, 6]]	9

def solution(jobs):
    jobs.sort(key=lambda x: x[0])  # 들어온 시간순으로 다시 정렬
    answer, now, length = 0, 0, len(jobs) # now = 현재 시간

    while len(jobs) != 0:
        pickIndex = -1
        # 먼저 실행시킬 스케줄을 찾아오는 로직 
        for i in range(len(jobs)):
            if jobs[i][0] <= now : # 현재 스케줄을 실행할수 있는지 확인하는 로직 
                if pickIndex == -1 or jobs[i][1] < jobs[pickIndex][1]:  # 걸리는 시간이 적은 스케줄을 확인
                    pickIndex = i
            else: # 실행할수 없을때
                break
        
        if pickIndex >= 0: # 실행 시킬 스케줄이 있는 경우
            k, v = jobs.pop(pickIndex)
            answer += now - k + v # 현재 모든 실행 시간을 계산하는 로직
            now += v  # 스케줄의 실행 완료 시간을 더해주는 로직
        else:
            now += 1 # 실행시킬 스케줄을 못찾은 경우 1초 시간 경과

    return answer // length


jobs1 = [[0, 3], [1, 9], [2, 6]]
result = solution(jobs1)
print(result)

