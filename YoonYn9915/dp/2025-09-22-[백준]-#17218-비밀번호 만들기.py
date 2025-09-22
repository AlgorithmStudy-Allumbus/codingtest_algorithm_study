"""
1. 문제 요구사항
   - 두 문자열이 주어졌을 때, Longest Common Subsequence(LCS, 최장 공통 부분 수열)을 구한다.
   - 문자열의 길이는 최대 40이며, 빈 문자열은 주어지지 않는다.
   - 가장 긴 부분 수열은 반드시 하나만 존재한다.

2. 아이디어
   - 전형적인 LCS 문제이므로 2차원 DP 테이블을 사용한다.
   - arr[i][j] = str2[0..i-1]과 str1[0..j-1]까지의 최장 공통 부분 수열 길이
   - 문자 같을 때 → arr[i][j] = arr[i-1][j-1] + 1
   - 문자 다를 때 → arr[i][j] = max(arr[i-1][j], arr[i][j-1])
   - DP 테이블 계산 후, 역추적(backtracking)을 통해 실제 LCS 문자열을 복원한다.

3. 시간 복잡도
   - 문자열 길이가 최대 40이므로, DP 테이블 크기는 (41 x 41)
   - 각 칸을 채우는 데 O(1) → 전체 시간 복잡도는 O(n^2) (n ≤ 40)
   - 1초 제한에서 충분히 통과 가능

4. 세부 구현 방법
   - 입력: 두 문자열 str1, str2
   - DP 테이블 arr 초기화 (크기 (len(str2)+1) x (len(str1)+1))
   - 이중 반복문으로 arr 채우기
   - 마지막 위치 (len(str2), len(str1))에서 역추적 시작
     - 문자가 같으면 → 해당 문자 결과에 추가, 대각선 이동
     - 문자가 다르면 → 위 또는 왼쪽 중 더 큰 값 방향으로 이동
   - 역추적 결과는 뒤집혀 있으므로 reverse 후 출력
"""

import sys

inp = sys.stdin.readline

# 문자열 입력
str1 = inp().strip()
str2 = inp().strip()

len_str1 = len(str1)
len_str2 = len(str2)

# DP 테이블 초기화
arr = [[0] * (len_str1 + 1) for _ in range(len_str2 + 1)]

# LCS 길이 구하기
for i in range(1, len_str2 + 1):
    for j in range(1, len_str1 + 1):
        if str1[j-1] == str2[i-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])

# 역추적
answer = []
i, j = len_str2, len_str1

while i > 0 and j > 0:
    if str1[j-1] == str2[i-1]:
        answer.append(str1[j-1])
        i -= 1
        j -= 1
    elif arr[i-1][j] >= arr[i][j-1]:
        i -= 1
    else:
        j -= 1

# 결과는 뒤집혀 있으므로 reverse
answer.reverse()
print(''.join(answer))
