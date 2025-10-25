import sys
input = sys.stdin.readline

N = int(input())
coding = list(map(int, input().split()))
coding.sort()
answer = 0

for i in range(N):
    target = -coding[i]
    left = i + 1
    right = N - 1

    while left < right:
        two_sum = coding[left] + coding[right]
        if two_sum < target:
            left += 1
        elif two_sum > target:
            right -= 1
        else: # two_sum == target
            if coding[left] != coding[right]:
                left_value = coding[left]
                right_value = coding[right]

                # 왼쪽에 같은 값(left_value)이 연속으로 몇 명 있는지 센다
                cnt_left = 1
                while left + cnt_left < right and coding[left + cnt_left] == left_value:
                    cnt_left += 1

                # 오른쪽에 같은 값(right_value)이 연속으로 몇 명 있는지 센다
                cnt_right = 1
                while right - cnt_right > left and coding[right - cnt_right] == right_value:
                    cnt_right += 1

                # 이 조합들 각각은 전부 서로 다른 학생 조합이므로
                # 경우의 수 = cnt_left * cnt_right
                answer += cnt_left * cnt_right

                # 세야 할 학생을 처리했으므로, 포인터 한 번에 이동
                left += cnt_left
                right -= cnt_right

            else: # coding[left] == coding[right]
                # 이 구간에 남은 학생 수
                m = right - left + 1

                # m명 중 2명을 뽑는 조합 수 C(m, 2)
                answer += m * (m - 1) // 2

                # i에 대해 셀 조합 종료
                break

print(answer)
