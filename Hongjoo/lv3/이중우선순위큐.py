"""
- 우선순위 큐 함수 조건
    - l 숫자 : 큐에 해당 숫자 삽입
    - D -1 : 큐에서 최소값 삭제(빈 큐면 무시 )
    - D 1 : 큐에서 최대값 삭제
- 출력 : 연산 종료 후 큐가 비어 있음 [0,0] / 비어 있지 않음 [최대값, 최솟값]
- 
"""
import heapq
def solution(operations):
    answer = []
    heap = []

    def prior_queue(operate , heap) : # 입력 명령문 종류에 따라 3가지 동작 중 택 1을 적용한다. 
        
        action , num = operate.split()
        # [0] (예외처리)빈 heap에 삭제 명령이면, 무시한다. 
        if not heap and action == "D": 
            return heap
        # [1] 큐에 삽입하기
        if action == "I" : 
            heapq.heappush(heap , int(num))
         # [2] 최소값 삭제
        elif action == "D" and num == "-1":
            heapq.heapify(heap)
            heapq.heappop(heap)
       #[3] 최대값 삭제
        elif action == 'D' and num == "1" :
            heap = list(map(lambda x : -1*x , heap))
            heapq.heapify(heap)
            heapq.heappop(heap)
            heap = list(map(lambda x : -1*x , heap))
    
        return heap
    
    #2. 입력 명령문에 대해 반복 동작하기
    for o in operations : 
        heap=prior_queue(o , heap )

    #3. 출력 형태 맞춰 변형하기
    if len(heap) >=2  : # (1)안 비어 있으면 -> 최대값 & 최소값 출력
        heap.sort()
        return [heap[-1] , heap[0]]
    elif len(heap) < 1 : # (2) 비어 있음 -> [0,0]
        return [0,0]
    else : # (3) heap 이 1개 남아 있을떄 -> 최대값 = 최소값 *[테케 8,9,10]
        return [heap[0] , heap[0]]
    
    return answer