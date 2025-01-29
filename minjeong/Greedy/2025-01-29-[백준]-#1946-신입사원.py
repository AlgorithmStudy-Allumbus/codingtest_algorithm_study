import sys
input = sys.stdin.readline

T = int(input())  # 테스트 케이스 수

for _ in range(T):
    N = int(input())  # 지원자 수
    new_crew = []

    # 지원자 데이터 입력
    for _ in range(N):
        paper_score, interview_score = map(int, input().split())
        new_crew.append((paper_score, interview_score))

    # 서류 심사 순위 기준 정렬
    new_crew.sort()

    # 첫 번째 지원자는 무조건 선발
    answer = 1
    min_interview_rank = new_crew[0][1]

    # 두 번째 지원자부터 체크
    for i in range(1, N):
        if new_crew[i][1] < min_interview_rank:
            answer += 1
            min_interview_rank = new_crew[i][1]  # 최소 면접 등수 갱신

    print(answer)
