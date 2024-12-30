import sys

input = sys.stdin.readline

N, K = map(int, input().split())  # N: 멀티탭 구멍 개수, K: 전기용품 총 사용횟수
items = list(map(int, input().split()))  # 전기용품 사용 순서
multitap = []  # 현재 멀티탭
cnt = 0  # 플러그를 뽑는 횟수

for i in range(K):
    # 이미 꽂혀있는 경우
    if items[i] in multitap:
        continue

    # 멀티탭에 자리가 있는 경우
    if len(multitap) < N:
        multitap.append(items[i])
    else:
        # 교체할 전기용품 찾기
        remove_device = 0
        most_late_device = 0
        for d in multitap:
            if d not in items[i:]:  # 앞으로 사용되지 않는다면  바로 제거
                remove_device = d
                break

            else:  # 모든 기기가 다 사용되어야 한다면, 가장 나중에 사용되는 기기를 제거
                later_device = items[i:].index(d)
                if later_device > most_late_device:
                    most_late_device = later_device
                    remove_device = d

        # 플러그 교체
        multitap.remove(remove_device)
        multitap.append(items[i])
        cnt += 1

# 결과 출력
print(cnt)