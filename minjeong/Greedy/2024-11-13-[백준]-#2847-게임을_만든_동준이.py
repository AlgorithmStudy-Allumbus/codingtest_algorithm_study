# 입력 예시: N과 각 레벨 점수 리스트
N = int(input())
scores = [int(input()) for _ in range(N)]

# 감소 횟수 변수
answer = 0

# 가장 높은 레벨부터 시작해서 점수를 조정
for i in range(N - 2, -1, -1):  # 뒤에서 두 번째 레벨부터 첫 번째 레벨까지
    if scores[i] >= scores[i + 1]:  # 다음 레벨 점수보다 크거나 같다면
        answer += scores[i] - (scores[i + 1] - 1)  # 감소해야 하는 횟수 증가
        scores[i] = scores[i + 1] - 1  # 다음 레벨보다 1 작게 설정

# 결과 출력
print(answer)