'''

1. 입력 받기
2. dp에는 각 용량, 각 물건 당 넣을 수 있는 최대 가치를 저장.
예) dp[1][1]은 배낭 용량이 1이고, 넣을 수 있는 물건이 1까지 일떄 가질 수 있는 최대 가치
    2.1 점화식을 쓰기 위해 무게순으로 물건을 오름차순 정렬해야 할 듯
    2.2 반복문 안에서 현재 지정된 물건을 넣는 경우와 못 넣는 경우 두가지로 분리하여 생각
    2.3 현재 물건을 i라고 했을 때, 점화식은 i의 가치 + dp[i-1][(배낭 용량 - i의 무게)] , dp[i-1][j]
3. dp 배열 중 마지막 값, [N][K]번 요소 출력

'''

N, K = map(int, input().split())

arr = []

# 입력받기
for i in range(N):
    W, V = map(int, input().split())
    arr.append([W, V])

# 무게순으로 물건 오름차순 정렬
sorted_arr = sorted(arr, key=lambda x: x[0])

dp = [[0] * (K + 1) for i in range(N + 1)]

for i in range(N + 1):
    for j in range(K + 1):
        if i == 0 or j == 0:
            continue
        # 현재 배낭의 용량이 i번 물건을 담을 수 없는 경우
        if sorted_arr[i - 1][0] > j:
            # 이전 물건 기준 배낭의 최대 가치 그대로 가져오기
            dp[i][j] = dp[i - 1][j]
        else:
            # 현재 배낭의 용량이 i번 물건을 담을 수 있는 경우
            # 배낭에 물건을 담은 경우, 담지 않은 경우 두 가지 중 큰거 입력
            dp[i][j] = max(sorted_arr[i - 1][1] + dp[i - 1][j - sorted_arr[i - 1][0]], dp[i - 1][j])

print(dp[N][K])
