"""
# 우선순위 
- wait_que = [[작업 번호 , 작업 요청 시간 , 소요시간]]
- if wait_que : 
    #우선순위 높은 순 부터 작업 할당
    우선순위 : [소요시간 short  , 요청시간이 fast , 번호가 작은 것]
- intercept 없음 
- 같은 time 에 HD에 작업이 끝나는 시점 == 다른 작업 요청이 들어오는 시점일 경우, 
    HD 작업 종료 -> 바로 wait queue에서 ready queue로 할당
- 출력 : 각 jobs들의 반환 시각의 평균값의 정수부분
# INSPECT 
1. 다중 변수에 대한 우선순위 큐 사용하기
2. time += 1 각 time 별로 (1) wait 큐에 <- jobs 할당하기 (2) HD 에 <- wait 큐속 작업 할당하기 등 전체 작업 진행  
"""
import heapq
def solution(jobs):
    answer = 0 ; a = []
    wait = []
    # 반복문 종료 조건 : 모든 jobs가 HD 작업 종료
    finished = 0 ; t = 0 ; hd_timeout = -1 
    # time += 1 로 wait 큐와 HD 할당을 각 시각별로 확인 및 처리
    while finished < len(jobs) :
        # print(f"##t {t}")
        #[1] wait 큐에 요청 시각에 맞춰 작업 할당하기
        for idx , (accept_time , duration) in enumerate(jobs):
            if accept_time == t : 
                heapq.heappush(wait , [duration , accept_time, idx])

        #2. HD 작업 진행 여부 확인 
        #[1]. HD 작업 진행중 
        if hd_timeout > 0 : # HD 작업 진행중
            hd_timeout -=1 
        #[2] HD 작업 완료 및 비어 있을 때(hd_timout 음수 , 초기 시점)
        elif hd_timeout <= 0  :
            if hd_timeout == 0 : # (1) 진행중인 HD 작업 완료 -> 완료 작업 개수 += 1 
                a.append([t, start_t]) # 작업의 (종료 시점, 요청 시점) 을 정답 리스트에 반환
                finished += 1 
                hd_timeout = -1 # hd 비어있음
        
            # wait 큐의 존재하면 ->  wait큐에서 우선순위 작업을 뽑아 HD에 할당하기
            if wait : 
                hd_timeout , start_t , id = heapq.heappop(wait)
                hd_timeout = hd_timeout - 1

        t += 1

    # [4] 작업 반환 시간(turnaround_time) : 요청시간 - 완료 시간
    for e, s in a : 
        answer += (e - s) 
    answer = answer // len(a)

    return answer