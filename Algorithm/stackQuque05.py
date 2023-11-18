# 스택/큐 - 다리를 지나는 트럭

# 경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
# 0	        []	            []	                [7,4,5,6]
# 1	        []	            [7]	                [4,5,6]
# 2	        []	            [7]	                [4,5,6]
# 3	        [7]	            [4]	                [5,6]
# 4	        [7]	            [4,5]	            [6]
# 5     	[7,4]	        [5]	                [6]
# 6	        [7,4,5]	        [6]	                []
# 7	        [7,4,5]	        [6]	                []
# 8	        [7,4,5,6]	    []	                []

# bridge_length	weight	truck_weights	return
# 2	            10	    [7,4,5,6]	    8
# 100	        100	    [10]	        101
# 100	        100	    [10,10,10,10,10,10,10,10,10,10]	110

def solution(bridge_length, weight, truck_weights):
    waitQueue = [i for i in range(len(truck_weights))] # 트럭의 대기 댓수
    trunkNumToMoveLenDict = dict() # 실제 다리에 올라간 트럭의 이동한 거리를 계산하는 map
    roundCount, nowWeight, finishCount = 1, 0, 0
    
    for i in range(10) : # 무한 반복문 대신 for문으로 시뮬레이션
        if len(waitQueue) > 0 : # 트럭이 올라갈수 있는지 
            nextWeight = nowWeight + truck_weights[waitQueue[0]]
            if nextWeight <= weight : # 트럭이 다리에 올라갈수 있는지 무게 체크
                truckNum = waitQueue.pop(0)
                nowWeight += truck_weights[truckNum]
                trunkNumToMoveLenDict[truckNum] = 0
        
        # 다리 위에 올라간 트럭을 이동 시켜주는 계산을 하고, 이동이 끝난 트럭을 제거하는 코드
        truckSet = trunkNumToMoveLenDict.items()
        finishQueue = []
        for trunkNum, moveLen in truckSet :
            moveLen += 1
            if moveLen == bridge_length: # 끝난 조건
                finishQueue.append(trunkNum)
            else :
                trunkNumToMoveLenDict[truckNum] = moveLen

        # 끝난 트럭의 무게를 다리에서 빼주는 코드
        for deleteNum in finishQueue:
            trunkNumToMoveLenDict.pop(deleteNum)
            nowWeight -= truck_weights[deleteNum]

        roundCount += 1

        # 끝내는 조건부
        if len(waitQueue) == 0 and len(trunkNumToMoveLenDict) == 0 :
            break

    return roundCount


bridge_length1 = 2
weight1 = 10
truck_weights1 = [7, 4, 5, 6]
result = solution(bridge_length1, weight1, truck_weights1)