# 26099 : 설탕 배달 2
import sys
input = sys.stdin.readline

N = int(input().strip()) # kg
bag_count = 0            # 봉지 수

while N >= 0:
    # 5kg 봉지 최대한 많이 사용해야 한다.
    if N % 5 == 0:  # 5의 배수인 경우, 5의 몫을 저장
        bag_count += N // 5
        print(bag_count)
        break
    N -= 3
    bag_count += 1
else:
    print(-1)