def solution(n, times):
    left = min(times)
    right = max(times) * n
    answer = right  # 최소 시간을 구하는 문제이므로 초기값을 right로 설정

    while left <= right:
        mid = (left + right) // 2
        completed = 0

        # mid 시간 동안 각 심사관이 처리할 수 있는 사람 수를 계산
        for t in times:
            completed += mid // t

        # 모든 사람을 심사할 수 있는 경우
        if completed < n: # 시간이 부족하므로 더 많은 시간이 필요함
            left = mid + 1
        else: #  complete >= n
            answer = mid   # 최소 시간을 기록
            right = mid - 1# 시간을 더 줄여서 확인
    return answer