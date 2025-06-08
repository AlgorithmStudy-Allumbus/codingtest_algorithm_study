import heapq

def solution(jobs):
    jobs.sort()     # 요청시간 기준 정렬
    job_len = len(jobs)
    i = 0           # jobs 인덱스
    end_time = 0    # 현재 시간
    return_time = 0 # 작업 반환 시간
    count = 0       # 작업 처리한 개수

    heap = []

    while count < job_len:
        # 현재 시간에 요청된 작업 처리
        while i < job_len and jobs[i][0] <= end_time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0], i))  # 소요시간, 요청시간, 작업번호 순서
            i += 1

        # 대기 큐에 작업이 있다면, 시간을 업데이트한다.
        if len(heap) > 0:
            work_time, start_time, num = heapq.heappop(heap)
            end_time += work_time
            return_time += end_time - start_time
            count += 1
        else:
            # 대기 큐가 비었다면, 다음 작업이 올 때까지 기다려야 한다.
            end_time = jobs[i][0]

    return return_time // job_len