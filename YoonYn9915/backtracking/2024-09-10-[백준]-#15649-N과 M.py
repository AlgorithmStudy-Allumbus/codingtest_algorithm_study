def backtracking(cnt, arr):
    global answer, N, M
    if M == cnt:
        answer.append(arr[:])  # 결과를 복사해서 저장
        return

    for i in range(1, N+1):
        if i not in arr:  # 중복 방지
            arr.append(i)
            backtracking(cnt+1, arr)
            arr.pop()  # 마지막 원소 제거로 백트래킹

N, M = map(int, input().split())

answer = []

backtracking(0, [])

# answer 리스트에서 하나씩 출력
for ans in answer:
    print(" ".join(map(str, ans)))
