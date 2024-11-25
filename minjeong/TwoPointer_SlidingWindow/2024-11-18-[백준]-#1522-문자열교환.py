import sys
input = sys.stdin.readline

# 1. 문자열 입력받기
ab_str = input().rstrip()

# 2. a의 개수 계산
a = ab_str.count('a')

# 3. 원형 문자열 처리
ab_str += ab_str  # 문자열을 두 배로 늘림

# 4. 슬라이딩 윈도우로 최소 b의 개수 계산
answer = len(ab_str)  # 충분히 큰 초기값 설정
for i in range(len(ab_str) // 2):
    answer = min(answer, ab_str[i:i+a].count('b'))  # b의 개수 최소값 갱신

# 5. 결과 출력
print(answer)