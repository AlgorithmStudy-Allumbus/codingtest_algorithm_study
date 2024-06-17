import sys
input = sys.stdin.readline

s = input().rstrip()    # 문자열
q = int(input())        # 질문 개수
prefix_sum = [[0] * 26] # 누적합 리스트 초기화

# 입력한 문자열에 대한 누적합 구하기
# ord(): 아스키코드 구하는 함수
for i, ch in enumerate(s):
    prefix_sum.append(prefix_sum[len(prefix_sum) - 1][:]) # 직전 배열 복사(누적하여 저장 가능)
    prefix_sum[i+1][ord(ch) - 97] += 1   # 문자열 위치에서 해당 알파벳이 위치한 자리값 누적합

for _ in range(q):
    alpha, start, end = map(str, input().strip().split()) # 문자, 시작, 끝 입력
    ## 구간합 구하기
    # 누적합 - 구간
    answer = prefix_sum[int(end)+1][ord(alpha)-97] - prefix_sum[int(start)][ord(alpha)-97]
    print(answer)
