"""
프로그래머스. 디스크 컨트롤러
https://school.programmers.co.kr/learn/courses/30/lessons/42627
유형: Priority Queue
"""
"""
풀이1
"""
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


"""
풀이2
출처: https://velog.io/@kiwoong96/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4PythonLevel3-%EB%94%94%EC%8A%A4%ED%81%AC-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC
"""
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