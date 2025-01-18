def solution(strs, t):
    n = len(t)
    dp = [1e9] * (n + 1)  # 1e9는 불가능한 경우를 의미
    dp[0] = 0  # 초기값 설정: 시작점은 0

    # strs를 set으로 변환해 빠르게 포함 여부 확인
    str_set = set(strs)

    # DP 진행
    for i in range(1, n + 1):
        # 최대 5글자까지 확인
        for j in range(1, 6):
            if i - j >= 0 and t[i - j:i] in str_set:
                # 현재 위치를 j 길이만큼 뒤로 가서 비교
                dp[i] = min(dp[i], dp[i - j] + 1)

    # 결과 반환: 완성 가능하면 dp[n], 불가능하면 -1
    return dp[n] if dp[n] != 1e9 else -1